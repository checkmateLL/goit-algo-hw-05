import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[str, None, None]:
    pattern = r'\d+\.*\d*'
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number

def sum_profit(text: str, func: Callable[[str], Generator[str, None, None]]) -> float:
    number_sum = 0
    for number in func(text):
        number_sum += float(number)
    return number_sum



# Example

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income}') # 1351.46