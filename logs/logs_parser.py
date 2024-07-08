import sys
from colorama import Fore
from pathlib import Path
from collections import Counter

# Gets path from user and optionally additional argument as in level of error
path = sys.argv[1]
log_level = sys.argv[2] if len(sys.argv) > 2 else None

# Parse lines from log into dictionary and apply keys to values
def parse_log_line(line: str) -> dict:
    # Splits line 3 times using spaces, handling text in 'message' as single dictionary value
    log_line = line.split(' ', maxsplit=3)
    return {
            'date': log_line[0],
            'time': log_line[1],
            'level': log_line[2],
            'message': log_line[3].strip()
        } 

# Loads log from file and creates list with log dictionaries
def load_logs(file_path: str) -> list:
    log_list = []
    try:        
        with open(file_path, 'r') as log_file:
            for line in log_file:
                #Parsing log file using function 'parse_log_line'
                logs = parse_log_line(line)
                log_list.append(logs)        
    # Handles possible exeptions
    except FileNotFoundError:
        print(f'Файл не знайдено')
    except Exception as e:
        print(f'Помилка виконання: {e}')
    return log_list

# When user enters 'level' this function filters log file by this level
def filter_logs_by_level(logs: list, level: str) -> list:
     return list(filter(lambda log: log['level'].lower() == level.lower(), logs))

# Counts number of each level in log file
def count_logs_by_level(logs: list) -> dict:
    counter = Counter(log['level'] for log in logs)
    return dict(counter)

# Outputs information about total number of error and their levels
def display_log_counts(counts: dict):
    # This print formats the output in the table-like view
    print(f"{'Рівень логування':<10} | {'Кількість':<5}")
    print('-' * 30)
    for level, count in counts.items():
        if level == 'INFO':
            color = Fore.GREEN
        elif level == 'ERROR':
            color = Fore.RED
        elif level == 'DEBUG':
            color = Fore.BLUE
        elif level == 'WARNING':
            color = Fore.YELLOW
        else:
            color = Fore.WHITE
        print(f'{color}{level:<10} | {count:<5}')

# Loads the logs
logs = load_logs(path)

# Displays count
counts = count_logs_by_level(logs)
display_log_counts(counts)


# If user added 'level', information about this level will be provided
if log_level:
    filtered_logs = filter_logs_by_level(logs, log_level)
    print(f"{Fore.WHITE}\nДеталі логів для рівня '{log_level}':")
    if filtered_logs:
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    else:
        print(f"No logs found for level: {log_level}")
else:
    # Display count
    counts = count_logs_by_level(logs)
    display_log_counts(counts)