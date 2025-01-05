import streamlit as st

# Predefined questions for different tech stacks
tech_questions = {
    "Python": [
        "What are the key differences between Python 2 and Python 3?",
        "How does Python's memory management work?",
        "What is the difference between deep copy and shallow copy in Python?",
        "Explain Python decorators with an example.",
        "How does Python handle exception handling?"
    ],
    "Django": [
        "What is Django's ORM and how does it work?",
        "Explain the concept of middleware in Django.",
        "What is the role of `settings.py` in Django?",
        "How do you optimize database queries in Django?",
        "What is a Django model and how do you use it?"
    ],
    "PostgreSQL": [
        "What is a JOIN in SQL and how does it work?",
        "Explain the difference between INNER JOIN, LEFT JOIN, and RIGHT JOIN.",
        "How would you optimize a query that runs too slowly?",
        "What is an index in PostgreSQL and how does it improve query performance?",
        "Explain the concept of database normalization."
    ],
    "JavaScript": [
        "What is the difference between `let`, `var`, and `const` in JavaScript?",
        "Explain event delegation in JavaScript.",
        "What is closure in JavaScript?",
        "What are promises in JavaScript and how do they work?",
        "Explain the concept of hoisting in JavaScript."
    ],
    # Add more technologies here
}

# Streamlit UI
st.title("TalentScout Hiring Assistant Chatbot")
st.markdown("### Your Intelligent Assistant for Candidate Screening")

# Initialize session state
if "step" not in st.session_state:
    st.session_state["step"] = 0
if "candidate" not in st.session_state:
    st.session_state["candidate"] = {}

# Candidate Information Gathering
if st.session_state["step"] == 0:
    st.write("👋 Hi! I'm here to help screen candidates. Let's get started.")
    if st.button("Start"):
        st.session_state["step"] = 1

# Candidate Information Gathering
if st.session_state["step"] == 1:
    with st.form("candidate_form"):
        st.session_state["candidate"]["name"] = st.text_input("Full Name")
        st.session_state["candidate"]["email"] = st.text_input("Email Address")
        st.session_state["candidate"]["phone"] = st.text_input("Phone Number")
        st.session_state["candidate"]["experience"] = st.slider("Years of Experience", 0, 20, 1)
        st.session_state["candidate"]["position"] = st.text_input("Desired Position")
        st.session_state["candidate"]["location"] = st.text_input("Current Location")
        st.session_state["candidate"]["tech_stack"] = st.text_area("Tech Stack (e.g., Python, Django, PostgreSQL)")

        if st.form_submit_button("Submit"):
            if all(st.session_state["candidate"].values()):  # Ensure all fields are filled
                st.session_state["step"] = 2
            else:
                st.error("Please fill in all the required fields.")

# Technical Question Generation
if st.session_state["step"] == 2:
    st.write(f"Great! Let’s generate questions for {st.session_state['candidate']['tech_stack']}.")
    tech_stack = st.session_state["candidate"]["tech_stack"].split(", ")
    
    # Clean and standardize the tech stack input
    tech_stack = [tech.strip().capitalize() for tech in tech_stack]  # Trim spaces and capitalize
    
    questions_to_display = []
    
    for tech in tech_stack:
        if tech in tech_questions:
            questions_to_display.extend(tech_questions[tech])
        else:
            questions_to_display.append(f"Sorry, no predefined questions available for {tech}.")
    
    if questions_to_display:
        for i, q in enumerate(questions_to_display, 1):
            st.write(f"**Q{i}:** {q}")
    else:
        st.error("No questions could be generated. Please try again later.")
    
    if st.button("Finish"):
        st.write("🎉 Thank you for using the Hiring Assistant! We'll process the data and get back to you.")
        st.session_state["step"] = 0
