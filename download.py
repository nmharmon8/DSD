'''
Downloads stock data from nasdaq.
'''
import pandas as pd 
import os
import requests
from bs4 import BeautifulSoup
import time
'''
Saves data to a file
'''
def save_df(df, output_dir, filename):
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
       df.to_csv(filepath, index=False)
    except Exception as ex:
        print('Could not open file {} to write data'.format(filepath))
        print(ex)


def html_table_to_df(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    columns = [column.text.replace('"', '').strip().split(' ')[0].strip() for column in table.find_all('th')]
    rows = []

    for row in table.find_all('tr'):
        row = [val.text.encode('utf8').strip() for val in row.find_all('td')]
        #Make sure the list is not empty
        if row:
            rows.append(row)
    df = pd.DataFrame(data=rows, columns=columns)
    df['Date'] = pd.to_datetime(df.Date)
    df = df.sort_values(by='Date')
    df['Volume'] = df['Volume'].map(lambda x: float(x.replace(',', '')))
    return df


def try_download(ticker):
    try:
        response = requests.post('https://www.nasdaq.com/symbol/{}/historical'.format(ticker.lower()), headers = {'Content-Type': 'application/json'}, data="10y|false|{}".format(ticker.upper()))
        return response
    except:
        return None

'''
Given a stock ticker (aka 'tsla') will download and save the data to the
out put dir as a csv 
'''
def download_ticker(ticker, output_dir, retry_count=4):
    try:
        response = try_download(ticker)
        while (not response or not response.text or 'table' not in response.text) and retry_count > 0:
            print('Retrying.....')
            time.sleep(5)
            response = try_download(ticker)
            retry_count -= 1

        if response.status_code == 200:
            df = html_table_to_df(response.text)
            save_df(df, output_dir, '{}.csv'.format(ticker))
        else:
            print('Download failed with retry')
    except Exception as ex:
        print('Could not download {}'.format(ticker))
        print(ex)


if __name__ == '__main__':
    df = pd.read_csv('companylist.csv')
    # Nasdaq 500 
    df = df.sort_values(by=['MarketCap'], ascending=False)
    df = df[:500]
    for symbol in df.Symbol:
        print('Downloading {}'.format(symbol))
        download_ticker(symbol, 'stock_data')


