TalentScout Hiring Assistant
Overview
TalentScout is a chatbot designed to assist in the initial screening of candidates for technical roles. It collects key information such as the candidate's name, contact details, years of experience, desired position, and tech stack. Based on the candidate's declared tech stack, it dynamically generates technical interview questions to assess proficiency, providing a seamless and efficient screening process.

Features
Collect basic candidate details such as name, email, phone, experience, position, and tech stack.
Dynamically generate technical interview questions based on the candidate's declared tech stack (e.g., Python, Django, PostgreSQL).
Gracefully handle the flow of conversation, ensuring a coherent user experience.
Provide a fallback mechanism for handling unexpected inputs.
Allow users to end the conversation gracefully with a thank you message.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/TalentScoutChatbot.git
Navigate to the project directory:

bash
Copy code
cd TalentScoutChatbot
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
streamlit run your_script_name.py
The app will be available at http://localhost:8501.

Usage
Start the Chatbot: Upon launching the app, click the "Start" button to begin the interaction.
Provide Candidate Information: Enter details such as name, email, phone number, years of experience, desired position, current location, and tech stack.
Generate Technical Questions: Once the information is provided, the chatbot will generate a set of technical questions based on the candidate's declared tech stack (e.g., Python, Django, PostgreSQL).
Finish: After the questions are displayed, click the "Finish" button to conclude the interaction.
Example Interaction
Greeting: The chatbot greets the user and prompts them to start the process.
Information Gathering: The user fills in their details and tech stack.
Technical Question Generation: The chatbot generates and displays questions based on the specified tech stack.
Completion: After the questions are displayed, the chatbot concludes the conversation and exits.
File Structure
bash
Copy code
.
├── requirements.txt       # List of required Python packages
├── your_script_name.py    # Main Python script for the chatbot
└── README.md              # Project documentation (this file)
Technical Details
Predefined Tech Stack Questions: The chatbot uses predefined questions for several technologies, including Python, Django, PostgreSQL, and JavaScript. These questions are used to assess a candidate's technical knowledge based on their declared tech stack.
Streamlit Interface: The application uses Streamlit to create a clean and interactive user interface for candidates to interact with.
Challenges & Solutions
Challenge: Managing candidate data and maintaining the flow of conversation.
Solution: Used Streamlit's session state to track and store candidate information across the conversation.
Challenge: Handling tech stack input and generating relevant questions.
Solution: Implemented a dictionary of predefined questions to generate questions based on the candidate's tech stack.
Future Enhancements
Advanced Question Generation: Implement a system for dynamically generating interview questions using an advanced language model (e.g., GPT-3).
Sentiment Analysis: Add sentiment analysis to understand the candidate's mood during the interaction.
Multilingual Support: Add support for multiple languages to cater to a diverse audience.