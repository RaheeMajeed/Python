import streamlit as st

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    st.title("Prime Number Checker")

    # Input field for number
    number = st.number_input("Enter a number:", min_value=0, step=1)

    # Checking if the number is prime
    if number:
        if is_prime(int(number)):
            st.write(f"{number} is a prime number.")
        else:
            st.write(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
