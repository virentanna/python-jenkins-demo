from app import add_numbers

def test_addition():
    # This checks if our function works correctly
    assert add_numbers(5, 5) == 10
    print("Test passed successfully!")

if __name__ == "__main__":
    test_addition()
