import time
def main():
    fib_n = int
    fib_base = Fib_base()
    fib_memery = Fib_memery()
    fib_lin = Fib_lin()
    fib_bine = Fib_bine()
    fib_matrix = Fib_matrix()
    while fib_n != 0:
        print("Введите порядковый номер числа фибоначчи(для выхода 0):")
        fib_n = int(input())
        fib_base.test_fib(fib_n)
        fib_memery.test_fib(fib_n)
        fib_lin.test_fib(fib_n)
        fib_bine.test_fib(fib_n)
        fib_matrix.test_fib(fib_n)

class Fib:
    name = ""
    compl = ""

    def get_fib_result(self, n):
        pass

    def test_fib(self, n):
        fib_time = time.time()
        fib_result = self.get_fib_result(n)
        fib_time = time.time() - fib_time
        print(self.name+" сложность: "+self.compl+"\nПорядковый номер:" + str(
            fib_result) + " Затрачено время:" + str(fib_time)+"\n")

class Fib_base(Fib):
    name = "Стандартная рекурсивная формула фибоначи."
    compl = "O(2^n)"

    def get_fib_result(self, n):
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            return self.get_fib_result(n - 1) + self.get_fib_result(n - 2) # Вызываем функцию для предидущих значений

class Fib_memery(Fib):
    memory = {0: 0, 1: 1, 2: 1}
    name = "Рекурсивная формула фибоначи с запоминанием."
    compl = "O(n)"

    def get_fib_result(self, n):
        if n in self.memory:
            return self.memory[n] # Берем из пямяти если уже посчитано
        else:
            self.memory[n] = self.get_fib_result(n - 1) + self.get_fib_result(n - 2) # Сохраняем новое значение
        return self.memory[n]

class Fib_lin(Fib):
    name = "Линейная формула фибоначи." # Храним только 2 последних значения
    compl = "O(n)"

    def get_fib_result(self, n):
        curr = 0
        next = 1
        for __ in range(n):
            curr, next = next, curr + next
        return curr

class Fib_bine(Fib):
    name = "Фибоначчи по Формуле Бине."
    gold = (1 + 5 ** 0.5) / 2 # Золотое сечение
    compl = "O(1)"

    def get_fib_result(self, n):
        return int((self.gold ** n - (1 - self.gold)**n) / (5 ** 0.5))


class Fib_matrix(Fib):
    name = "Матричная формула фибоначи."
    M = [[1, 1], [1, 0]]
    compl = "O(Log(n))"

    def get_fib_result(self, n):
        F = [[1, 1],
             [1, 0]]
        if n == 0:
            return 0
        for i in range(2, n):
            self.multiply(F)
        return F[0][0]

    def multiply(self, F): # Перемножение матриц
        x = (F[0][0] * self.M[0][0] + F[0][1] * self.M[1][0])
        y = (F[0][0] * self.M[0][1] + F[0][1] * self.M[1][1])
        z = (F[1][0] * self.M[0][0] + F[1][1] * self.M[1][0])
        w = (F[1][0] * self.M[0][1] + F[1][1] * self.M[1][1])
        F[0][0] = x
        F[0][1] = y
        F[1][0] = z
        F[1][1] = w

if __name__ == '__main__':
    main()
