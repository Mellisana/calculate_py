# Ввод длины стороны квадрата
side_length = float(input("Введите длину стороны квадрата: "))

# Вычисление периметра и площади квадрата
square_perimeter = 4 * side_length
square_area = side_length ** 2

# Вывод результатов для квадрата
print("Периметр квадрата:", square_perimeter)
print("Площадь квадрата:", square_area)

# Ввод длины и ширины прямоугольника
rect_length = float(input("Введите длину прямоугольника: "))
rect_width = float(input("Введите ширину прямоугольника: "))

# Вычисление периметра и площади прямоугольника
rect_perimeter = 2 * (rect_length + rect_width)
rect_area = rect_length * rect_width

# Вывод результатов для прямоугольника
print("Периметр прямоугольника:", rect_perimeter)
print("Площадь прямоугольника:", rect_area)