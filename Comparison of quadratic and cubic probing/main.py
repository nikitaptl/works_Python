import random

GREEN = "\033[1;32m"
RESET = "\033[0m"

c1 = 1
c2 = 1
c3 = 1


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def quadratic_probe(self, initial, attempt):
        return int((initial + c1 * attempt + c2 * attempt ** 2) % self.size)

    def cubic_probe(self, initial, attempt):
        return (initial + c1 * attempt + c2 * attempt ** 2 + c3 * attempt ** 3) % self.size

    def insert(self, key, value, par=1):
        index_start = self.hash_function(key)
        index = index_start
        attempt = 0
        ch = 0

        while self.table[index] is not None:
            ch += 1
            if ch > self.size:
                raise ValueError("Произошло зацикливание. Вставить элемент невозможно")
            if (par == 1):
                index = self.quadratic_probe(index_start, attempt)
            else:
                index = self.cubic_probe(index_start, attempt)
            attempt += 1

        self.table[index] = (key, value)
        return attempt + 1


coeff = 1
cycleStep = 1

start = 500
end = 1000

print(f"\033[1;30;45mМакс. размер хэш-таблиц = {end}, коэф. заполнения = {coeff}\033[0m")

res_quadro = 0
attempts = 0
for M in range(start, end, cycleStep):
    hash_table_quadro = HashTable(M)
    res = 0

    # Здесь мы можем поменять значения параметров
    if (M > 0 and (M & (M - 1)) == 0):
        c1 = 0.5
        c2 = 0.5
    else:
        c1 = 1
        c2 = 1

    try:
        iterations = int(M * coeff)
        for i in range(iterations):
            el = random.randint(1, M * M)
            res += hash_table_quadro.insert(el, el)
        res_quadro += res / iterations
        attempts += 1

    except ValueError as e:
        continue

res_quadro = res_quadro / attempts
print(f"{GREEN}Квадратичное пробирование:{RESET}")
print(f"Среднее число проб = {res_quadro}")

###

res_cubic = 0
attempts = 0
for M in range(start, end, cycleStep):
    hash_table_cube = HashTable(M)
    res = 0

    c1 = 1
    c2 = 1
    c3 = 1

    try:
        iterations = int(M * coeff)
        for i in range(iterations):
            el = random.randint(1, M * M)
            res += hash_table_cube.insert(el, el, 2)
        res_cubic += res / iterations
        attempts += 1
    except ValueError as e:
        continue

res_cubic = res_cubic / attempts
print(f"{GREEN}Кубическое пробирование:{RESET}")
print(f"Среднее число проб = {res_cubic}")

if (res_quadro < res_cubic):
    print("Сегодня квадратичное пробирование оказалось круче")
else:
    print("Сегодня кубическое пробирование оказалось круче")
