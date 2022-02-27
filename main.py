from data_retrieval import get_json_data
from data_processing import prepare_df

if __name__ == "__main__":
    raw_data = get_json_data()
    stock_df = prepare_df(raw_data)
    print(stock_df.head())
