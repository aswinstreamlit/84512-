import streamlit as st
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta  # Import for accurate month addition

# Add the heading at the top of the webpage with alignment adjustments
st.markdown("""
    <div style="display: flex; flex-direction: column; align-items: flex-start; margin-top: 10px;">
        <span style="font-size: 49.28px; font-weight: bold; text-align: left;"> 
        CORPORATE TAX 
        </span>
        REGISTRATION DEADLINE CALCULATOR
        </span>
    </div>
""", unsafe_allow_html=True)

# Custom CSS to add more space above the main heading, reduce header size, add borders, and make headings bold
st.markdown("""
    <style>
    h2 {
        font-size: 44.8px; /* Increased size by 60% from the original 28px */
        text-transform: uppercase; /* Make text uppercase */
        margin-top: 40px; /* Increase space above the heading by 2cm */
        text-align: left; /* Align the first line to the left */
        line-height: 1.2; /* Adjust line height */
        font-weight: bold; /* Make the main heading bold */
    }
    h2 span {
        display: block; /* Make the second line block-level */
        text-align: center; /* Center the second line */
    }
    h3 {
        font-size: 24px;
    }
    .box {
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        white-space: pre-wrap; /* Preserve new lines */
    }
    .smaller-heading {
        font-size: 20px;
        margin-top: 10px;
        margin-bottom: 10px;
        font-weight: bold;
        text-transform: uppercase; /* Make subheadings uppercase like main heading */
        text-align: left; /* Keep subheadings aligned to the left */
    }
    .input-container {
        width: 100%;
        display: inline-block;
    }
    
    /* Style the input fields to align */
    .stTextInput {
        width: 100% !important;
    }

    /* Style the button */
    div.stButton > button {
        background-color: #2B547E; /* Professional dark blue color */
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    div.stButton > button:hover {
        background-color: #3C6E9C; /* Slightly lighter blue when hovered */
    }

    .contact-text {
        font-size: 17px; /* Reduced size by 15% from a typical 20px size */
        margin-top: 20px;
        text-align: right; /* Align text to the right */
    }
    </style>
""", unsafe_allow_html=True)

# Create two columns
col1, col2 = st.columns(2)

# Date input widget in the first column with smaller heading
with col1:
    st.markdown('<div class="smaller-heading">Establishment Date</div>', unsafe_allow_html=True)
    date_input_str = st.text_input(
        "",
        placeholder="DD-MM-YYYY or DD/MM/YYYY",
        help="Enter the establishment date in the format DD-MM-YYYY or DD/MM/YYYY"
    )

    input_date = None
    # If a date is manually typed, try to parse it
    if date_input_str:
        # Replace slashes with dashes to normalize the date format
        date_input_str = date_input_str.replace("/", "-")
        try:
            # Parse the manually entered date in DD-MM-YYYY format
            input_date = datetime.strptime(date_input_str, "%d-%m-%Y").date()
        except ValueError:
            st.error("Please enter a valid date in DD-MM-YYYY or DD/MM/YYYY format.")

# Company name input moved to the right column
with col2:
    st.markdown('<div class="smaller-heading">Company Name</div>', unsafe_allow_html=True)
    company_name = st.text_input(
        "Enter the Company Name",
        help="Provide the registered name of the company"
    )

# Function to get deadline based on the month and day (ignoring the year)
def get_deadline_based_on_rules(input_date):
    month_day = (input_date.month, input_date.day)
    if (1, 1) <= month_day <= (2, 29):  # Jan 1 - Feb 29
        return "31 May 2024"
    elif (3, 1) <= month_day <= (4, 30):  # Mar 1 - Apr 30
        return "30 Jun 2024"
    elif (5, 1) <= month_day <= (5, 31):  # May 1 - May 31
        return "31 Jul 2024"
    elif (6, 1) <= month_day <= (6, 30):  # Jun 1 - Jun 30
        return "31 Aug 2024"
    elif (7, 1) <= month_day <= (7, 31):  # Jul 1 - Jul 31
        return "30 Sep 2024"
    elif (8, 1) <= month_day <= (9, 30):  # Aug 1 - Sep 30
        return "31 Oct 2024"
    elif (10, 1) <= month_day <= (11, 30):  # Oct 1 - Nov 30
        return "30 Nov 2024"
    elif (12, 1) <= month_day <= (12, 31):  # Dec 1 - Dec 31
        return "31 Dec 2024"
    return None

# Define the threshold date for the 90-day rule
threshold_date = datetime(2024, 3, 1).date()

# Display the deadline for corporate tax registration below
st.markdown('<div class="smaller-heading">Deadline For Corporate Tax Registration</div>', unsafe_allow_html=True)

# Check if the date input is provided
if date_input_str:
    if not company_name:
        st.error("Please enter the name of the company.")  # Error if company name is not provided
    else:
        try:
            # If input date is after March 1, 2024, apply the 3-month rule using relativedelta
            if input_date > threshold_date:
                calculated_date = input_date + relativedelta(months=3)
                st.markdown(f"<h3>{calculated_date.strftime('%B %d, %Y')}</h3>", unsafe_allow_html=True)
            else:
                # Apply the table rules based on the month and day (ignoring the year)
                deadline = get_deadline_based_on_rules(input_date)
                if deadline:
                    calculated_date = datetime.strptime(deadline, "%d %b %Y").date()
                    st.markdown(f"<h3>{deadline}</h3>", unsafe_allow_html=True)
                else:
                    st.write("The selected date does not fall within the specified ranges.")
            
            # Get the current date
            current_date = datetime.today().date()
            
            # Check if the calculated deadline is past the current date
            if calculated_date < current_date:
                # Inform the user that the registration is past due date
                st.markdown('<div class="box">The registration is past due date.</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="box">The registration is not past due date.</div>', unsafe_allow_html=True)
        
        except NameError:
            st.error("Please enter a valid date.")

# Email link for contact, aligned to the right
st.markdown("""
    <div class="contact-text" style="text-align: right;">
        Contact us via email: <a href="mailto:akhilesh@finitwell.com">akhilesh@finitwell.com</a>
    </div>
""", unsafe_allow_html=True)
