# Enhanced Python File for Additional Guest Information Input
import streamlit as st
def collect_billing_info():
    """
    Captures expenses like meals, spa treatments, minibar usage, and stores them for bill generation.

    Returns:
        tuple: Contains individual expenses for meals, spa treatments, minibar usage, and the total expense.
    """
    # Display a subheader to introduce the basic billing information section
    st.subheader("Basic Billing Information")
    
    # Input field for meals expense
    # Allows the guest to enter their expense for meals
    meals_expense = st.number_input("Meals Expense ($)", min_value=0.0, step=0.01)
    
    # Input field for spa treatments expense
    # Allows the guest to enter their expense for spa treatments
    spa_expense = st.number_input("Spa Treatments Expense ($)", min_value=0.0, step=0.01)
    
    # Input field for minibar usage expense
    # Allows the guest to enter their expense for minibar usage
    minibar_expense = st.number_input("Minibar Usage Expense ($)", min_value=0.0, step=0.01)

    # Calculate the total expenses
    total_expense = meals_expense + spa_expense + minibar_expense
    
    # Display the total expense to the user
    st.write(f"Total Expenses: ${total_expense}")

    # Return the collected billing information as a tuple
    return meals_expense, spa_expense, minibar_expense, total_expense

if __name__ == "__main__":
    # Run the functions to collect guest information

    meals, spa, minibar, total = collect_billing_info()

    st.write("### Billing Information")
    st.write(f"- Meals Expense: ${meals}")
    st.write(f"- Spa Treatments Expense: ${spa}")
    st.write(f"- Minibar Usage Expense: ${minibar}")
    st.write(f"- Total Expense: ${total}")
