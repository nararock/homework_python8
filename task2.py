class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        print(f"Сумма клеток равна {self.quantity + other.quantity}")
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            print(f"Разность клеток равна {self.quantity - other.quantity}")
            return Cell(self.quantity - other.quantity)
        else:
            print("Разность количества ячеек двух клеток меньше нуля!")

    def __mul__(self, other):
        print(f"Произведение клеток равно {self.quantity * other.quantity}")
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        print(f"Частное клеток равно {self.quantity // other.quantity}")
        return Cell(self.quantity // other.quantity)

    def make_order(self, cells):
        cell_str = ''
        for i in range(self.quantity // cells):
            for j in range(cells):
                cell_str += '* '
            cell_str += '\n'
        for k in range(self.quantity % cells):
            cell_str += '* '
        return cell_str


cell1 = Cell(30)
cell2 = Cell(25)

cell3 = Cell(10)
cell4 = Cell(15)

print("Складываем")
new_cell1 = cell1 + cell2

print()

print("Вычитаем")
new_cell2 = cell2 - cell1
new_cell3 = cell4 - cell3

print()

print("Умножаем")
new_cell4 = cell2 * cell1

print()

print("Делим")
new_cell5 = cell1 / cell2

print("Организация ячеек по рядам")
print(cell1.make_order(5))
print(cell2.make_order(10))
