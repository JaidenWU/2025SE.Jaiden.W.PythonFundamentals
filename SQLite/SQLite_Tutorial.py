import sqlite3
from employee import Employee

con = sqlite3.connect(":memory:")  # creates a database connection object

cur = con.cursor()

cur.execute(
    """CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )"""
)


def insert_emp(emp):
    with con:
        cur.execute(
            "INSERT INTO employees VALUES (:first,:last,:pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_name(lastname):
    cur.execute("SELECT * FROM employees WHERE last=:last", {"last": lastname})
    return cur.fetchall()


def update_pay(emp, pay):
    with con:
        cur.execute(
            """UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with con:
        cur.execute(
            "DELETE from employees WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


emp_1 = Employee("John", "Doe", 80000)
emp_2 = Employee("Jane", "Doe", 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name("Doe")
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name("Doe")
print(emps)

con.close()
