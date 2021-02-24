import sqlite3
import db_manager
from coin import Coin

_DB_FILE_PATH = 'databases/cryptocurrency.db'
_DB_NAME = 'coins'
_CREATE_TABLE_SQL = f"""CREATE TABLE IF NOT EXISTS {_DB_NAME} (
                        symbol text PRIMARY KEY,
                        name text NOT NULL,
                        slug text,
                        max_supply integer DEFAULT 0
                    );"""

_conn, _cursor = db_manager.startup_database(_DB_FILE_PATH, _CREATE_TABLE_SQL)

def insert_coin(coin):
    with _conn:
        _cursor.execute(f'REPLACE INTO {_DB_NAME} VALUES (?,?,?,?)', coin.get_tuple())

def get_coin(symbol):
    entry = _cursor.execute(f'SELECT symbol, name, slug, max_supply FROM {_DB_NAME} WHERE id = ?', (symbol,)).fetchone()
    return Coin(entry[0], entry[1], entry[2], entry[3])

## Used for testing
def print_all():
    entries = _cursor.execute(f'SELECT symbol, name, slug, max_supply FROM {_DB_NAME}').fetchall()
    for entry in entries:
        print(Coin(entry[0], entry[1], entry[2], entry[3]))
