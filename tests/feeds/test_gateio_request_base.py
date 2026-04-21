import base64
from bt_api_gateio.feeds.live_gateio.request_base import GateioRequestData
def test_gateio_accepts_api_key_and_api_secret_aliases() -> None:
    request_data = GateioRequestData(api_key="public-key", api_secret="secret-key")
    headers = request_data._build_auth_headers("GET", "/api/v4/spot/accounts")

    assert request_data.public_key == "public-key"
    assert request_data.private_key == "secret-key"
    assert headers["KEY"] == "public-key"
    assert headers["SIGN"]
