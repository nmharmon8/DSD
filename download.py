'''
Downloads stock data from stooq.com. The default data is nasdaq 
but any stock stmbol can be downloaded using this scrip if the 
stock is available on stooq.com
'''

import urllib2
import pandas as pd 
import os

'''
Saves data to a file
'''
def save(data, output_dir, filename):
    try:
        #the output dir may not exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    except Exception as ex:
        print('Could not create output dir')
        print(ex)
        return
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, 'wb') as f:
            f.write(data)
    except Exception as ex:
        print('Could not open file {} to write data'.format(filepath))
        print(ex)

'''
Given a stock ticker (aka 'tsla') will download and save the data to the
out put dir as a csv 
'''
def download_ticker(ticker, output_dir):
    try:
        filedata = urllib2.urlopen('https://stooq.com/q/d/l/?s={}.us&i=d'.format(ticker))
        dataowire = filedata.read()
        save(dataowire, output_dir, '{}.csv'.format(ticker))
    except Exception as ex:
        print('Could not download {}'.format(ticker))
        print(ex)


if __name__ == '__main__':
    df = pd.read_csv('companylist.csv')
    # Nasdaq 100 
    df = df.sort_values(by=['MarketCap'], ascending=False)
    df = df[:100]
    for symbol in df.Symbol:
        print('Downloading {}'.format(symbol))
        download_ticker(symbol, 'stock_data')

