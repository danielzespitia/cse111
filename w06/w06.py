import csv
from datetime import datetime
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Entry, messagebox

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to calculate recommended daily calorie intake
def calculate_calorie_intake(age, gender, weight, height, activity_level):
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        messagebox.showerror("Error", "Invalid gender")
        return

    if activity_level == "sedentary":
        calorie_intake = bmr * 1.2
    elif activity_level == "lightly active":
        calorie_intake = bmr * 1.375
    elif activity_level == "moderately active":
        calorie_intake = bmr * 1.55
    elif activity_level == "very active":
        calorie_intake = bmr * 1.725
    else:
        messagebox.showerror("Error", "Invalid activity level")
        return

    return calorie_intake

# Function to record a workout
def record_workout(workout_type, duration):
    workout_log = []
    with open("workout_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), workout_type, duration])
        workout_log.append([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), workout_type, duration])
    return workout_log

# Function to save fitness data to a CSV file
def save_data_to_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Function to track and display fitness progress
def track_progress():
    bmi = calculate_bmi(weight, height)
    calorie_intake = calculate_calorie_intake(age, gender, weight, height, activity_level)
    workout_log = []
    with open("workout_log.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            workout_log.append(row)

    # Progress tracking and display logic here
    pass

# Test function for calculate_bmi()
def test_calculate_bmi():
    weight = 70
    height = 1.75
    expected_bmi = 22.86
    assert calculate_bmi(weight, height) == expected_bmi

# Test function for calculate_calorie_intake()
def test_calculate_calorie_intake():
    # Test cases and assertions here
    pass

# Test function for record_workout()
def test_record_workout():
    # Test cases and assertions here
    pass

# Test function for save_data_to_csv()
def test_save_data_to_csv():
    # Test cases and assertions here
    pass

# Test function for track_progress()
def test_track_progress():
    # Test cases and assertions here
    pass

# Execute the test functions using pytest
def run_tests():
    test_calculate_bmi()
    test_calculate_calorie_intake()
    test_record_workout()
    test_save_data_to_csv()
    test_track_progress()

# GUI code using tkinter
def create_gui():
    def calculate_bmi_button_clicked():
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = calculate_bmi(weight, height)
        messagebox.showinfo("BMI", f"Your BMI is: {bmi:.2f}")

    def calculate_calorie_intake_button_clicked():
        age = int(age_entry.get())
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        gender = gender_entry.get()
        activity_level = activity_level_entry.get()
        calorie_intake = calculate_calorie_intake(age, gender, weight, height, activity_level)
        messagebox.showinfo("Calorie Intake", f"Your recommended daily calorie intake is: {calorie_intake:.2f} calories")

    def record_workout_button_clicked():
        workout_type = workout_type_entry.get()
        duration = float(duration_entry.get())
        workout_log = record_workout(workout_type, duration)
        messagebox.showinfo("Workout Recorded", "Your workout has been recorded.")

    def track_progress_button_clicked():
        track_progress()

    root = Tk()
    root.title("Fitness Tracker")

    # BMI Calculator
    bmi_label = Label(root, text="BMI Calculator")
    weight_label = Label(root, text="Weight (in kg):")
    weight_entry = Entry(root)
    height_label = Label(root, text="Height (in meters):")
    height_entry = Entry(root)
    calculate_bmi_button = Button(root, text="Calculate BMI", command=calculate_bmi_button_clicked)

    bmi_label.pack()
    weight_label.pack()
    weight_entry.pack()
    height_label.pack()
    height_entry.pack()
    calculate_bmi_button.pack()

    # Calorie Intake Calculator
    calorie_intake_label = Label(root, text="Calorie Intake Calculator")
    age_label = Label(root, text="Age:")
    age_entry = Entry(root)
    gender_label = Label(root, text="Gender:")
    gender_entry = Entry(root)
    weight_label2 = Label(root, text="Weight (in kg):")
    weight_entry2 = Entry(root)
    height_label2 = Label(root, text="Height (in meters):")
    height_entry2 = Entry(root)
    activity_level_label = Label(root, text="Activity Level:")
    activity_level_entry = Entry(root)
    calculate_calorie_intake_button = Button(root, text="Calculate Calorie Intake", command=calculate_calorie_intake_button_clicked)

    calorie_intake_label.pack()
    age_label.pack()
    age_entry.pack()
    gender_label.pack()
    gender_entry.pack()
    weight_label2.pack()
    weight_entry2.pack()
    height_label2.pack()
    height_entry2.pack()
    activity_level_label.pack()
    activity_level_entry.pack()
    calculate_calorie_intake_button.pack()

    # Workout Tracker
    workout_label = Label(root, text="Workout Tracker")
    workout_type_label = Label(root, text="Workout Type:")
    workout_type_entry = Entry(root)
    duration_label = Label(root, text="Duration (in minutes):")
    duration_entry = Entry(root)
    record_workout_button = Button(root, text="Record Workout", command=record_workout_button_clicked)

    workout_label.pack()
    workout_type_label.pack()
    workout_type_entry.pack()
    duration_label.pack()
    duration_entry.pack()
    record_workout_button.pack()

    # Progress Tracker
    track_progress_button = Button(root, text="Track Progress", command=track_progress_button_clicked)
    track_progress_button.pack()

    root.mainloop()

# Main function to run the program
def main():
    run_tests()
    create_gui()

# Execute the main function
if __name__ == '__main__':
    main()