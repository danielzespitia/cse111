import datetime
import csv
from tkinter import Tk, Label, Button

# Function to calculate Body Mass Index (BMI)
def calculate_bmi(weight, height):
    # BMI calculation
    bmi = weight / (height ** 2)
    return bmi

# Function to record a workout in the fitness log
def record_workout(workout_type, duration):
    # Current date and time
    now = datetime.datetime.now()
    workout_entry = [now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), workout_type, duration]

    # Save the entry to the CSV file
    with open('fitness_log.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(workout_entry)

# Function to display fitness progress
def track_progress():
    # Load data from the CSV file
    with open('fitness_log.csv', 'r') as file:
        reader = csv.reader(file)
        workout_entries = list(reader)

    # Calculate BMI
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight, height)

    # Display progress
    print("=== Fitness Progress ===")
    print("BMI: {:.2f}".format(bmi))
    print("Workout History:")
    for entry in workout_entries:
        print("Date: {}, Time: {}, Workout Type: {}, Duration: {} minutes".format(entry[0], entry[1], entry[2], entry[3]))

# Function to save fitness data to a CSV file
def save_data_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Function to test BMI calculation
def test_calculate_bmi():
    weight = 70.0
    height = 1.75
    bmi = calculate_bmi(weight, height)
    print("BMI: {:.2f}".format(bmi))

# Function to test workout recording
def test_record_workout():
    workout_type = "Running"
    duration = 30
    record_workout(workout_type, duration)
    print("Workout recorded.")

# Function to test progress tracking
def test_track_progress():
    track_progress()

# Run the tests
test_calculate_bmi()
test_record_workout()
test_track_progress()