# --- Dummy setup (can be ignored) --


# Assume we have a meaningfull Employee class
# This is just a minimal dummy for demonstration
class Employee:
    HOURLY_FLAG = 'hourly'

    def __init__(self, flags: list, age: int):
        self.flags = flags
        self.age = age

    def is_eligible_for_full_benefit(self):
        return Employee.HOURLY_FLAG in self.flags and self.age > 65


# Create instance for demonstration
employee = Employee([Employee.HOURLY_FLAG], 18)

# --- Superfluous comment: --
# Check to see if the employee is eligible for full benefits
if Employee.HOURLY_FLAG in employee.flags and employee.age > 65:
    pass

# --- Comment replaced by method name: --
if employee.is_eligible_for_full_benefit():
    pass
