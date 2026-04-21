from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orderbooks.orderbook import OrderBookData
from bt_api_base.functions.utils import from_dict_get_float, from_dict_get_int


class GateioOrderBookData(OrderBookData):
    def __init__(
        self,
        orderbook_info: str | dict,
        symbol_name: str,
        asset_type: str,
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(orderbook_info, has_been_json_encoded)
        self.exchange_name = "GATEIO"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.orderbook_data: Any = orderbook_info if has_been_json_encoded else None
        self.sequence_id: int | None = None
        self.current_time: float | None = None
        self.update_time: float | None = None
        self.bids: list[dict[str, float]] | None = None
        self.asks: list[dict[str, float]] | None = None
        self.all_data: dict[str, Any] | None = None
        self.has_been_init_data = False

    def init_data(self) -> GateioOrderBookData:
        if not self.has_been_json_encoded:
            self.orderbook_data = json.loads(self.order_book_info)
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        self.sequence_id = from_dict_get_int(self.orderbook_data, "id")
        self.current_time = from_dict_get_float(self.orderbook_data, "current")
        self.update_time = from_dict_get_float(self.orderbook_data, "update")

        self.bids = []
        if "bids" in self.orderbook_data and isinstance(self.orderbook_data["bids"], list):
            for bid in self.orderbook_data["bids"]:
                if isinstance(bid, list) and len(bid) >= 2:
                    self.bids.append(
                        {
                            "price": from_dict_get_float(bid, 0),
                            "amount": from_dict_get_float(bid, 1),
                        }
                    )

        self.asks = []
        if "asks" in self.orderbook_data and isinstance(self.orderbook_data["asks"], list):
            for ask in self.orderbook_data["asks"]:
                if isinstance(ask, list) and len(ask) >= 2:
                    self.asks.append(
                        {
                            "price": from_dict_get_float(ask, 0),
                            "amount": from_dict_get_float(ask, 1),
                        }
                    )

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.init_data()
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "asset_type": self.asset_type,
                "local_update_time": self.local_update_time,
                "sequence_id": self.sequence_id,
                "current_time": self.current_time,
                "update_time": self.update_time,
                "bids": self.bids,
                "asks": self.asks,
            }
        return self.all_data

    def __str__(self) -> str:
        self.init_data()
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_local_update_time(self) -> float:
        return self.local_update_time

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_sequence_id(self) -> int | None:
        return self.sequence_id

    def get_current_time(self) -> float | None:
        return self.current_time

    def get_update_time(self) -> float | None:
        return self.update_time

    def get_bids(self) -> list[dict[str, float]] | None:
        return self.bids

    def get_asks(self) -> list[dict[str, float]] | None:
        return self.asks

    def get_best_bid(self) -> float | None:
        if self.bids and len(self.bids) > 0:
            return self.bids[0]["price"]
        return None

    def get_best_ask(self) -> float | None:
        if self.asks and len(self.asks) > 0:
            return self.asks[0]["price"]
        return None

    def get_spread(self) -> float | None:
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()
        if best_bid and best_ask:
            return best_ask - best_bid
        return None

    def get_bid_depth(self, price_levels: int = 5) -> list[dict[str, float]]:
        if self.bids:
            return self.bids[:price_levels]
        return []

    def get_ask_depth(self, price_levels: int = 5) -> list[dict[str, float]]:
        if self.asks:
            return self.asks[:price_levels]
        return []


class GateioRequestOrderBookData(GateioOrderBookData):
    def init_data(self) -> GateioRequestOrderBookData:
        if not self.has_been_json_encoded:
            self.orderbook_data = json.loads(self.order_book_info)
            self.has_been_json_encoded = True

        if self.has_been_init_data:
            return self

        self.sequence_id = from_dict_get_int(self.orderbook_data, "id")
        self.current_time = from_dict_get_float(self.orderbook_data, "current")
        self.update_time = from_dict_get_float(self.orderbook_data, "update")

        self.bids = []
        if "bids" in self.orderbook_data and isinstance(self.orderbook_data["bids"], list):
            for bid in self.orderbook_data["bids"]:
                if isinstance(bid, list) and len(bid) >= 2:
                    self.bids.append(
                        {
                            "price": from_dict_get_float(bid, 0),
                            "amount": from_dict_get_float(bid, 1),
                        }
                    )

        self.asks = []
        if "asks" in self.orderbook_data and isinstance(self.orderbook_data["asks"], list):
            for ask in self.orderbook_data["asks"]:
                if isinstance(ask, list) and len(ask) >= 2:
                    self.asks.append(
                        {
                            "price": from_dict_get_float(ask, 0),
                            "amount": from_dict_get_float(ask, 1),
                        }
                    )

        self.has_been_init_data = True
        return self


class GateioWssOrderBookData(GateioOrderBookData):
    def init_data(self) -> GateioWssOrderBookData:
        return self
