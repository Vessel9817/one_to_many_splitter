"""Tests for UI module."""
from src import ui
from unittest.mock import patch


class TestExpandAsBase:
    def test_simple(self):
        result = ui.expand_as_base(6, {(0, 1)})
        assert result == "1"

    def test_complex(self):
        result = ui.expand_as_base(6, {(0, 1), (1, 2), (2, 3)})
        assert result == "1 + 2\xb76\xb9 + 3\xb76\xb2"

    def test_negative(self):
        result = ui.expand_as_base(6, [(0, -1), (1, 2), (2, 3)])
        assert result == "-1 + 2\xb76\xb9 + 3\xb76\xb2"

    def test_negative_complex(self):
        result = ui.expand_as_base(6, [(0, -1), (1, -2), (2, -3)])
        assert result == "-1 - 2\xb76\xb9 - 3\xb76\xb2"

    def test_zero(self):
        result = ui.expand_as_base(6, {})
        assert result == "0"

    


class TestGetInt:
    def test_valid_input(self):
        with patch("builtins.input", return_value="5"):
            result = ui.get_int(lambda n: n > 0)
            assert result == 5

    def test_invalid_then_exit(self):
        with patch("builtins.input", side_effect=["invalid", "q"]):
            result = ui.get_int(lambda n: n > 0, exit_phrase="q")
            assert result is None

    def test_exit_phrase(self):
        with patch("builtins.input", return_value="q"):
            result = ui.get_int(lambda n: n > 0, exit_phrase="q")
            assert result is None

    def test_negative_number_fails_condition(self):
        with patch("builtins.input", side_effect=["-5", "q"]):
            result = ui.get_int(lambda n: n > 0, exit_phrase="q")
            assert result is None

    def test_no_exit_phrase(self):
        with patch("builtins.input", return_value="42"):
            result = ui.get_int(lambda n: n > 0)
            assert result == 42