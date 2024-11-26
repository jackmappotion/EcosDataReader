from .data_reader.economic_index import EconomicIndexDataReader
from .data_reader.price_index import PriceIndexDataReader
from .data_reader.interest import InterestDataReader

from .data_reader.global_index import GlobalIndexDataReader
from .data_reader.foreign_currency import ForeignCurrencyDataReader

from .data_reader.bank import BankDataReader
from .data_reader.monetary import MonetaryDataReader

from .data_reader.market import MarketDataReader

from .data_reader.payment import PaymentDataReader
from .data_reader.trade import TradeDataReader


class EcosDataReader:
    def __init__(self, api_key):
        self.api_key = api_key
        self.economic_index_data_reader = EconomicIndexDataReader
        self.price_index_data_reader = PriceIndexDataReader
        self.interest_data_reader = InterestDataReader
        self.global_index_data_reader = GlobalIndexDataReader
        self.foreign_currency_data_reader = ForeignCurrencyDataReader
        self.bank_data_reader = BankDataReader
        self.monetary_data_reader = MonetaryDataReader
        self.market_data_reader = MarketDataReader
        self.payment_data_reader = PaymentDataReader
        self.trade_data_reader = TradeDataReader