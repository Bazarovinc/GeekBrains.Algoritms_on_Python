
x1, y1 = input("Введите координаты первой точки через пробел: ").split()
x2, y2 = input("Введите координаты второй точки через пробел: ").split()
x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
k = (y2 - y1) / (x2 - x1)
b = y1 - (x1 * k)
print(f"Уравнение имеет вид: y = {k}x + {b}")