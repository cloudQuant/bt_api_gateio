# Gate.io Documentation

## English

Welcome to the Gate.io documentation for bt_api.

### Quick Start

```bash
pip install bt_api_gateio
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "GATEIO___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("GATEIO___SPOT", "BTC_USDT")
print(ticker)
```

## 中文

欢迎使用 bt_api 的 Gate.io交易所 文档。

### 快速开始

```bash
pip install bt_api_gateio
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "GATEIO___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("GATEIO___SPOT", "BTC_USDT")
print(ticker)
```

## API Reference

See source code in `src/bt_api_gateio/` for detailed API documentation.
