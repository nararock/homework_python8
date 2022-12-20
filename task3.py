class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = float(input("Введите делимое "))
    b = float(input("Введите делитель "))
    if b == 0:
        raise MyZeroDivision("Вы ввели 0 в качестве делителя.")
except MyZeroDivision as err:
    print(err)
else:
    print(f"Частное равно {a / b}")
