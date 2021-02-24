import sqlite3
import db_manager
from coin_cost import CoinCost

_DB_FILE_PATH = 'databases/cryptocurrency.db'
_DB_NAME = 'coin_costs'
_CREATE_TABLE_SQL = f"""CREATE TABLE IF NOT EXISTS {_DB_NAME} (
                        symbol text NOT NULL,
                        value real NOT NULL,
                        time text NOT NULL,
                        hour_percent_delta real,
                        day_percent_delta real,
                        week_percent_delta real,
                        month_percent_delta real
                    );"""

_conn, _cursor = db_manager.startup_database(_DB_FILE_PATH, _CREATE_TABLE_SQL)

def insert_coin_cost(coin_cost):
    with _conn:
        _cursor.execute(f'INSERT INTO {_DB_NAME} VALUES (?,?,?,?,?,?,?)', coin_cost.get_tuple())

## Used for testing
def print_all():
    entries = _cursor.execute(f'SELECT * FROM {_DB_NAME}').fetchall()
    for entry in entries:
        print(CoinCost(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6]))
print_all()