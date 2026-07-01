import yfinance as yf
gold=yf.download(
    "GC=F" ,
    start="2016-01-01",
    end="2026-07-01"
)
gold.to_csv("data/raw/gold_prices.csv")
