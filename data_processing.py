import pandas as pd


def prepare_df(json_data):
    df = pd.DataFrame(json_data)
    df = (df.join(pd.DataFrame.from_dict(df['results'].apply(pd.Series)))[['ticker', 'v', 'h', 'l', 't']]
            .rename(columns = {'ticker': 'Ticker', 'v': 'Value', 'h': 'Daily_high', 'l': 'Daily_low', 't': 'Timestamp'})
          )
    df['Timestamp'] = (pd.to_datetime(df['Timestamp'], unit='ms')
                       .apply(lambda x: x.strftime('%Y-%m-%d'))
                       )
    return df
