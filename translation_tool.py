import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def translate_text():
    input_text = text_entry.get("1.0", tk.END).strip()
    source_lang = src_lang_combo.get().lower()
    target_lang = dest_lang_combo.get().lower()
    if not input_text:
        messagebox.showwarning("Warning", "Please enter some text to translate!")
        return
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
        output_entry.delete("1.0", tk.END)
        output_entry.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

def copy_to_clipboard():
    translated_text = output_entry.get("1.0", tk.END).strip()
    if translated_text:
        root.clipboard_clear()
        root.clipboard_append(translated_text)
        messagebox.showinfo("Success", "Text copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Nothing to copy!")

root = tk.Tk()
root.title("CodeAlpha - Language Translation Tool")
root.geometry("550", "450")
root.config(bg="#f0f2f5")
languages = ["English", "Hindi", "Spanish", "French", "German", "Arabic", "Chinese"]
tk.Label(root, text="Language Translation Tool", font=("Arial", 16, "bold"), bg="#f0f2f5", fg="#333").pack(pady=10)
lang_frame = tk.Frame(root, bg="#f0f2f5")
lang_frame.pack(pady=5)
tk.Label(lang_frame, text="From:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=0, padx=5)
src_lang_combo = ttk.Combobox(lang_frame, values=languages, width=12, state="readonly")
src_lang_combo.set("English")
src_lang_combo.grid(row=0, column=1, padx=5)
tk.Label(lang_frame, text="To:", bg="#f0f2f5", font=("Arial", 10)).grid(row=0, column=2, padx=5)
dest_lang_combo = ttk.Combobox(lang_frame, values=languages, width=12, state="readonly")
dest_lang_combo.set("Hindi")
dest_lang_combo.grid(row=0, column=3, padx=5)
tk.Label(root, text="Enter Text:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
text_entry = tk.Text(root, height=5, width=55, font=("Arial", 10))
text_entry.pack(pady=5)
translate_btn = tk.Button(root, text="Translate", command=translate_text, bg="#007bff", fg="white", font=("Arial", 11, "bold"), padx=15, pady=5, bd=0)
translate_btn.pack(pady=10)
tk.Label(root, text="Translated Text:", bg="#f0f2f5", font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
output_entry = tk.Text(root, height=5, width=55, font=("Arial", 10))
output_entry.pack(pady=5)
btn_frame = tk.Frame(root, bg="#f0f2f5")
btn_frame.pack(pady=10)
copy_btn = tk.Button(btn_frame, text="📋 Copy", command=copy_to_clipboard, bg="#28a745", fg="white", font=("Arial", 10), padx=10)
copy_btn.grid(row=0, column=0, padx=5)
root.mainloop()
