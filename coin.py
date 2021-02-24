from db_entry import DbEntry

class Coin(DbEntry):
    symbol = None
    name = None
    slug = None
    max_supply = None

    def __init__(self, symbol, name, slug, max_supply):
        super().__init__()
        self.symbol = symbol
        self.name = name
        self.slug = slug
        self.max_supply = max_supply

    def get_tuple(self):
        return (self.symbol, self.name, self.slug, self.max_supply)

    def __str__(self):
        return f'{{symbol: {self.symbol}, name: {self.name}, slug: {self.slug}, max_supply: {self.max_supply}}}'