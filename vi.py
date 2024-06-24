import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the translator
translator = Translator()

def translate_text():
    source_text = source_text_entry.get("1.0", tk.END)
    src_lang = src_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()

    if not source_text.strip():
        translated_text.set("Please enter text to translate")
        return

    try:
        translation = translator.translate(source_text, src=src_lang, dest=dest_lang)
        translated_text.set(translation.text)
    except Exception as e:
        translated_text.set(f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x400")

# Source language selection
tk.Label(root, text="Source Language:").pack(pady=5)
src_lang_combobox = ttk.Combobox(root, values=["en", "fr", "es", "de", "zh-cn", "ja"], state="readonly")
src_lang_combobox.set("en")
src_lang_combobox.pack(pady=5)

# Destination language selection
tk.Label(root, text="Destination Language:").pack(pady=5)
dest_lang_combobox = ttk.Combobox(root, values=["en", "fr", "es", "de", "zh-cn", "ja"], state="readonly")
dest_lang_combobox.set("fr")
dest_lang_combobox.pack(pady=5)

# Source text entry
tk.Label(root, text="Enter Text:").pack(pady=5)
source_text_entry = tk.Text(root, height=10, width=50)
source_text_entry.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Translated text display
translated_text = tk.StringVar()
translated_text_label = tk.Label(root, textvariable=translated_text, wraplength=500, justify="left")
translated_text_label.pack(pady=5)

# Run the main loop
root.mainloop()