import yfinance as yf
gold=yf.download(
    "GC=F" ,
    start="2016-01-01",
    end="2026-07-01"
)

if gold.columns.nlevels>1:
    gold.columns=gold.columns.get_level_values(0)
gold.reset_index(inplace=True)
gold.to_csv("data/raw/gold_prices.csv",index=False)
print("Data updated successfully")