import random

def create_data():
    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(3))
    data = f"tselykh21{random_digits}@test.ru"
    return data
