import re

def generator_numbers(text: str):
  numbers = re.findall(r"\d+\.\d+", text)
  print(numbers)

  for number in numbers:
    yield float(number)

def sum_profit(text: str, func: callable) -> float:
  result = 0

  for number in func(text):
    print(number)
    result += number
  
  return result

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}$")