faculty_list = ["John", "Alice", "Bob", "Eve"]
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
hours_list = ["8:00 AM", "10:00 AM", "1:00 PM", "3:00 PM"]
subjects_list = ["Math", "Science", "English", "History"]

print("-" * 50)
print(f"{'| Faculty':<10}{'| Days':<12}{'| Hours':<10}{'| Subjects':<15} |")
print("-" * 50)  
for faculty in faculty_list:
    for day in days_list:
        for hour in hours_list:
            for subject in subjects_list:
                print(f"{'| ' + faculty:<10}{'| ' + day:<12}{'| ' + hour:<10}{'| ' + subject:<15} |")
                print("-" * 50)  