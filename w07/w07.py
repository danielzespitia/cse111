import csv

filename = 'time_log.csv'

with open(filename, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Print header
header = data[0]
header_str = f'{"Date":<12} {"Hours":<10} {"Description of Work"}'
print('=' * len(header_str))
print(header_str)
print('-' * len(header_str))

# Print content
for row in data[1:]:
    date, hours, description = row
    print(f'{date:<12} {hours:<10} {description}')

print('=' * len(header_str))

# Count functions
num_functions = len(data) - 1  # Subtract 1 to exclude the header row
num_functions_str = "four or more" if num_functions >= 4 else str(num_functions)
print(f"The program is divided into {num_functions_str} functions.")