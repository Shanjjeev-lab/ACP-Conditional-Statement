
def calculate_attendance(total_days, absent_days):
    present_days = total_days - absent_days
    attendance_percentage = (present_days / total_days) * 100
    return attendance_percentage

present = int(input("Enter a number: "))
absent = int(input("Enter a number: "))

attendance_percentage = calculate_attendance(present, absent)

print(f"Your attendance percentage is: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("You Are: Eligible")
else:
    print("You Are: Not Eligible")
