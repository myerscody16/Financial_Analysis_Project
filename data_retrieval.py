import requests
from datetime import datetime
from creds import api_params


def get_json_data():
    current_date = datetime.now()
    start_date = datetime(2019, 1, 1)
    comp_name = 'AAPL'

    res = requests.get("https://api.polygon.io/v2/aggs/ticker/{company_name}/range/1/day/{start_date}/{current_date}?adjusted=true&sort=asc&limit=120&apiKey={api_key}".format(company_name = comp_name,
                                                                                                                                                                               start_date = start_date.strftime(('%Y-%m-%d')),
                                                                                                                                                                               current_date = current_date.strftime(('%Y-%m-%d')),
                                                                                                                                                                               api_key = api_params['access_key'])
                       )
    return res.json()
