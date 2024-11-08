# Date input widget in the first column with smaller heading
with col1:
    st.markdown('<div class="smaller-heading">Establishment Date</div>', unsafe_allow_html=True)
    date_input_str = st.text_input(
        "",
        placeholder="DD-MM-YYYY or DD/MM/YYYY",
        help="Enter the establishment date in the format DD-MM-YYYY or DD/MM/YYYY"
    )
    # Additional text added below the date input heading
    st.markdown('<div style="font-size: 16px; margin-top: -10px;">Please refer to your Trade license</div>', unsafe_allow_html=True)

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
