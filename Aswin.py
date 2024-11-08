import streamlit as st

# Question prompt
st.write("How good is Aswin Suresh?")

# Radio buttons for rating, no default option selected
rating = st.radio("", options=["Select", "10", "9", "8", "<8"], index=0, key="rating", horizontal=True)

# Check if the user selected a valid rating
if rating == "10":
    st.write("Mmmm, you are a smart ass!")
elif rating == "9":
    st.write("Mm close but still not right")
elif rating == "8":
    st.write("Well, you are getting there!")
elif rating == "<8":
    # Trigger a vibration effect (using custom HTML and CSS)
    st.markdown("""
        <style>
            @keyframes vibrate {
                0% { transform: translateX(0); }
                25% { transform: translateX(-5px); }
                50% { transform: translateX(5px); }
                75% { transform: translateX(-5px); }
                100% { transform: translateX(0); }
            }
            .vibrate {
                animation: vibrate 0.5s linear;
            }
        </style>
        <div class="vibrate" style="font-size: 20px; color: red; text-align: center;">
            Error: Rating below 8 is not allowed!
        </div>
    """, unsafe_allow_html=True)
