# Challenge 2: QA Browser Test Results Analysis

# =============================================================================
# STEP 1: Store the browser data
# Chrome: 8 passed, 2 failed
# Firefox: 7 passed, 3 failed  
# Safari: 9 passed, 1 failed
# =============================================================================

# TODO: Create variables for Chrome
chrome_passed = 8
chrome_failed = 2
chrome_total = chrome_passed + chrome_failed

# TODO: Create variables for Firefox
firefox_passed = 7
firefox_failed = 3
firefox_total = firefox_passed + firefox_failed

# TODO: Create variables for Safari
safari_passed = 9
safari_failed = 1
safari_total = safari_passed + safari_failed

# =============================================================================
# STEP 2: Calculate success rates for each browser
# =============================================================================

# TODO: Calculate success rate for each browser (as percentage)
chrome_success_rate = chrome_passed/chrome_total * 100
firefox_success_rate = firefox_passed/firefox_total * 100
safari_success_rate = safari_passed/safari_total * 100

# =============================================================================
# STEP 3: Calculate overall statistics
# =============================================================================

# TODO: Calculate total tests across all browsers
total_tests = chrome_total + firefox_total + safari_total

# TODO: Calculate total passed tests across all browsers
total_passed = chrome_passed + firefox_passed + safari_passed

# TODO: Calculate overall success rate
overall_success_rate = (chrome_success_rate + firefox_success_rate + safari_success_rate) / 3

# =============================================================================
# STEP 4: Find best performing browser
# =============================================================================

# TODO: Determine which browser has the highest success rate
best_browser = "Safari"
best_rate = max([chrome_success_rate, firefox_success_rate, safari_success_rate])
# =============================================================================
# STEP 5: Print professional results
# =============================================================================

print("=== QA Browser Test Results ===")
# TODO: Print each browser's results
# Format: "Chrome: 8/10 passed (80.0% success rate)"
print(f"Chrome: {chrome_passed} passed ({chrome_success_rate} success rate) \n Firefox: {firefox_passed} passed ({firefox_success_rate} success rate) \n Safari: {safari_passed} passed ({safari_success_rate} success rate)")
print("\n=== Overall Summary ===")
print(f"Total tests executed: {total_tests} \n Total test passed: {total_passed} \n Overall sucess rate: {overall_success_rate} \n Best performing browser: {best_browser}({best_rate}%)")
# TODO: Print overall statistics
# Format: "Total tests executed: 30"
# Format: "Total tests passed: 24" 
# Format: "Overall success rate: 80.0%"
# Format: "Best performing browser: Safari (90.0%)"