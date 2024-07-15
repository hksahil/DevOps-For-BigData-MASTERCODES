## See in the container is the passwords.txt present or not using ls there

# app.py
from page1.page1 import page1_function
from page2.page2 import page2_function

def main():
    print(page1_function())
    print(page2_function())

if __name__ == "__main__":
    main()
