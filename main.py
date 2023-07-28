from Student import Student

student = Student("Иванов Иван Иванович", "items.csv")

student.add_score("Математика", 4, 85)
student.add_score("Математика", 5, 92)
student.add_score("Математика", 3, 78)

student.add_score("История", 5, 90)
student.add_score("История", 4, 85)
student.add_score("История", 4, 80)

student.add_score("Программирование", 2, 60)

print(student.print_average())
print(student.print_overall_average())
