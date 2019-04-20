# Script To Downloads Stock Data from Alpha Vantage

A simple script to download stock data from alphavantage.co. Specifically it is setup to download the NASDAQ top 500. 


*Dependencies*:

  * [Python 3](https://www.python.org/download/releases/3.0/)

  * [Numpy](http://www.numpy.org/)

  * [Pandas](https://pandas.pydata.org/)
  
  * [urllib](https://docs.python.org/3/library/urllib.html)
  
###Install
```bash
cd DSD
sudo python setup.py install
```
###Setup API
Get a free API key from [AlphaVantage](https://www.alphavantage.co/support/#api-key)

export the API key as an environmental variable. I recommend just adding it to your bashrc so it is always available.

``` bash
echo "export ALPHA_VANTAGE_KEY=<Your API Key Here>" >> ~/.bashrc
#Should look somthing like "export ALPHA_VANTAGE_KEY=AHKDSFJHUDFDJD"
source ~/.bashrc
```

You are ready!

```python
from dsd import download_nasdaq_data as dnd

'''
Downloads multiple companies
'''
dnd.downloadNTopMarketCapCompanies(500, output_dir='stock_data')

'''
Given a stock symbol (aka 'tsla') will download and save the data to the
output dir as a csv 
'''
dnd.download_symbol(symbol, output_dir, retry_count=4)
```

Have fun.
