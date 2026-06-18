from app import check_website_status

def test_status():
    assert check_website_status() == 200
    print("Dependency test passed successfully!")

if __name__ == "__main__":
    test_status()
