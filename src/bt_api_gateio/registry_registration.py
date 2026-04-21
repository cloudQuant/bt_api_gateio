from __future__ import annotations

from typing import Any

from bt_api_base.balance_utils import nested_balance_handler as _gateio_balance_handler
from bt_api_gateio.exchange_data.gateio_exchange_data import (
    GateioExchangeDataSpot,
    GateioExchangeDataSwap,
)
from bt_api_gateio.feeds.live_gateio.spot import GateioRequestDataSpot
from bt_api_gateio.feeds.live_gateio.swap import GateioRequestDataSwap
from bt_api_base.registry import ExchangeRegistry


def _gateio_spot_subscribe_handler(
    data_queue: Any, exchange_params: Any, topics: Any, bt_api: Any
) -> None:
    topic_list = [i["topic"] for i in topics]
    bt_api.log(f"Gate.io Spot topics requested: {topic_list}")


def _gateio_swap_subscribe_handler(
    data_queue: Any, exchange_params: Any, topics: Any, bt_api: Any
) -> None:
    topic_list = [i["topic"] for i in topics]
    bt_api.log(f"Gate.io Swap topics requested: {topic_list}")


def register_gateio(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("GATEIO___SPOT", GateioRequestDataSpot)
    registry.register_exchange_data("GATEIO___SPOT", GateioExchangeDataSpot)
    registry.register_balance_handler("GATEIO___SPOT", _gateio_balance_handler)
    registry.register_stream("GATEIO___SPOT", "subscribe", _gateio_spot_subscribe_handler)

    registry.register_feed("GATEIO___SWAP", GateioRequestDataSwap)
    registry.register_exchange_data("GATEIO___SWAP", GateioExchangeDataSwap)
    registry.register_balance_handler("GATEIO___SWAP", _gateio_balance_handler)
    registry.register_stream("GATEIO___SWAP", "subscribe", _gateio_swap_subscribe_handler)
