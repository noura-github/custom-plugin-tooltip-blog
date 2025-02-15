
import sqlite3
import pytest
from unittest.mock import MagicMock, patch
from handledbdata import find_image_file, get_employee_data


def test_get_employee_data(mocker):
    # Mock the sqlite3.connect method
    mock_conn = mocker.patch('sqlite3.connect', return_value=MagicMock())

    # Create a mock cursor
    mock_cursor = mock_conn.return_value.cursor.return_value

    # Set up the mock to return specific rows when fetchall is called
    mock_cursor.fetchall.return_value = [
        (1, 'John', 'Doe', 'john.doe@example.com', '1234567890', 1, 'HR', 'Company A', 1, 'file1.png', 'Description 1'),
        (2, 'Jane', 'Smith', 'jane.smith@example.com', '0987654321', 2, 'IT', 'Company B', 2, 'file2.png',
         'Description 2')
    ]

    # Call the function
    result = get_employee_data()

    # Expected result
    expected_result = [
        {
            "id": 1,
            "firstname": 'John',
            "lastname": 'Doe',
            "email": 'john.doe@example.com',
            "phone": '1234567890',
            "departmentId": 1,
            "departmentName": 'HR',
            "companyName": 'Company A',
            "file_id": 1,
            "filename": 'file1.png',
            "description": 'Description 1'
        },
        {
            "id": 2,
            "firstname": 'Jane',
            "lastname": 'Smith',
            "email": 'jane.smith@example.com',
            "phone": '0987654321',
            "departmentId": 2,
            "departmentName": 'IT',
            "companyName": 'Company B',
            "file_id": 2,
            "filename": 'file2.png',
            "description": 'Description 2'
        }
    ]

    # Assert that the result is as expected
    assert result == expected_result

    # Assert that the database connection and cursor were called correctly
    mock_conn.assert_called_once_with('custom_plugin.db')
    mock_cursor.execute.assert_called_once_with('''
        SELECT employee.id, firstname, lastname, email, phone, departmentId, departmentName, companyName, file_id, filename, description FROM employee
        INNER JOIN files ON employee.file_id = files.id
    ''')

    # Assert that the connection was closed
    mock_conn.return_value.close.assert_called_once()

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