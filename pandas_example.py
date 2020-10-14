import pandas as pd
import numpy as np
import time
import sqlite3
from contextlib import contextmanager
import io
import sqlalchemy

@contextmanager
def watch(name):
    start = time.time()
    yield
    process_time =  time.time() - start
    print(f"{name}は{process_time}秒かかりました")

def create_dummy_data(rows,columns=3):
    labels = [f'col_{i:0>5}' for i in range(columns)]
    data = np.random.randn(rows,columns)
    return pd.DataFrame(data,columns=labels)

data = create_dummy_data(1000000)
db_file = 'test.db'
conn = sqlite3.connect(db_file)

with watch('raw to_csv'):
    data.to_csv('test.csv')
with watch('zip to_csv'):
    data.to_csv('test.csv.zip',compression='zip')
with watch('gz to_csv'):
    data.to_csv('test.csv.gz',compression='gzip')
with watch('bz2 to_csv'):
    data.to_csv('test.csv.bz2',compression='bz2')
with watch('to_sql'):
    data.to_sql('test_table',conn,if_exists='replace')
with watch('to_feather'):
    data.to_feather('test.feather')
# very slow
# with watch('xz to_csv'):
#     data.to_csv('test.csv.xz',compression='xz')
with watch('raw read_csv'):
    pd.read_csv('test.csv')
with watch('zip read_csv'):
    pd.read_csv('test.csv.zip',compression='zip')
with watch('gz read_csv'):
    pd.read_csv('test.csv.gz',compression='gzip')
with watch('bz2 read_csv'):
    pd.read_csv('test.csv.bz2',compression='bz2')
with watch('read_sql_query'):
    pd.read_sql_query('select * from test_table',conn)
with watch('raw feather'):
    pd.read_feather('test.feather')

# very slow
# with watch('xz read_csv'):
#     pd.read_csv('test.csv.xz',compression='xz')