import os
import random
import re
import tkinter as tk
from PIL import Image, ImageTk

class Id:
    def __init__(self, artist, work, location, year_range):
        self.artist = artist  # or, architect
        self.work = work  # or, building
        self.place = location
        self.year_range = year_range


FULL_RANGE = range(17)
INDIA_AND_BANGLADESH = range(5)
JAPAN = range(5, 13)
GUTAI = range(5, 9) # >=1955
JIKKEN_KOBO = range(9, 13) # <=1955
CHINA = range(13, 17)


# the last entry (image or set of images of the same work) that will be included in the quiz. default: 16
IMAGE_RANGE = range(13)

"""
all of Louis Kahn's works were in 1962-1982
the only thing we need to know "Tokyo" for is the performance of Pierrot Lunaire
there's no "general" anything. it's "Central Secretariat" by Le Corbusier
"Legislative Assembly" is by Le Corbusier and "National Assembly" is by Louis Kahn
    it's on water and it's from 1961-1964
"""
answers = {
    'ha1.webp': Id('Le Corbusier', 'Central Secretariat', 'Chandigarh, India', '1955'),
    'ha2.webp': Id('Le Corbusier', 'Legislative Assembly', 'Chandigarh, India', '1961-1964'),
    'ha3.webp': Id('Louis Kahn', 'Mosque, National Assembly', 'Dhaka, Bangladesh', '1962-1982'),
    'ha4.1.webp': Id('Louis Kahn', 'National Assembly', 'Dhaka, Bangladesh', '1962-1982'),  # exterior
    'ha4.2.webp': Id('Louis Kahn', 'National Assembly', 'Dhaka, Bangladesh', '1962-1982'),  # interior

    'ha5.webp': Id('Shiraga Kazuo', 'Challenging Mud', 'Japan', '1955'),
    'ha6.webp': Id('Shiraga Kazuo', 'Work II', 'Japan', '1958'),
    'ha7.1.webp': Id('Murakami Saburō', 'Passing Through (Tsūka)', 'Japan', '1956'),
    'ha7.2.webp': Id('Murakami Saburō', 'Passing Through (Tsūka)', 'Japan', '1956'),
    'ha8.webp': Id('Tanaka Atsuko', 'Work (Bell)', 'Japan', '1955'),

    'ha9.webp': Id('Jikken Kōbō', 'performance of Pierrot Lunaire', 'Tokyo, Japan', '1955'),
    'ha10.1.webp': Id('Jikken Kōbō', 'performance of Pierrot Lunaire', 'Tokyo, Japan', '1955'),
    'ha10.2.webp': Id('Jikken Kōbō', 'performance of Pierrot Lunaire', 'Tokyo, Japan', '1955'),
    'ha11.webp': Id('Katsuhiro Yamaguchi (Jikken Kōbō)', 'Vitorīnu: Yoru no shinkō [Vitrine: Deep into the Night]', 'Japan', '1954'),
    'ha12.webp': Id('Katsuhiro Yamaguchi (Jikken Kōbō)', 'Vitrine No. 1', 'Japan', '1952'),

    'ha13.webp': Id('Luo Gongliu', "Mao Zedong Reporting on the Rectification in Yan'an", 'China', '1951'),
    'ha14.webp': Id('Dong Xiwen', 'The Founding of the Nation', 'China', '1952-1953'),
    'ha15.webp': Id('Hou Yimin', 'Liu Shaoqi and the Anyuan Coal Miners', 'China', '1961'),
    'ha16.1.webp': Id('', 'Rent Collection Courtyard', 'China', '1965'),  # made by a collective of sculptors from the Sichuan Fine Arts Institute
    'ha16.2.webp': Id('', 'Rent Collection Courtyard', 'China', '1965'),
    'ha16.3.webp': Id('', 'Rent Collection Courtyard', 'China', '1965'),
}

# "images" is expected to live in the same folder as this script.
image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

image_paths = [
    entry.path.replace("\\", "/")
    for entry in os.scandir(image_dir)
    if entry.is_file()
]


def numeric_key(path):
    filename = os.path.basename(path)
    match = re.search(r'ha(\d+)(?:\.(\d+))?', filename)
    main_num = int(match.group(1))
    sub_num = int(match.group(2)) if match.group(2) else 0
    return (main_num, sub_num)


image_paths = [p for p in image_paths if numeric_key(p)[0] in IMAGE_RANGE]
image_paths.sort(key=numeric_key)

random.shuffle(image_paths)
current_index = 0
displayed_image = None

root = tk.Tk()
root.title("Image Quiz")

image_label = tk.Label(root)
image_label.pack(padx=20, pady=(20, 10))

fields_frame = tk.Frame(root)
fields_frame.pack(padx=20, pady=10, fill="x")

# Each field: (key on Id object, display label)
FIELD_DEFS = [
    ("artist", "Artist"),
    ("work", "Work"),
    ("place", "Location"),
    ("year_range", "Year range"),
]

entries = {}
status_labels = {}
last_focused_entry = None


def remember_focus(entry_widget):
    global last_focused_entry
    last_focused_entry = entry_widget


