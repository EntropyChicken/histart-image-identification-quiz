import os
import re
import tkinter as tk
from PIL import Image, ImageTk

FIELD_DEFS = [
    ("artist", "Artist"),
    ("work", "Work"),
    ("place", "Location"),
    ("year_range", "Year range"),
    ("art_group", "Art group"),
]
FIELD_KEYS = [key for key, _ in FIELD_DEFS]

# Characters that don't exist on a standard US keyboard, e.g. the macrons used
# in Hepburn romanization of Japanese (Kōbō, Saburō, Tsūka, etc.).
SPECIAL_CHARS = ["ā", "ī", "ū", "ē", "ō", "Ā", "Ī", "Ū", "Ē", "Ō"]


def normalize(text):
    text = text.strip().lower()
    text = re.sub(r"[\u2013\u2014]", "-", text)  # normalize en/em dashes to hyphen
    text = re.sub(r"\s*-\s*", "-", text)  # tighten spacing around hyphens
    text = re.sub(r"\s+", " ", text)  # collapse whitespace
    text = re.sub(r"[.,]", "", text)  # drop stray punctuation
    return text


def field_is_correct(key, user_text, correct_id):
    correct_value = getattr(correct_id, key)
    # Fields left blank in the answer key (e.g. unknown artist) are
    # auto-accepted so they never block the user from progressing.
    if correct_value.strip() == "":
        return True
    return normalize(user_text) == normalize(correct_value)


class QuizApp:
    def __init__(self, image_paths, answers):
        self.image_paths = image_paths
        self.answers = answers
        self.current_index = 0
        self.displayed_image = None

        self.root = tk.Tk()
        self.root.title("Image Quiz")

        self.image_label = tk.Label(self.root)
        self.image_label.pack(padx=20, pady=(20, 10))

        self.fields_frame = tk.Frame(self.root)
        self.fields_frame.pack(padx=20, pady=10, fill="x")

        self.entries = {}
        self.status_labels = {}
        self.last_focused_entry = None

        for row, (key, label_text) in enumerate(FIELD_DEFS):
            tk.Label(
                self.fields_frame,
                text=f"{label_text}:",
                font=("Arial", 12),
                anchor="w",
                width=11,
            ).grid(row=row, column=0, sticky="w", pady=4)
            entry = tk.Entry(self.fields_frame, font=("Arial", 14), width=35)
            entry.grid(row=row, column=1, sticky="we", padx=(5, 5), pady=4)
            entry.bind("<FocusIn>", self._remember_focus)
            entry.bind("<Return>", lambda event, k=key: self._focus_next_field(k))
            status = tk.Label(self.fields_frame, text="", font=("Arial", 12), width=2)
            status.grid(row=row, column=2, sticky="w")
            self.entries[key] = entry
            self.status_labels[key] = status

        self.fields_frame.grid_columnconfigure(1, weight=1)
        self.last_focused_entry = self.entries["artist"]

        special_chars_frame = tk.Frame(self.root)
        special_chars_frame.pack(padx=20, pady=(0, 10))
        tk.Label(special_chars_frame, text="Insert:", font=("Arial", 10)).grid(
            row=0, column=0, padx=(0, 6)
        )
        for col, char in enumerate(SPECIAL_CHARS, start=1):
            tk.Button(
                special_chars_frame,
                text=char,
                font=("Arial", 13),
                width=2,
                command=lambda c=char: self._insert_special_char(c),
            ).grid(row=0, column=col, padx=2)

        self.submit_button = tk.Button(
            self.root, text="Check", font=("Arial", 12), command=self.submit_answer
        )
        self.submit_button.pack(pady=(0, 5))

        self.result = tk.Label(self.root, font=("Arial", 12))
        self.result.pack(pady=(0, 20))

    def _remember_focus(self, event):
        self.last_focused_entry = event.widget

    def _insert_special_char(self, char):
        target = self.last_focused_entry
        if target is None:
            return
        cursor_index = target.index(tk.INSERT)
        target.insert(cursor_index, char)
        target.icursor(cursor_index + len(char))
        target.focus_set()

    def _focus_next_field(self, key):
        idx = FIELD_KEYS.index(key)
        if idx + 1 < len(FIELD_KEYS):
            self.entries[FIELD_KEYS[idx + 1]].focus_set()
        else:
            self.submit_answer()
        return "break"

    def _clear_statuses(self):
        for key in FIELD_KEYS:
            self.status_labels[key].config(text="")

    def _check_all_correct(self, correct_id):
        all_correct = True
        for key in FIELD_KEYS:
            user_text = self.entries[key].get()
            if field_is_correct(key, user_text, correct_id):
                self.status_labels[key].config(text="✓", fg="green")
            else:
                self.status_labels[key].config(text="✗", fg="red")
                all_correct = False
        return all_correct

    def show_current_image(self):
        if self.current_index >= len(self.image_paths):
            self.image_label.config(image="", text="Quiz complete!")
            self.fields_frame.pack_forget()
            self.submit_button.pack_forget()
            self.result.config(text=f"You got through {len(self.image_paths)} images. Nice work!")
            return

        with Image.open(self.image_paths[self.current_index]) as img:
            img.thumbnail((700, 500))
            self.displayed_image = ImageTk.PhotoImage(img.copy())

        self.image_label.config(image=self.displayed_image, text="")

        for key in FIELD_KEYS:
            self.entries[key].delete(0, tk.END)

        self._clear_statuses()
        self.entries[FIELD_KEYS[0]].focus_set()
        self.result.config(text="")

    def submit_answer(self, event=None):
        if self.current_index >= len(self.image_paths):
            return

        image_path = self.image_paths[self.current_index]
        correct_id = self.answers.get(os.path.basename(image_path))

        if correct_id is None:
            self.result.config(
                text=f"No answer key entry for {os.path.basename(image_path)}.",
                fg="orange",
            )
            return

        if self._check_all_correct(correct_id):
            self.result.config(text="Correct!", fg="green")
            self.current_index += 1
            self.root.after(500, self.show_current_image)
        else:
            self.result.config(text="Not quite — check the marked fields.", fg="red")

    def run(self):
        self.show_current_image()
        self.root.mainloop()
