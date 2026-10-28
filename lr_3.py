import tkinter as tk
from tkinter import messagebox
import threading
import time
import winsound


def shift_char(char,shift):
    alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if char not in alf:
        return char
    cur_ind = alf.index(char)
    new_ind = (cur_ind + shift) % len(alf)
    return alf[new_ind]
    

def generator_key(first_block):
    first_block == first_block.upper()
    if len(first_block) != 5:
        return None

    second_block = ''.join(shift_char(c,3) for c in first_block)
    third_block = ''.join(shift_char(c,5) for c in first_block)

    return f"{first_block}-{second_block}-{third_block}"


def generate():
    user_input = ENTRY_INPUT.get().strip()
    if len(user_input) != 5:
        messagebox.showerror("Ошибка", "Первый блок должен содержать 5 символов!")
        return
    generated_key = generator_key(user_input)
    if generated_key:
        ENTRY_RESULT.config(state='normal')
        ENTRY_RESULT.delete(0, tk.END)
        ENTRY_RESULT.insert(0, generated_key)
        ENTRY_RESULT.config(state="readonly", readonlybackground="#1e1e2e", fg="#a6e3a1")


def play_8bit_music():
    melody = [
        (659, 150), (659, 150), (0, 150), (659, 150), (0, 150), (523, 150), (659, 150), (0, 150),
        (784, 150), (0, 300), (392, 150), (0, 300),
        (523, 200), (0, 150), (392, 150), (0, 150), (330, 200), (0, 150),
        (440, 150), (494, 150), (466, 150), (440, 150),
        (392, 120), (659, 12), (784, 120), (880, 150), (698, 120), (784, 120),
        (0, 150), (659, 150), (0, 150), (523, 150), (587, 150), (494, 150)
    ] # Super Mario Bros

    while True:
        for freq, duration in melody:
            if freq == 0:
                time.sleep(duration / 1000.0)
            else:
                winsound.Beep(freq, duration)
        time.sleep(0.5)

# --- Создание интерфейса ---
window = tk.Tk()
window.title("Keygen for WarHammer")
window.geometry("800x450")
window.resizable(False, False)

bg_default = "#11111b"
window.config(bg=bg_default)
bg_image = tk.PhotoImage(file = "WarHammer.png")
bg_elements = "#181825"
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label_title = tk.Label(
    window, 
    text="KEYGEN", 
    font=("Courier New", 18, "bold"), 
)
label_title.grid(row=0, column=0, pady=20)
# Контейнер ввода
frame_input = tk.Frame(window, bg=bg_elements, padx=10, pady=5)
frame_input.grid(row=1, column=3, pady=5)

label_input = tk.Label(frame_input, text="Входной блок:", font=("Courier New", 11), bg=bg_elements, fg="#cdd6f4")
label_input.grid(row=0, column=0, padx=5)

ENTRY_INPUT = tk.Entry(frame_input, font=("Courier New", 12, "bold"), width=10, bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4", justify="center")
ENTRY_INPUT.grid(row=0, column=1, padx=5)

# Кнопка генерации
btn_generate = tk.Button(
    window, 
    text="[ GENERATE KEY ]", 
    font=("Courier New", 11, "bold"), 
    bg="#313244", 
    fg="#a6e3a1", 
    activebackground="#a6e3a1",
    activeforeground="#11111b",
    command=generate,
    cursor="hand2",
    
    relief="raised"
)
btn_generate.grid(row=2, column=3, pady=20)

# Поле результата
ENTRY_RESULT = tk.Entry(
    window, 
    font=("Courier New", 14, "bold"), 
    width=23, 
    bg="#1e1e2e", 
    fg="#a6e3a1",               
    readonlybackground="#1e1e2e",
    justify="center",
    state="readonly"
)
ENTRY_RESULT.grid(row=3, column=3, pady=5)

music_thread = threading.Thread(target=play_8bit_music, daemon=True)
music_thread.start()

window.mainloop()