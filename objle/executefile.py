from objle.student import Student
lisa =Student('Lisa',59,12)
richard = Student('Richard',85,13)

lisa.print_score()
richard.print_score()
print(lisa.get_grade())
print(lisa.get_age())
lisa.__age=15

print(lisa.get_age())
