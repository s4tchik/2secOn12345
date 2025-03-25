import random
import time

def generate_code():
    """Генерирует 5-значный код с ведущими нулями [[1]][[9]]"""
    return f"{random.randint(0, 99999):05d}"

def display_centered_code():
    """Выводит код по центру консоли (80 символов) [[1]]"""
    code = generate_code()
    border = "=" * 80
    # Вычисляем отступы для центрирования
    padding = (80 - len(code)) // 2
    print(f"\n{border}\n{' ' * padding}{code}{' ' * padding}\n{border}")

try:
    while True:
        display_centered_code()
        # Обновление каждые 10 секунд [[3]][[4]]
        time.sleep(2)
except KeyboardInterrupt:
    # Обработка прерывания через Ctrl+C [[3]]
    print("\nГенерация остановлена.")