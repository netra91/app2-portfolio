import streamlit as st
from send_email import send_mail

st.header("contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("your email address")
    raw_message = st.text_area("enter your message")
    message = f"""\
    
    subject: new email from {user_email}
    
    from:{user_email}
    
    {raw_message}
    """
    button = st.form_submit_button("submit")
    print(button)
    if button:
        send_mail(message)
        st.info("your email was sent successfully")