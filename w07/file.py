import csv

data = [
    ['2024-04-04', '6', 'Writing the program'],
    ['2024-04-04', '2', 'Testing and troubleshooting'],
    ['2024-04-04', '6', 'Writing code for error modifications'],
    ['2024-04-04', '1', 'Testing']
]

filename = 'time_log.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Time Spent (hours)', 'Description of Work'])
    writer.writerows(data)

print(f'File {filename} generated successfully.')