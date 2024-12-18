import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Configure SSL and download NLTK data
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from the JSON file
file_path = os.path.abspath("./intents.json")
with open(file_path, "r") as file:
    intents = json.load(file)

# Initialize NLP model and vectorizer
vectorizer = TfidfVectorizer(ngram_range=(1, 4))
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)


def chatbot(input_text):
    """Function to predict chatbot responses based on input text."""
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response


# Initialize conversation log in session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # To store chat messages
if "chat_counter" not in st.session_state:
    st.session_state.chat_counter = 0  # For counting chat interactions


def save_to_csv(user_input, response):
    """Save chat conversation to a CSV file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists('chat_log.csv'):
        with open('chat_log.csv', 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['User Input', 'Chatbot Response', 'Timestamp'])
    with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([user_input, response, timestamp])


# Main function for the chatbot app
def main():
    """Main function to run the ChatGPT-like interface."""
    st.set_page_config(page_title="Modern Chatbot", page_icon="🤖", layout="centered")

    # Sidebar navigation
    st.sidebar.title("🔧 Options")
    menu = ["🏠 Chat", "🕒 Conversation History", "📘 About"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    # Main Chat Page
    if choice == "🏠 Chat":
        st.title("🤖 WAKEUPRAX : An NLP based Chatbot ready to assist you  :)")
        st.caption("Powered by NLP and Logistic Regression. Ask me anything!")

        # Display previous chat messages
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # User input in a modern chat box
        user_input = st.chat_input("Send a message...")

        if user_input:
            # Display user message
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            # Get chatbot response
            response = chatbot(user_input)
            save_to_csv(user_input, response)  # Save to CSV log

            # Display chatbot response
            st.session_state.messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.markdown(response)

            # Stop chat if goodbye response is detected
            if response.lower() in ['goodbye', 'bye']:
                st.success("Thanks for chatting! Have a great day! 🎉")
                st.stop()

    # Conversation History Page
    elif choice == "🕒 Conversation History":
        st.title("📝 Conversation History")
        if not os.path.exists("chat_log.csv"):
            st.warning("No conversation history found.")
        else:
            with open("chat_log.csv", "r", encoding="utf-8") as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip header row
                for row in csv_reader:
                    st.markdown(f"**🧑‍💻 User:** {row[0]}")
                    st.markdown(f"**🤖 Chatbot:** {row[1]}")
                    st.caption(f"🕒 {row[2]}")
                    st.markdown("---")

    # About Page
    elif choice == "📘 About":
        st.title("📘 About the Chatbot")
        st.info(
            "This chatbot uses Natural Language Processing and Logistic Regression "
            "to predict user intents and generate responses. The interface is designed "
            "to resemble modern chat applications like ChatGPT."
        )
        st.subheader("Features:")
        st.markdown("""
        - **Modern Interface**: Clean and conversational UI using `st.chat_message` and `st.chat_input`.
        - **Persistent Chat**: View your chat history during the session.
        - **Logging**: All conversations are saved to a CSV file for later review.
        """)
        st.subheader("Technologies Used:")
        st.markdown("""
        - Python
        - Streamlit
        - Scikit-learn
        - NLTK
        """)

        st.caption("✨ Built with love for NLP and AI enthusiasts! ✨")


if __name__ == "__main__":
    main()
