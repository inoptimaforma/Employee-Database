class EmployeeDAO:
    def __init__(self, db_name='employee_db.sqlite'):
        self.db_name = db_name
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._get_connection() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS employee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    position TEXT,
                    salary REAL,
                    hire_date TEXT
                )
            ''')
            conn.commit()

    def insert(self, employee):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO employee (name, position, salary, hire_date)
                VALUES (?, ?, ?, ?)
            ''', (employee.name, employee.position, employee.salary, employee.hire_date))
            employee.id = cursor.lastrowid
            conn.commit()
        return employee

    def get_by_id(self, id):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))
            row = cursor.fetchone()
            if row:
                return Employee(*row)
            return None

    def get_all(self):
        employees = []
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employee ORDER BY id')
            for row in cursor.fetchall():
                employees.append(Employee(*row))
        return employees

    def update(self, employee):
        with self._get_connection() as conn:
            conn.execute('''
                UPDATE employee 
                SET name = ?, position = ?, salary = ?, hire_date = ?
                WHERE id = ?
            ''', (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
            conn.commit()
        return employee

    def delete(self, id):
        with self._get_connection() as conn:
            conn.execute('DELETE FROM employee WHERE id = ?', (id,))
            conn.commit()
