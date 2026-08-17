"""Module-level docstring."""
import base64
from bt_api_gateio.feeds.live_gateio.request_base import GateioRequestData
def test_gateio_accepts_api_key_and_api_secret_aliases() -> None:
    """test_gateio_accepts_api_key_and_api_secret_aliases function"""
    request_data = GateioRequestData(api_key="public-key", api_secret="secret-key")
    headers = request_data._build_auth_headers("GET", "/api/v4/spot/accounts")

    assert request_data.public_key == "public-key"
    assert request_data.private_key == "secret-key"
    assert headers["KEY"] == "public-key"
    assert headers["SIGN"]


def test_gateio_error_response_raises_invalid_signature() -> None:
    """API 错误(label 非空)必须翻译为 UnifiedError 并抛出。"""
    import pytest

    from bt_api_base.error import UnifiedError

    request_data = GateioRequestData(api_key="pk", api_secret="sk")
    with pytest.raises(UnifiedError):
        request_data._raise_if_error({"label": "INVALID_SIGNATURE", "message": "bad sign"})


def test_gateio_error_response_raises_balance_not_enough() -> None:
    import pytest

    from bt_api_base.error import UnifiedError

    request_data = GateioRequestData(api_key="pk", api_secret="sk")
    with pytest.raises(UnifiedError):
        request_data._raise_if_error(
            {"label": "BALANCE_NOT_ENOUGH", "message": "Insufficient balance"}
        )


def test_gateio_error_response_raises_rate_limit() -> None:
    import pytest

    from bt_api_base.error import UnifiedError

    request_data = GateioRequestData(api_key="pk", api_secret="sk")
    with pytest.raises(UnifiedError):
        request_data._raise_if_error(
            {"label": "RATE_LIMIT_EXCEEDED", "message": "Too many requests"}
        )


def test_gateio_success_response_does_not_raise() -> None:
    """成功响应(无 label)不抛异常。"""
    request_data = GateioRequestData(api_key="pk", api_secret="sk")
    request_data._raise_if_error({"result": "ok", "currency_pair": "BTC_USDT"})
