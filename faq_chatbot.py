import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_data = {
    "what is codealpha?": "CodeAlpha is a platform offering virtual internship programs for students to build real-world tech skills.",
    "how many tasks do i need to complete?": "According to the instruction sheet, you must complete a minimum of 2 or 3 tasks to get your certificate.",
    "where should i submit my tasks?": "You need to upload your source code to GitHub and submit the project link using the official Submission Form.",
    "will i get a certificate?": "Yes, upon successful completion and submission of the required tasks, you will receive an Internship Certificate.",
    "how to contact codealpha support?": "You can email them at services.codealpha@gmail.com or via WhatsApp at +91 9336576663.",
    "hello": "Hello! I am your FAQ assistant. How can I help you with your CodeAlpha internship today?",
    "hi": "Hi there! How can I assist you today?"
}
questions = list(faq_data.keys())
answers = list(faq_data.values())

def get_bot_response(user_query):
    user_query = user_query.lower().strip()
    all_texts = questions + [user_query]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
    best_match_idx = similarity_scores.argmax()
    if similarity_scores[best_match_idx] > 0.3:
        return answers[best_match_idx]
    else:
        return "I'm sorry, I couldn't find an exact answer to that. Please contact support at services.codealpha@gmail.com."

def send_message():
    user_text = user_input.get().strip()
    if not user_text:
        return
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_text + "\n", "user")
    bot_response = get_bot_response(user_text)
    chat_display.insert(tk.END, "Bot: " + bot_response + "\n\n", "bot")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)
    user_input.delete(0, tk.END)

root = tk.Tk()
root.title("CodeAlpha - FAQ Chatbot")
root.geometry("450", "500")
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20, width=50, font=("Arial", 10))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_display.tag_config("user", foreground="#007bff", font=("Arial", 10, "bold"))
chat_display.tag_config("bot", foreground="#333333")
chat_display.insert(tk.END, "Bot: Hello! Ask me anything about your CodeAlpha internship.\n\n", "bot")
chat_display.config(state=tk.DISABLED)
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, padx=10, pady=5)
user_input = tk.Entry(input_frame, font=("Arial", 11), width=35)
user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
user_input.bind("<Return>", lambda event: send_message())
send_btn = tk.Button(input_frame, text="Send", bg="#28a745", fg="white", font=("Arial", 10, "bold"), command=send_message)
send_btn.pack(side=tk.RIGHT)
root.mainloop()
