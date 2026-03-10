salary = int(input("Enter the salary amount  : "))
late_Days = int(input("Enter late days : "))
absent_days = int(input("Enter absent days : "))

deduction = 0

if late_Days > 10:
    deduction += 0.10
elif late_Days > 5:
    deduction += 0.05


if absent_days > 2:
    deduction += 0.05

final_salary = salary - (salary * deduction)

print("Final Salary : ", int(final_salary))