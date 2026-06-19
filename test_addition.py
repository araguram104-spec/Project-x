def add(a, b):
    """Function to add two numbers"""
    return a + b


# Test cases
test_cases = [
    {"input": (2, 3), "expected": 5},
    {"input": (10, 5), "expected": 15},
    {"input": (-1, 1), "expected": 0},
    {"input": (0, 0), "expected": 0},
]


def run_tests():
    print("Running Test Cases...\n")
    
    for i, test in enumerate(test_cases, start=1):
        a, b = test["input"]
        expected = test["expected"]
        result = add(a, b)

        if result == expected:
            print(f"✅ Test Case {i}: PASS")
        else:
            print(f"❌ Test Case {i}: FAIL")
            print(f"   Input: {a}, {b}")
            print(f"   Expected: {expected}, Got: {result}")


if __name__ == "__main__":
    run_tests()