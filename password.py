import re
import streamlit as st

#page stiling
st.set_page_config(page_title="passwerd generator", page_icon=":lock:", layout="centered")
#custom css
st.markdown(
    """
    <style>
    .main {text-align: center;}
    .stTextInput {width: 60% : imprtant; margin: auto;}
    .stButton button {width: 50$; background-color #4CAF50; color: width; font-size: 18px; }
    .stButton button:hover {background-color: #45a049;}

    <style/>
    """
    ,unsafe_allow_html=True
)
#page title and discription
st.title("passwerd strangth Genrator")
st.write("Enter your passwerd below to check its security level.")

#function to check passwerd strength

def check_passwerd_strength(passwerd):
    score = 0
    feedback = []

    if len(passwerd) >= 8:
        score += 1 #increased
    else:
        feedback.append("password should be **atleast 8 character long**")

    if re.search(r"[A-Z]", passwerd) and re.search(r"[a-z]",passwerd):
        score += 1
    else:
        feedback.append("password should include **both upper case (A-Z) and lower case (a-z)letters**.")         
    if re.search(r"\d",passwerd):
        score +=1
    else:
        feedback.append("password should include **at least one number(0-9)**.") 

    #special charectors
    if re.search(r"[!@#$%^&*]",passwerd):
        score +=1
    else:
        feedback.append("password should include **at least one special character (!@#$%^&*)")

    #display password strength results
    if score == 4:
        st.success("**Strong Password** Your password is secure")
    elif score == 3 :
        st.info("**Moderat Password** - Consider improving security by adding more feature")
    else:
        st.error("**week Passwod** - Follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("**Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong")

#Button working 
if st.button("Check Strength"):
    if password:
        check_passwerd_strength(password)
    else:
        st.warning("Please enter a password first") #show warning if passwod empty
            