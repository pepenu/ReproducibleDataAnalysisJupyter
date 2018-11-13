import os
import pandas as pd
from urllib.request import urlretrieve

# keep the URL for future reference
FREMONT_URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"


def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL,
                     force_download=False):
    '''Download and cash the frmont data

    Parameters
    ----------
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force redownload of data

    Returns
    -------
    data : pandas.DataFrame
        The Fremont bridge data
    '''

    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv',index_col='Date',parse_dates=True)
    data.columns = ['West','East']
    data['Total'] = data['West'] + data['East']
    return data
