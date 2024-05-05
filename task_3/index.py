import sys
import os
from tabulate import tabulate

def main():
  arguments = sys.argv[1:]
  length = len(arguments)

  if (length == 0):
    print("Usage: 'python index.py <file_path>' or 'python index.py <file_path> <level>'")
    sys.exit(0)

  file_path = arguments[0]

  logs = load_logs(file_path)

  count = count_logs_by_level(logs)

  print(tabulate(count, headers='keys', tablefmt="grid"))

  if length == 2:
    level = arguments[1]
    filtered_logs = filter_logs_by_level(logs, level)
    print(f"\nДеталі логів для рівня '{level}':\n")
    for log in filtered_logs:
      print(log)


def load_logs(file_path: str) -> None:
  if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

  logs = []

  with open(file_path, 'r') as file:
    for line in file:
      str_item = line.rstrip("\n")
      logs.append(parse_log_line(str_item))

  return logs


def parse_log_line(line: str):
  date, time, level, *message = line.split(' ')
  return {
    "date": date,
    "time": time,
    "level": level,
    "message": " ".join(message)
  }

def count_logs_by_level(logs: list) -> dict:
  counts = {}

  for log in logs:
    level = log['level']

    if level in counts:
      counts[level] += 1
    else:
      counts[level] = 1
  
  result = []

  for key, value in counts.items():
    result.append({
      "Level": key,
      "Count": value
    })
  
  return result


def filter_logs_by_level(logs: list, level: str) -> list:
  level = level.upper()

  filtered_logs = []

  for log in logs:
    if log['level'] == level:
      filtered_logs.append(f"{log['date']} {log['time']} - {log['message']}")
  
  return filtered_logs

def display_log_counts(counts: dict):
  pass;

main()

# /Users/alexnosov/Projects/python_lessons/goit-pycore-hw-05/task_3/log.csv
