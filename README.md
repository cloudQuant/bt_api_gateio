# Gate.io

Gate.io exchange plugin for bt_api, supporting Spot and Futures trading.

[![PyPI Version](https://img.shields.io/pypi/v/bt_api_gateio.svg)](https://pypi.org/project/bt_api_gateio/)
[![Python Versions](https://img.shields.io/pypi/pyversions/bt_api_gateio.svg)](https://pypi.org/project/bt_api_gateio/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/cloudQuant/bt_api_gateio/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudQuant/bt_api_gateio/actions)
[![Docs](https://readthedocs.org/projects/bt-api-gateio/badge/?version=latest)](https://bt-api-gateio.readthedocs.io/)

---

## English | [中文](#中文)

### Overview

This package provides **Gate.io exchange plugin for bt_api** for the [bt_api](https://github.com/cloudQuant/bt_api_py) framework. It offers a unified interface for interacting with **Gate.io** exchange.

### Features

- Spot and futures trading
- REST and WebSocket APIs
- Order book depth data
- Trade history
- Balance management

### Installation

```bash
pip install bt_api_gateio
```

Or install from source:

```bash
git clone https://github.com/cloudQuant/bt_api_gateio
cd bt_api_gateio
pip install -e .
```

### Quick Start

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

### Supported Operations

| Operation | Status |
|-----------|--------|
| Ticker | ✅ |
| OrderBook | ✅ |
| Trades | ✅ |
| Bars/Klines | ✅ |
| Orders | ✅ |
| Balances | ✅ |
| Positions | ✅ |

### Online Documentation

| Resource | Link |
|----------|------|
| English Docs | https://bt-api-gateio.readthedocs.io/ |
| Chinese Docs | https://bt-api-gateio.readthedocs.io/zh/latest/ |
| GitHub Repository | https://github.com/cloudQuant/bt_api_gateio |
| Issue Tracker | https://github.com/cloudQuant/bt_api_gateio/issues |

### Requirements

- Python 3.9+
- bt_api_base >= 0.15

### Architecture

```
bt_api_gateio/
├── src/bt_api_gateio/     # Source code
│   ├── containers/     # Data containers
│   ├── feeds/          # API feeds
│   ├── gateway/       # Gateway adapter
│   └── plugin.py      # Plugin registration
├── tests/             # Unit tests
└── docs/             # Documentation
```

### License

MIT License - see [LICENSE](LICENSE) for details.

### Support

- Report bugs via [GitHub Issues](https://github.com/cloudQuant/bt_api_gateio/issues)
- Email: yunjinqi@gmail.com

---

## 中文

### 概述

本包为 [bt_api](https://github.com/cloudQuant/bt_api_py) 框架提供 **Gate.io exchange plugin for bt_api**。它提供了与 **Gate.io交易所** 交易所交互的统一接口。

### 功能特点

- 现货和期货交易
- REST 和 WebSocket API
- 订单簿深度数据
- 交易历史
- 余额管理

### 安装

```bash
pip install bt_api_gateio
```

或从源码安装：

```bash
git clone https://github.com/cloudQuant/bt_api_gateio
cd bt_api_gateio
pip install -e .
```

### 快速开始

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

### 支持的操作

| 操作 | 状态 |
|------|------|
| Ticker | ✅ |
| OrderBook | ✅ |
| Trades | ✅ |
| Bars/Klines | ✅ |
| Orders | ✅ |
| Balances | ✅ |
| Positions | ✅ |

### 在线文档

| 资源 | 链接 |
|------|------|
| 英文文档 | https://bt-api-gateio.readthedocs.io/ |
| 中文文档 | https://bt-api-gateio.readthedocs.io/zh/latest/ |
| GitHub 仓库 | https://github.com/cloudQuant/bt_api_gateio |
| 问题反馈 | https://github.com/cloudQuant/bt_api_gateio/issues |

### 系统要求

- Python 3.9+
- bt_api_base >= 0.15

### 架构

```
bt_api_gateio/
├── src/bt_api_gateio/     # 源代码
│   ├── containers/     # 数据容器
│   ├── feeds/          # API 源
│   ├── gateway/        # 网关适配器
│   └── plugin.py       # 插件注册
├── tests/             # 单元测试
└── docs/             # 文档
```

### 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE)。

### 技术支持

- 通过 [GitHub Issues](https://github.com/cloudQuant/bt_api_gateio/issues) 反馈问题
- 邮箱: yunjinqi@gmail.com

## Provider role and integration boundary

`plugin.py` advertises `GATEIO___SPOT` and `GATEIO___SWAP`; `registry_registration.py` wires request-feed, exchange-data, and balance handlers. Its current subscribe handlers only log requested topics and do not start WebSocket consumers, so stream registration is not evidence of a live stream or trading capability. This provider package owns Gate.io-specific API adaptation; `bt_api_base` supplies the shared plugin protocol and registry, while Backtrader owns strategy and backtest logic. See [Trading system architecture](https://github.com/cloudQuant/backtrader/blob/dev/docs/TRADING_SYSTEM_ARCHITECTURE.md).

## 提供方职责与集成边界

`plugin.py` 列出 `GATEIO___SPOT` 和 `GATEIO___SWAP`；`registry_registration.py` 注册请求 Feed、交易所数据和余额处理器。目前的订阅处理器只记录请求的 topic，不会启动 WebSocket 消费者，因此注册订阅处理器不代表实时数据流或交易能力已可用。本包负责 Gate.io 专用 API 适配；`bt_api_base` 提供共享插件协议和注册表，Backtrader 负责策略与回测逻辑。架构说明：[Trading system architecture](https://github.com/cloudQuant/backtrader/blob/dev/docs/TRADING_SYSTEM_ARCHITECTURE.md)。
