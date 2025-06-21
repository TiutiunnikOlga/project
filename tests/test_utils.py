from unittest.mock import patch, mock_open
from src.utils import fin_operations


def test_fin_operations():
    mock_file = mock_open(read_data='[{"A": "G"}]')
    with patch("builtins.open", mock_file):
        result = fin_operations("operation.json")
        assert result == [{"A": "G"}]
