import tkinter as tk
import difflib

# FAQ data
faq_data = {
    "what is python": "Python is a programming language used for web, AI, and data science.",
    "what is flask": "Flask is a lightweight Python web framework.",
    "what is nlp": "NLP stands for Natural Language Processing.",
    "how to run flask app": "Use command: python app.py"
}

def get_answer(user_query):
    user_query = user_query.lower()

    matches = difflib.get_close_matches(user_query, faq_data.keys(), n=1, cutoff=0.5)

    if matches:
        return faq_data[matches[0]]
    else:
        return "Sorry, I didn't understand your question."

def send_message():
    user_text = entry_box.get()
    if user_text.strip() == "":
        return

    chat_box.insert(tk.END, "You: " + user_text + "\n")

    response = get_answer(user_text)
    chat_box.insert(tk.END, "Bot: " + response + "\n\n")

    entry_box.delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("500x500")

# Chat display box (separate output box)
chat_box = tk.Text(root, height=20, width=60)
chat_box.pack(pady=10)

# Input box (separate input field)
entry_box = tk.Entry(root, width=40)
entry_box.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
