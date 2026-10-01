# Geometric Lib

## Общее описание решения

Библиотека `geometric_lib` - набор функций для вычисления площадей и периметров стандартных фигур. Реализованы функции для фигур: круг, прямоугольник, квадрат, треугольник

## Структура библиотеки:

```text
`geometric_lib`  
    ├── `circle.py`  
    ├── `rectangle.py`  
    ├── `square.py`  
    ├── `triangle.py`  
    └── `docs`  
         ├── `README.md`  
         └── `CHANGELOG.md`  
```

## Формулы для вычисления:

### Area
```
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = a * h / 2
```

### Perimeter
```
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c
```

## Описание файлов:

### circle.py

- `area(r)` — Вычисляет площадь круга по заданному радиусу r
- `perimeter(r)` - Вычисляет периметр круга по заданному радиусу r

Примеры вызова:
```python
print(area(3)) # 28.274333882308138
print(perimeter(3)) # 18.84955592153876
```

### rectangle.py

- `area(a, b)` — Вычисляет площадь прямоугольника по заданным сторонам a и b
- `perimeter(a, b)` - Вычисляет периметр прямоугольника по заданным сторонам a и b

Примеры вызова:
```python
print(area(3, 4)) # 12
print(perimeter(3, 4)) # 14
```

### square.py

- `area(a)` — Вычисляет площадь квадрата по заданной стороне a
- `perimeter(a)` - Вычисляет периметр квадрата по заданной стороне a

Примеры вызова:
```python
print(area(3)) # 9
print(perimeter(3)) # 12
```

### triangle.py

- `area(a, h)` — Вычисляет площадь треугольника по заданной стороне a и высоте h
- `perimeter(a, b, c)` - Вычисляет периметр треугольника по заданным сторонам a, b и c

Примеры вызова:
```python
print(area(3, 4)) # 6
print(perimeter(3, 4, 5)) # 12
```