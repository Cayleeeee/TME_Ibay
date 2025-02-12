def convert_date(date_str):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    
    try:
        mm, dd, yyyy = map(int, date_str.split("/"))
        if 1 <= mm <= 12 and 1 <= dd <= 31:
            return f"{months[mm-1]} {dd}, {yyyy}"
        else:
            return "Invalid date format."
    except ValueError:
        return "Invalid date format."

date_input = input("Enter the date (mm/dd/yyyy): ")
print("Date Output:", convert_date(date_input))
