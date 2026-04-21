"""Tests for exchange_registers/register_gateio.py."""

from __future__ import annotations

from bt_api_gateio.registry_registration import register_gateio


class TestRegisterGateio:
    """Tests for Gate.io registration module."""

    def test_module_imports(self):
        """Test module can be imported."""
        assert register_gateio is not None
