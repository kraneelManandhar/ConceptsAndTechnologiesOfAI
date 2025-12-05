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

# # Task 5. Visualization - Study vs Sleep Pattern:
# # 1. Import matplotlib.pyplot as plt.
# import matplotlib.pyplot as plt
# # 2. Plot a scatter plot with:
# # • x-axis: Study hours
# study_hours = [item[0] for item in time_data]
# # print(study_hours)

# # • y-axis: Sleep hours
# sleep_hours = [item[2] for item in time_data]
# # print(sleep_hours)

# # plt.scatter(study_hours, sleep_hours, color='blue', marker='o')
# # plt.show()

# # 3. Add labels, title, and color.
# plt.scatter(study_hours, sleep_hours, color='blue', marker='o')
# plt.xlabel('Study Hours')
# plt.ylabel('Sleep Hours')
# plt.title('Study vs Sleep Pattern')
# plt.grid(True)

# plt.show()

# 8.1.1 Exercise - Recursion:
# Task 1 - Sum of Nested Lists:
# Scenario: You have a list that contains numbers and other lists of numbers (nested lists).
# You want to find the total sum of all the numbers in this structure.
# Task:
# • Write a recursive function sum_nested_list(nested_list) that:
# 1. Takes a nested list (a list that can contain numbers or other lists of numbers) as
# input.

lis2 = []
def nested_list(lis1):
    for x in lis1:
        if type(x) == list:
            nested_list(x)
        if type(x) != list:
            lis2.append(x)
    
# 2. Sums all numbers at every depth level of the list, regardless of how deeply nested
# the numbers are.
    sum = 0
    for x in lis2:
        sum += x
    return sum
# • Test the function with a sample nested list, such as
# nested_list = [1, [2, [3, 4], 5], 6, [7, 8]].
        
lis3 = [1,[2,[3,4],5],6,[7,8]]
print(nested_list(lis3))


# Task 2 - Generate All Permutations of a String:
# Scenario: Given a string, generate all possible permutations of its characters. This is useful
# for understanding backtracking and recursive depth-first search.
# Task:
# • Write a recursive function generate_permutations(s) that:
# – Takes a string s as input and returns a list of all unique permutations.
# • Test with strings like ”abc” and ”aab”.

# print(generate_permutations("abc"))
# # Should return [’abc’, ’acb’, ’bac’, ’bca’, ’cab’, ’cba’]

def generate_permutations(s):
    if len(s) == 1:
        return [s]

    permutations = []

    for i in range(len(s)):
        first_char = s[i]

        remaining = s[:i] + s[i+1:]

        for perm in generate_permutations(remaining):
            permutations.append(first_char + perm)

    return list(set(permutations))

print(generate_permutations("abc"))
print(generate_permutations("aab"))


# Task 3 - Directory Size Calculation:
# Directory Size Calculation Scenario: Imagine a file system where directories can contain files
# (with sizes in KB) and other directories. You want to calculate the total size of a directory,
# including all nested files and subdirectories.

# Sample directory structure.

# # Sample directory structure
# directory_structure = {
# "file1.txt": 200,
# "file2.txt": 300,
# "subdir1": {
# "file3.txt": 400,
# "file4.txt": 100
# },
# "subdir2": {
# "subsubdir1": {
# "file5.txt": 250
# },
# "file6.txt": 150
# }
# }


def calculate_directory_size(directory):
    total = 0

    for item in directory.values():
        if isinstance(item, dict):
            total += calculate_directory_size(item)
        else:
            total += item

    return total


#To test
directory_structure = {
    "file1.txt": 200,
    "file2.txt": 300,
    "subdir1": {
        "file3.txt": 400,
        "file4.txt": 100
    },
    "subdir2": {
        "subsubdir1": {
            "file5.txt": 250
        },
        "file6.txt": 150
    }
}

print(calculate_directory_size(directory_structure))

# 8.2.1 Exercises - Dynamic Programming:
# Task 1 - Coin Change Problem:
# Scenario: Given a set of coin denominations and a target amount, find the minimum number
# of coins needed to make the amount. If it’s not possible, return - 1.
# Task:
# 1. Write a function min_coins(coins, amount) that:
# • Uses DP to calculate the minimum number of coins needed to make up the
# amount.
# 2. Test with coins = [1, 2, 5] and amount = 11. The result should be 3 (using coins
# [5, 5, 1]).

# Sample Code - Coin Change Problem.

# def min_coins(coins, amount):
# """
# Finds the minimum number of coins needed to make up a given amount using dynamic
# programming.
# This function solves the coin change problem by determining the fewest number of
# coins from a given set of coin denominations that sum up to a target amount. The
# solution uses dynamic programming(tabulation) to iteratively build up the minimum
# number of coins required for each amount.
# Parameters:
# coins (list of int): A list of coin denominations available for making change. Each
# coin denomination is a positive integer.
# 8.2.1 Exercises - Dynamic Programming:
# Task 1 - Coin Change Problem:
# Scenario: Given a set of coin denominations and a target amount, find the minimum number
# of coins needed to make the amount. If it’s not possible, return - 1.
# Task:
# 1. Write a function min_coins(coins, amount) that:
# • Uses DP to calculate the minimum number of coins needed to make up the
# amount.
# 2. Test with coins = [1, 2, 5] and amount = 11. The result should be 3 (using coins
# [5, 5, 1]).

# Sample Code - Coin Change Problem.

# def min_coins(coins, amount):
# """
# Finds the minimum number of coins needed to make up a given amount using dynamic
# programming.
# This function solves the coin change problem by determining the fewest number of
# coins from a given set of coin denominations that sum up to a target amount. The
# solution uses dynamic programming(tabulation) to iteratively build up the minimum
# number of coins required for each amount.
# Parameters:
# coins (list of int): A list of coin denominations available for making change. Each
# coin denomination is a positive integer.


def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


coins = [1, 2, 5]
amount = 11
print(min_coins(coins, amount))

# Task 2 - Longest Common Subsequence (LCS):
# Scenario: Given two strings, find the length of their longest common subsequence (LCS).
# This is useful in text comparison.
# Task:
# 1. Write a function longest_common_subsequence(s1, s2) that:
# • Uses DP to find the length of the LCS of two strings s1 and s2.
# 2. Test with strings like "abcde" and "ace"; the LCS length should be 3 ("ace").

def longest_common_subsequence(s1, s2):
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

print(longest_common_subsequence("abcde", "ace"))

# Task 3 - 0/1 Knapsack Problem:
# Scenario: You have a list of items, each with a weight and a value. Given a weight capacity,
# maximize the total value of items you can carry without exceeding the weight capacity.
# Task:
# 1. Write a function knapsack(weights, values, capacity) that:
# • Uses DP to determine the maximum value that can be achieved within the given
# weight capacity.

# 2. Test with weights [1, 3, 4, 5], values [1, 4, 5, 7], and capacity 7. The re-
# sult should be 9.

def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]

                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
