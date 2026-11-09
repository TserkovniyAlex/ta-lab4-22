import math

# Розміри хеш-таблиць
M_DIV = 13
M_MUL = 16

# Константа для методу множення
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


def build_open_hash_table(words, m, hash_function):
    """Побудова відкритої хеш-таблиці методом роздільних ланцюжків."""
    # Ініціалізація порожніх ланцюжків
    hash_table = [[] for _ in range(m)]
    for word in words:
        key = calculate_key(word)
        address = hash_function(key)
        # У таблиці зберігаються лише унікальні слова:
        # порівнюються самі слова, а не числові ключі K
        if word in hash_table[address]:
            print(f"Слово {word} вже є в комірці {address} - пропущено")
            continue
        # Додавання слова в кінець ланцюжка
        hash_table[address].append(word)
    return hash_table


def display_hash_table(table, method):
    """Виведення хеш-таблиці."""
    print(f"\n--- {method} ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")


# Побудова таблиці методом ділення
table_div = build_open_hash_table(WORDS, M_DIV, division_hash)
display_hash_table(table_div, "Метод ділення (M=13)")

# Побудова таблиці методом множення
table_mul = build_open_hash_table(WORDS, M_MUL, multiplication_hash)
display_hash_table(table_mul, "Метод множення (M=16)")
