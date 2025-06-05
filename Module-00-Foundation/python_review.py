# Challenge: Create variables for a QA test scenario
test_name = "Login Functionality Test"
test_cases_total = 15
test_cases_passed = 12
success_rate = test_cases_passed / test_cases_total

# Your task: Print a summary message
# Example: "Login Functionality Test: 12/15 passed (80.0% success rate)"
print(f"{test_name}: {test_cases_total}/{test_cases_passed} passed ({success_rate * 100}% success rate)")