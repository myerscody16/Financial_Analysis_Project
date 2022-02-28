import pandas as pd
import math


def prepare_df(json_data):
    df = pd.DataFrame(json_data)
    df = (df.join(pd.DataFrame.from_dict(df['results'].apply(pd.Series)))[['ticker', 'v', 'h', 'l', 't']]
            .rename(columns={'ticker': 'Ticker', 'v': 'Valuations', 'h': 'Daily_High', 'l': 'Daily_Low', 't': 'Timestamp'})
          )
    df['Timestamp'] = (pd.to_datetime(df['Timestamp'], unit='ms')
                       .apply(lambda x: x.strftime('%Y-%m-%d'))
                       )
    return df


def create_scatter_plots(stock_df, days_between):
    show_bool = False
    bin_width = math.floor(days_between/10)-1

    count = 0
    multiplier = 1
    bin_idx_lst = []
    while count < days_between:
        x = bin_width * multiplier
        if x > days_between:
            count = days_between + 1
        else:
            bin_idx_lst.append(x - 1)
            multiplier += 1

    high_plot = stock_df.plot_bokeh(title='Daily Highs', kind='scatter', x='Timestamp', y='Daily_High', xticks=bin_idx_lst, show_figure=show_bool)
    high_plot.xaxis.major_label_orientation = math.pi/3
    low_plot = stock_df.plot_bokeh(title='Daily Lows', kind='scatter', x='Timestamp', y='Daily_Low', xticks=bin_idx_lst, show_figure=show_bool)
    low_plot.xaxis.major_label_orientation = math.pi/3
    valuations = stock_df.plot_bokeh(title='Daily Valuations', kind='scatter', x='Timestamp', y='Valuations', xticks=bin_idx_lst, show_figure=show_bool)
    valuations.xaxis.major_label_orientation = math.pi/3
    return [high_plot, low_plot, valuations]
