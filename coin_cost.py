from db_entry import DbEntry
from datetime import datetime
import re

class CoinCost(DbEntry):
    _COIN_MARKET_CAP_FORMAT_REGEX = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z$'
    _COIN_MARKET_CAP_FORMAT_DATETIME = f'%Y-%m-%dT%H:%M:%S.%fZ'
    _ISO_FORMAT_REGEX = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(\.\d+)?$'

    symbol = None
    value = None
    time = None
    hour_percent_delta = None
    day_percent_delta = None
    week_percent_delta = None
    month_percent_delta = None

    def __init__(self, symbol, value, time, hour_percent_delta, day_percent_delta, week_percent_delta, month_percent_delta):
        super().__init__()
        self.symbol = symbol
        self.value = value
        self.hour_percent_delta = hour_percent_delta
        self.day_percent_delta = day_percent_delta
        self.week_percent_delta = week_percent_delta
        self.month_percent_delta = month_percent_delta
        if re.search(self._COIN_MARKET_CAP_FORMAT_REGEX, time):
            self.time = self._convert_coin_market_format_to_iso_format(time)
        elif re.search(self._ISO_FORMAT_REGEX, time):
            self.time = time
        else:
            raise Exception(f'Time was improperly formatted: {time}')
    
    def _convert_coin_market_format_to_iso_format(self, timestamp):
        iso = datetime.strptime(timestamp, self._COIN_MARKET_CAP_FORMAT_DATETIME)
        # If you want to set minutes, seconds, and microseconds to 0:
        # iso = iso.replace(minute=0, second=0, microsecond=0)
        return str(iso)

    def _get_time_as_datetime(self):
        return datetime.fromisoformat(self.time)

    def get_tuple(self):
        return (
            self.symbol, 
            self.value, 
            self.time, 
            self.hour_percent_delta, 
            self.day_percent_delta, 
            self.week_percent_delta, 
            self.month_percent_delta
        )

    def __str__(self):
        return f'{{symbol: {self.symbol}, value: {self.value}, time: {self.time}, hour %: {self.hour_percent_delta}, day %: {self.day_percent_delta}, week %: {self.week_percent_delta}, month %: {self.month_percent_delta}}}'