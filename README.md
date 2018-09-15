# Script To Downloads Stock Data from Alpha Vantage

A simple script to download stock data from alphavantage.co. Specifically it is setup to download the NASDAQ top 500. 


*Dependencies*:

  * [Python 2.7](https://www.python.org/download/releases/2.7/)

  * [Numpy](http://www.numpy.org/)

  * [Pandas](https://pandas.pydata.org/)
  
  * [urllib2](https://docs.python.org/2/library/urllib2.html)
  


```bash
pip install numpy
pip install pandas
pip install urllib2
pip install numpy
```

Get a free API key from [AlphaVantage](https://www.alphavantage.co/support/#api-key)

export the API key as an environmental variable. I recommend just adding it to your bashrc so it is always available.

``` bash
echo "export ALPHA_VANTAGE_KEY=<Your API Key Here>" >> ~/.bashrc
#Should look somthing like "export ALPHA_VANTAGE_KEY=AHKDSFJHUDFDJD"
source ~/.bashrc
```

You are now ready to run!

```bash
python download.py
```