for row, (key, label_text) in enumerate(FIELD_DEFS):
    tk.Label(fields_frame, text=f"{label_text}:", font=("Arial", 12), anchor="w", width=11).grid(
        row=row, column=0, sticky="w", pady=4
    )
    entry = tk.Entry(fields_frame, font=("Arial", 14), width=35)
    entry.grid(row=row, column=1, sticky="we", padx=(5, 5), pady=4)
    entry.bind("<FocusIn>", lambda event, e=None: remember_focus(event.widget))
    status = tk.Label(fields_frame, text="", font=("Arial", 12), width=2)
    status.grid(row=row, column=2, sticky="w")
    entries[key] = entry
    status_labels[key] = status

fields_frame.grid_columnconfigure(1, weight=1)

last_focused_entry = entries["artist"]  # sensible default before anything is clicked

# Buttons for characters that don't exist on a standard US keyboard, e.g. the
# macrons used in Hepburn romanization of Japanese (Kōbō, Saburō, Tsūka, etc.).
# Clicking one inserts the character at the cursor position in whichever
# field was most recently focused.
SPECIAL_CHARS = ["ā", "ī", "ū", "ē", "ō", "Ā", "Ī", "Ū", "Ē", "Ō"]

special_chars_frame = tk.Frame(root)
special_chars_frame.pack(padx=20, pady=(0, 10))

tk.Label(special_chars_frame, text="Insert:", font=("Arial", 10)).grid(row=0, column=0, padx=(0, 6))


def insert_special_char(char):
    target = last_focused_entry
    if target is None:
        return
    cursor_index = target.index(tk.INSERT)
    target.insert(cursor_index, char)
    target.icursor(cursor_index + len(char))
    target.focus_set()


for col, char in enumerate(SPECIAL_CHARS, start=1):
    tk.Button(
        special_chars_frame,
        text=char,
        font=("Arial", 13),
        width=2,
        command=lambda c=char: insert_special_char(c),
    ).grid(row=0, column=col, padx=2)

submit_button = tk.Button(root, text="Check", font=("Arial", 12))
submit_button.pack(pady=(0, 5))

result = tk.Label(root, font=("Arial", 12))
result.pack(pady=(0, 20))

FIELD_KEYS = [key for key, _ in FIELD_DEFS]


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


def check_all_correct(correct_id):
    all_correct = True
    for key in FIELD_KEYS:
        user_text = entries[key].get()
        if field_is_correct(key, user_text, correct_id):
            status_labels[key].config(text="✓", fg="green")
        else:
            status_labels[key].config(text="✗", fg="red")
            all_correct = False
    return all_correct


def clear_statuses():
    for key in FIELD_KEYS:
        status_labels[key].config(text="")


def show_current_image():
    global displayed_image

    if current_index >= len(image_paths):
        image_label.config(image="", text="Quiz complete!")
        fields_frame.pack_forget()
        submit_button.pack_forget()
        result.config(text=f"You got through {len(image_paths)} images. Nice work!")
        return

    with Image.open(image_paths[current_index]) as img:
        img.thumbnail((700, 500))
        displayed_image = ImageTk.PhotoImage(img.copy())

    image_label.config(image=displayed_image, text="")

    for key in FIELD_KEYS:
        entries[key].delete(0, tk.END)

    clear_statuses()
    entries[FIELD_KEYS[0]].focus_set()
    result.config(text="")


def submit_answer(event=None):
    global current_index

    if current_index >= len(image_paths):
        return

    image_path = image_paths[current_index]
    correct_id = answers.get(os.path.basename(image_path))

    if correct_id is None:
        result.config(text=f"No answer key entry for {os.path.basename(image_path)}.", fg="orange")
        return

    all_correct = check_all_correct(correct_id)

    if all_correct:
        result.config(text="Correct!", fg="green")
        current_index += 1
        root.after(500, show_current_image)
    else:
        result.config(text="Not quite — check the marked fields.", fg="red")


def focus_next_field(event, key):
    idx = FIELD_KEYS.index(key)
    if idx + 1 < len(FIELD_KEYS):
        entries[FIELD_KEYS[idx + 1]].focus_set()
    else:
        submit_answer()
    return "break"


for key in FIELD_KEYS:
    entries[key].bind("<Return>", lambda event, k=key: focus_next_field(event, k))

submit_button.config(command=submit_answer)



# Calculate the max width for each column (including the header names)
file_w = max(len("File"), max(len(k) for k in answers.keys()))
artist_w = max(len("Artist"), max(len(v.artist) for v in answers.values()))
work_w = max(len("Work"), max(len(v.work) for v in answers.values()))
place_w = max(len("Location"), max(len(v.place) for v in answers.values()))
year_w = max(len("Year"), max(len(v.year_range) for v in answers.values()))

# Construct and print the header
header = f"{'File':<{file_w}} | {'Artist':<{artist_w}} | {'Work':<{work_w}} | {'Location':<{place_w}} | {'Year':<{year_w}}"
print(header)
print("-" * len(header))

# Print each row of data
for filename, obj in answers.items():
    print(f"{obj.artist:<{artist_w}} | {obj.work:<{work_w}} | {obj.place:<{place_w}} | {obj.year_range:<{year_w}}")




show_current_image()
root.mainloop()