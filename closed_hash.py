import math

# Розміри хеш-таблиць
M_DIV = 13
M_MUL = 16

# Константа методу множення
A = 0.6180339887

# Послідовність слів варіанта №22
WORDS = [
    "ЯК", "ДБАЄШ", "ТАК", "І", "МАЄШ", "ХТО",
    "ЗЕМЛЮ", "РОБИТЬ", "ТОЙ", "ХЛІБ", "ДОБРИЙ", "РОБИТЬ"
]

# Український алфавіт
ALPHABET = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"

# Словник порядкових номерів літер
LETTER_POSITIONS = {char: i + 1 for i, char in enumerate(ALPHABET)}


def calculate_key(word):
    """Обчислення числового ключа: K = сума порядкових номерів літер."""
    key = 0
    for char in word.upper():
        key += LETTER_POSITIONS.get(char, 0)
    return key


def division_hash(key):
    """Метод ділення: h(K) = K mod 13."""
    return key % M_DIV


def multiplication_hash(key):
    """Метод множення: h(K) = floor(16 * (KA mod 1))."""
    fractional_part = (key * A) % 1
    return math.floor(M_MUL * fractional_part)


def build_closed_hash_table(words, m, hash_function):
    """Побудова закритої хеш-таблиці з лінійним пробуванням."""
    # Ініціалізація порожніх комірок
    hash_table = [None] * m
    for word in words:
        key = calculate_key(word)
        start_address = hash_function(key)
        probes = []
        # Лінійне пробування: h(K, i) = (h(K) + i) mod m
        for i in range(m):
            address = (start_address + i) % m
            probes.append(address)
            if hash_table[address] == word:
                # Слово вже є в таблиці - повторно не вставляємо
                print(f"{word}: {probes} - вже є в комірці {address}")
                break
            if hash_table[address] is None:
                hash_table[address] = word
                print(f"{word}: {probes} -> комірка {address}")
                break
        else:
            print(f"Помилка: таблиця заповнена. Не вдалося додати: {word}")
    return hash_table


def display_hash_table(table, method):
    """Виведення закритої хеш-таблиці."""
    print(f"\n--- {method} ---")
    print("Індекс | Слово")
    print("-------|----------------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d}     | {value}")


# Побудова таблиці методом ділення
print("Хід вставлення (метод ділення):")
table_div = build_closed_hash_table(WORDS, M_DIV, division_hash)
display_hash_table(table_div, "Метод ділення (M=13)")

# Побудова таблиці методом множення
print("\nХід вставлення (метод множення):")
table_mul = build_closed_hash_table(WORDS, M_MUL, multiplication_hash)
display_hash_table(table_mul, "Метод множення (M=16)")
