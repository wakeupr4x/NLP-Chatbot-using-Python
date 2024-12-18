# **NLP Chatbot using Python**

### **Overview**
This project is an **NLP-based chatbot** developed using Python. It is designed to understand user input, classify intents, and respond with appropriate answers. The chatbot leverages natural language processing (NLP) techniques, machine learning models, and a structured `intents.json` file to provide dynamic and context-aware responses.  

The application uses **Streamlit** for the user interface, offering a modern and intuitive platform for interaction.

---

### **Key Features**
- **Intent Classification**: Uses machine learning to identify the intent of the user's input.  
- **Customizable Responses**: Responses are stored in a JSON file, making it easy to expand or modify.  
- **Modern UI**: Built with **Streamlit** to deliver a clean and user-friendly interface.  
- **Scalable**: Add new intents and responses effortlessly to meet future requirements.  
- **Interactive Chat Flow**: The bot can follow up responses with prompts like *"Do you want more info?"*.  

---

### **Technologies Used**
The following technologies and libraries are used to build this chatbot:

1. **Python** - Primary programming language.  
2. **NLTK** - Natural Language Toolkit for text preprocessing.  
3. **Scikit-Learn** - For training machine learning models.  
   - `TfidfVectorizer`: Converts text into numerical features.  
   - `LogisticRegression`: For intent classification.  
4. **Streamlit** - Front-end framework for a modern chatbot UI.  
5. **JSON** - For storing intents and responses.  

---

### **Project Structure**
```
NLP-Chatbot-using-Python/
│
├── intents.json          # JSON file containing intents and responses.
├── application.py        # Main Python script for the chatbot.
├── trained_data.ipynb    # Jupyter notebook for training/testing the model.
├── nltk_data/            # NLTK pre-downloaded data.
├── .venv/                # Python virtual environment.
├── README.md             # Project documentation.
├── requirements.txt      # List of Python dependencies.
└── app interface.png     # Screenshot of the chatbot's interface.
```

---

### **Setup Instructions**

Follow the steps below to install and run the project:

#### 1. **Clone the Repository**
First, clone this repository to your local system:
```bash
git clone https://github.com/wakeupr4x/NLP-Chatbot-using-Python.git
cd NLP-Chatbot-using-Python
```

#### 2. **Set Up a Virtual Environment**
It is recommended to use a virtual environment for the project dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # On Linux/Mac
.\.venv\Scripts\activate    # On Windows
```

#### 3. **Install Dependencies**
Install the required Python libraries using `requirements.txt`:
```bash
pip install -r requirements.txt
```

#### 4. **Download NLTK Data**
Ensure you have the required NLTK datasets downloaded:
```python
import nltk
nltk.download('punkt')
```

#### 5. **Run the Chatbot Application**
Launch the Streamlit app:
```bash
streamlit run application.py
```
The chatbot UI will open in your browser at `http://localhost:8501`.

---

### **How to Use**
1. Launch the chatbot by running the application.
2. Enter a message or query in the chat input box (e.g., "Hi", "How do I start gardening?").
3. The chatbot will analyze your input, classify the intent, and respond accordingly.
4. After each response, the bot may ask follow-up questions like *"Do you want more info?"* for additional interaction.

---

### **Customization**
1. **Add New Intents**: Update the `intents.json` file with new patterns and responses.
    ```json
    {
        "tag": "new_topic",
        "patterns": ["example question 1", "example question 2"],
        "responses": ["example response 1", "example response 2"]
    }
    ```
2. **Train the Model**: Update and retrain the model in `trained_data.ipynb` using the new data.

3. **UI Changes**: Modify the **Streamlit** layout in `application.py` to enhance the user interface.

---

### **Screenshots**
Here’s a preview of the chatbot interface:

![Chatbot UI](app%20interface.png)

---

### **Future Improvements**
1. Integrate **real-time APIs** for weather, news, or other live data.  
2. Add **memory** to handle conversational context over multiple exchanges.  
3. Implement advanced models like **Rasa** or **Transformers** for better NLP performance.  
4. Improve the interface using **Streamlit themes** or integrate other frameworks.  

---

### **Contributing**
Contributions are welcome! If you'd like to improve or extend the project:
1. Fork the repository.  
2. Create a new branch: `git checkout -b feature-branch`.  
3. Commit your changes: `git commit -m "Add new feature"`.  
4. Push the changes: `git push origin feature-branch`.  
5. Submit a Pull Request.  

---

### **License**
This project is licensed under the MIT License. You are free to use, modify, and distribute it.

---

### **Contact**
For any questions, feedback, or suggestions, feel free to reach out:

- **GitHub**: [@wakeupr4x](https://github.com/wakeupr4x)

---

This README will provide clarity about the project and make it easier for others to install, run, and contribute to the chatbot.

For further info, please feel free to drop a message :)
