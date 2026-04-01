import streamlit as st

# Create Streamlit app for division
st.title("Division Calculator")
st.write("Enter two numbers to divide")

# Create input fields
col1, col2 = st.columns(2)

with col1:
    num1 = st.text_input("First Number", value="0")
with col2:
    num2 = st.text_input("Second Number", value="0")

# Calculate button
if st.button("Calculate"):
    try:
        # Convert inputs to float
        number1 = float(num1)
        number2 = float(num2)
        
        # Perform division
        result = number1 / number2
        
        # Display success message
        st.success(f"✅ Result: {number1} ÷ {number2} = {result}")
        
    except ValueError:
        # Handle non-numeric input
        st.error("❌ Invalid input! Please enter numeric values only.")
        
    except ZeroDivisionError:
        # Handle division by zero
        st.error("❌ Error: Cannot divide by zero! Please enter a non-zero second number.")

# Add helpful information
with st.sidebar:
    st.header("How to use")
    st.write("1. Enter two numbers")
    st.write("2. Click 'Calculate Division'")
    st.write("3. See the result or error message")
    
    st.header("Example")
    st.write("First: 10")
    st.write("Second: 2")
    st.write("Result: 5.0")