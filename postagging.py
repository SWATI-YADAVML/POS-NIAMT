import tkinter as tk
from tkinter import filedialog, messagebox
import spacy
from docx import Document

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Function to process text and return POS tags
def tag_text(text):
    doc = nlp(text)
    return [(token.text, token.pos_) for token in doc]

# Function to tag sentence from input box
def tag_sentence():
    sentence = entry.get()
    if not sentence.strip():
        messagebox.showwarning(title="Warning", message="Please enter a sentence.")
        return
    tagged = tag_text(sentence)
    result_text.delete('1.0', tk.END)
    for word, pos in tagged:
        result_text.insert(tk.END, f"{word}: {pos}\n")

# Function to tag from MS Word file
def tag_file():
    file_path = filedialog.askopenfilename(
        title="Select Word File",
        filetypes=[("Word Documents", "*.docx")]
    )
    if not file_path:
        return
    doc = Document(file_path)
    full_text = "\n".join([para.text for para in doc.paragraphs])
    tagged = tag_text(full_text)
    result_text.delete('1.0', tk.END)
    for word, pos in tagged:
        result_text.insert(tk.END, f"{word}: {pos}\n")

# Function to tag from TXT file in Downloads
def tag_text_file():
    file_path = filedialog.askopenfilename(
        initialdir="C:/Users/gauta/Downloads",  # change "gauta" to your actual username if needed
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt")]
    )
    if not file_path:
        return
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    tagged = tag_text(content)
    result_text.delete('1.0', tk.END)
    for word, pos in tagged:
        result_text.insert(tk.END, f"{word}: {pos}\n")

# Create GUI
root = tk.Tk()
root.title("POS Tagging App")
root.geometry("600x500")

label = tk.Label(root, text="POS Tagging App", font=("Arial", 18, "bold"))
label.pack(pady=10)

entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(pady=10)

btn_tag = tk.Button(root, text="Tag Sentence", command=tag_sentence, bg="green", fg="white", width=20)
btn_tag.pack(pady=5)

btn_file = tk.Button(root, text="Tag MS Word File", command=tag_file, bg="blue", fg="white", width=20)
btn_file.pack(pady=5)

btn_tag_txt = tk.Button(root, text="Tag TXT File", command=tag_text_file, bg="orange", fg="white", width=20)
btn_tag_txt.pack(pady=5)

result_label = tk.Label(root, text="Tagged Words:", font=("Arial", 14))
result_label.pack(pady=10)

result_text = tk.Text(root, width=70, height=15, font=("Consolas", 11))
result_text.pack()

root.mainloop()