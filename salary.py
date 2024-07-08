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

text = "Culmulative salary of the employe consists of several parts: 1000.01 as a main income, with added income 27.45 and 324.00 dollars"

total_income = sum_profit(text, generator_numbers)
print(f'Culmulative income: {total_income}')