import sqlite3


db_name = "custom_plugin.db"

def get_employee_data():
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Query the table for employee data
    cursor.execute(
        """
        SELECT employee.id, firstname, lastname, email, phone, departmentId, departmentName, companyName, file_id, filename, description FROM employee
        INNER JOIN files ON employee.file_id = files.id
    """
    )

    # Fetch the employee data
    rows = cursor.fetchall()

    # Convert to a list of dictionaries
    employee_data = [
        {
            "id": row[0],
            "firstname": row[1],
            "lastname": row[2],
            "email": row[3],
            "phone": row[4],
            "departmentId": row[5],
            "departmentName": row[6],
            "companyName": row[7],
            "file_id": row[8],
            "filename": row[9],
            "description": row[10],
        }
        for row in rows
    ]

    # Close the connection
    conn.close()

    return employee_data


# Function to find an image file by filename
def find_image_file(file_id):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Query the table for the file
    cursor.execute(
        """
        SELECT file FROM files WHERE id = ?
    """,
        (file_id,),
    )

    # Fetch the file data
    file_data = cursor.fetchone()

    # Close the connection
    conn.close()

    return file_data
