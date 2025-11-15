# 7.1 Warmup exercise

# Daily time (in hours): [study, entertainment, sleep]
time_data = [
(3.5, 2.0, 7.0), (5.0, 1.5, 6.5), (2.5, 3.0, 8.0),
(4.0, 2.0, 6.0), (1.5, 4.5, 9.0), (3.0, 2.5, 7.5),
(5.5, 1.0, 6.0), (2.0, 3.5, 8.5), (4.5, 2.0, 7.0),
(3.0, 3.0, 7.5), (6.0, 1.5, 6.0), (2.5, 4.0, 8.0),
(4.0, 2.5, 7.0), (5.0, 2.0, 6.5), (3.5, 2.5, 7.0)
]


# 1 Empty list 
low = []
moderate = []
high = []

# 2 for adding values in lists
for study, entertainment, sleep in time_data:
    if study < 3:
        low.append(study)
    elif 3 <= study <= 5:
        moderate.append(study)
    else:
        high.append(study)


# 3 Print result
print("Low Study Time: ", low)
print("Moderate Study Time: ", moderate)
print("High Study Time: ", high,'\n')


# Task 2. Based on Data – Answer all the Questions:
# 1. How many days had low study time?
# (a) Hint: Count the number of items in the low study list and print the result.
print(f"The days with low study time is: {len(low)}")

# 2. How many days had moderate study time?
print(f"The days with moderate study time is: {len(moderate)}")

# 3. How many days had high study time?
print(f"The days with high study time is: {len(high)}\n")


# Task 3. Convert Study Hours to Minutes:
# Convert each study hour value into minutes and store it in a new list called study_minutes.

# Formula: Minutes = Hours × 60

study_minutes = []

# 1. Iterate over the time_data list and apply the formula to the study hours.
for study, entertainment, sleep in time_data:
    study1 = study * 60
    entertainment1 = entertainment * 60
    sleep1 = sleep *60

# 2. Store the results in the new list.
    study_minutes.append((study1,entertainment1,sleep1))


# 3. Print the converted values.
print(study_minutes,'\n')


# Task 4. Analyze Average Time Use:
# Scenario: Each record contains daily hours of study, entertainment, and sleep.
# 1. Create empty lists for study_hours, entertainment_hours, and sleep_hours.
study_hours = []
entertainment_hours = []
sleep_hours = []

# 2. Iterate over time_data and extract values into each list.
for study,entertainment,sleep in time_data:
    study_hours.append(study)
    entertainment_hours.append(entertainment)
    sleep_hours.append(sleep)
# Checked if the values are entered in the list or not 
# print(study_hours)
# print(entertainment_hours)
# print(sleep_hours)

# 3. Calculate and print:
# (a) Average hours spent studying.
print(f"The average hours spent studying is {sum(study_hours) / len(study_hours)}")

# (b) Average hours spent on entertainment.
print(f"The average hours spent on entertainment is {sum(entertainment_hours) / len(entertainment_hours)}")

# (c) Average hours spent sleeping.
print(f"The average hours spent on sleeping is {sum(sleep_hours) / len(sleep_hours)} \n")

# Task 5. Visualization - Study vs Sleep Pattern:
# 1. Import matplotlib.pyplot as plt.
import matplotlib.pyplot as plt
# 2. Plot a scatter plot with:
# • x-axis: Study hours
study_hours = [item[0] for item in time_data]
# print(study_hours)

# • y-axis: Sleep hours
sleep_hours = [item[2] for item in time_data]
# print(sleep_hours)

# plt.scatter(study_hours, sleep_hours, color='blue', marker='o')
# plt.show()

# 3. Add labels, title, and color.
plt.scatter(study_hours, sleep_hours, color='blue', marker='o')
plt.xlabel('Study Hours')
plt.ylabel('Sleep Hours')
plt.title('Study vs Sleep Pattern')
plt.grid(True)

plt.show()
