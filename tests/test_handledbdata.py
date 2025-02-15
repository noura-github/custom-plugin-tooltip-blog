
import sqlite3
import pytest
from unittest.mock import MagicMock, patch

from handledbdata import find_image_file


def test_find_image_file(mocker):
    # Mock the sqlite3.connect method
    mock_conn = mocker.patch('sqlite3.connect', return_value=MagicMock())

    # Create a mock cursor
    mock_cursor = mock_conn.return_value.cursor.return_value

    # Set up the mock to return a specific value when fetchone is called
    mock_cursor.fetchone.return_value = ('image_file.png',)

    # Call the function with a test file_id
    result = find_image_file(1)

    # Assert that the result is as expected
    assert result == ('image_file.png',)

    # Assert that the database connection and cursor were called correctly
    mock_conn.assert_called_once_with('custom_plugin.db')
    mock_cursor.execute.assert_called_once_with('''
        SELECT file FROM files WHERE id = ?
    ''', (1,))

    # Assert that the connection was closed
    mock_conn.return_value.close.assert_called_once()