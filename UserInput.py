import streamlit as st

def main():
    st.title("Name and Age Printer")

    # Input fields for name and age
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, step=1)

    # Displaying the message
    if name and age:
        st.write(f"Your name is {name} and your age is {age}.")

if __name__ == "__main__":
    main()

