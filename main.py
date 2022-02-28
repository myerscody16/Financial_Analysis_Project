from data_retrieval import get_json_data
from data_processing import prepare_df, create_scatter_plots
import pandas_bokeh


if __name__ == "__main__":
    raw_data = get_json_data()
    stock_df = prepare_df(raw_data[0])
    days_between = raw_data[1]
    print(stock_df.head())
    scatter_plots = create_scatter_plots(stock_df, days_between)
    pandas_bokeh.output_file('./financial_plots.html')
    pandas_bokeh.plot_grid([[scatter_plots[0]], [scatter_plots[1]], [scatter_plots[2]]])
