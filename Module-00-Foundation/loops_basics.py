# Challenge 3A: Loop through test cases (BEGINNER LEVEL)

test_cases = ["Login Test", "Registration Test", "Checkout Test"]

# YOUR TASK: 
# 1. Loop through each test case
# 2. Print "Executing: [test name]"
# 3. Count how many tests you executed

executed_count = 0
for test_case in test_cases:
    # YOUR CODE HERE - fill in these two lines:
    print(f"Executing: {test_case}")
    executed_count += 1
    # Print the execution message
    # Increment the counter
print(f"Total tests executed: {executed_count}")

# Challenge 3B: Nested Loops - Browser Test Matrix (INTERMEDIATE)

browsers = ["Chrome", "Firefox", "Safari"]
test_types = ["Login", "Registration", "Checkout"]

# YOUR TASK:
# 1. Run EACH test type on EACH browser (nested loops!)
# 2. Print: "Running [test_type] test on [browser]"
# 3. Count total combinations executed
# 4. Print which browser-test combination you're currently on (like "Test 1 of 9")

total_combinations = 0
test_number = 0
total_expected = len(browsers) * len(test_types)

for test in test_types:
    for br in browsers:
        print(f"Running {test} test on {br}")
        test_number += 1
        total_combinations += 1
        print(f"test number: {test_number} of {total_expected}")
# YOUR CODE HERE - figure out the nested loop structure
# Hint: You need a loop inside another loop!
# Hint: Think about how many total combinations there should be

print(f"Completed {total_combinations} test combinations")