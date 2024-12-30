import sqlite3


# Function to create the database and tables
def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('custom_plugin.db')
    cursor = conn.cursor()

    # Create the files table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT NOT NULL,
        description TEXT,
        file BLOB
    )
    ''')
    print("Table 'files' created successfully.")

    # Create the employee table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        departmentId INTEGER NOT NULL,
        departmentName TEXT NOT NULL,
        companyName TEXT NOT NULL,
        file_id INTEGER,
        FOREIGN KEY (file_id) REFERENCES files (id)
    )
    ''')
    print("Table 'employee' created successfully.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Function to populate the employee table
def populate_employee_table():
    employee_data = {
        "employees": [
            {"id": 1, "firstname": "Alice", "lastname": "Smith", "email": "alice@techcorp.com", "phone": "555-0246",
             "departmentId": 1,
             "departmentName": "Engineering", "companyName": "TechCorp"},
            {"id": 2, "firstname": "Bob", "lastname": "Brown", "email": "bob@techcorp.com", "phone": "555-1234",
             "departmentId": 1,
             "departmentName": "Engineering", "companyName": "TechCorp"},
            {"id": 3, "firstname": "Charlie", "lastname": "Davis", "email": "charlie@techcorp.com", "phone": "555-3781",
             "departmentId": 2,
             "departmentName": "Marketing", "companyName": "TechCorp"},
            {"id": 4, "firstname": "David", "lastname": "Wilson", "email": "david@techmicro.com", "phone": "555-0998",
             "departmentId": 3,
             "departmentName": "Sales", "companyName": "TechMicro"},
            {"id": 5, "firstname": "Mary", "lastname": "Johnson", "email": "mary@techmicro.com", "phone": "555-1165",
             "departmentId": 4,
             "departmentName": "HR", "companyName": "TechMicro"}
        ]
    }

    # Connect to SQLite database
    conn = sqlite3.connect('custom_plugin.db')
    cursor = conn.cursor()

    # Insert employee data into the table
    for emp in employee_data["employees"]:
        cursor.execute('''
        INSERT INTO employee (id, firstname, lastname, email, phone, departmentId, departmentName, companyName)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (emp["id"], emp["firstname"], emp["lastname"], emp["email"], emp["phone"], emp["departmentId"],
              emp["departmentName"], emp["companyName"]))

    print("Employee data inserted successfully.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Function to insert a file into the database
def insert_file(filename, description, filepath):
    # Connect to SQLite database
    conn = sqlite3.connect('custom_plugin.db')
    cursor = conn.cursor()

    # Read the file as binary data
    with open(filepath, 'rb') as file:
        file_data = file.read()

    # Insert the file into the table
    cursor.execute('''
        INSERT INTO files (filename, description, file)
        VALUES (?, ?, ?)
    ''', (filename, description, file_data))

    print(f"File '{filename}' inserted successfully.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()


# Function to populate the files table
def populate_files():
    # Example: Insert a file into the table
    insert_file('Dock.jpg', 'A dock over a lake at night.', 'static/images/Dock.jpg')
    insert_file('Fields.jpg', 'A road in the fields of flowers leading to the mountains.', 'static/images/Fields.jpg')
    insert_file('Waterfall.jpg', 'A Cascading Waterfall under pink trees.', 'static/images/Waterfall.jpg')
    insert_file('Lake.jpg', 'A a blue water lake.', 'static/images/Lake.jpg')


# Function to link an employee to a file
def link_employee_to_file(employee_id, file_id):
    # Connect to SQLite database
    conn = sqlite3.connect('custom_plugin.db')
    cursor = conn.cursor()

    # Update the employee table with the file_id
    cursor.execute('''
    UPDATE employee SET file_id = ? WHERE id = ?
    ''', (file_id, employee_id))

    print(f"Employee with ID {employee_id} linked to file ID {file_id}.")

    # Commit changes and close the connection
    conn.commit()
    conn.close()
