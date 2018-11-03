'''
Downloads stock data from alphavantage
'''
import pandas as pd 
import os
import time
from urllib.request import urlopen
from io import StringIO
import inspect

   
current_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
companylist_path = os.path.join(current_directory, 'companylist.csv')

if 'ALPHA_VANTAGE_KEY' not in os.environ:
    print('Get a free API key from [AlphaVantage](https://www.alphavantage.co/support/#api-key)\n\nexport the API key as an environmental variable. I recommend just adding it to your bashrc so it is always available.\n\necho "export ALPHA_VANTAGE_KEY=<Your API Key Here>" >> ~/.bashrc\n#Should look somthing like "export ALPHA_VANTAGE_KEY=AHKDSFJHUDFDJD"\nsource ~/.bashrc')
    exit()


ALPHA_VANTAGE_KEY = os.environ['ALPHA_VANTAGE_KEY']


'''
Saves data to a file
'''
def save(stock_csv, output_dir, filename):
    try:
        #the output dir may not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    except Exception as ex:
        print('Could not create output dir')
        print(ex)
        return
    filepath = os.path.join(output_dir, filename)
    print(filepath)
    try:
       df = pd.read_csv(StringIO(stock_csv))
       df = df.sort_values(by='timestamp')  
       df.to_csv(filepath, index=False)
    except Exception as ex:
        print('Could not open file {} to write data'.format(filepath))
        print(ex)


def try_download(symbol):
    try:
        # Keep call frequency below threshold 
        time.sleep(12)
        response = urlopen('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}&datatype=csv&outputsize=full'.format(symbol, ALPHA_VANTAGE_KEY))
        stock_csv = response.read()
        print(stock_csv)
        return stock_csv
    except Exception as ex:
        return None


'''
Given a stock symbol (aka 'tsla') will download and save the data to the
output dir as a csv 
'''
def download_symbol(symbol, output_dir, retry_count=4):

    stock_csv = try_download(symbol)
    if stock_csv:
        save(stock_csv, output_dir, '{}.csv'.format(symbol))
    else:
        print('Failed to download {}'.format(symbol))
       
'''
Downloads multiple companies 
'''
def downloadNTopMarketCapCompanies(n, output_dir='stock_data'):
    df = pd.read_csv(companylist_path) 
    df = df.sort_values(by=['MarketCap'], ascending=False)
    df = df[:n]
    for symbol in df.Symbol:
        print('Downloading {}'.format(symbol))
        download_symbol(symbol, output_dir)



if __name__ == '__main__':
    # Nasdaq 500 
    downloadNTopMarketCapCompanies(500)
    