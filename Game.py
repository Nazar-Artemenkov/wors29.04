import tkinter as tk
import random

# Загрузка списка слов из файла
def load_words(words):
    with open(words, 'r', encoding='utf-8') as file:
        words = [line.strip().upper() for line in file if len(line.strip()) == 5]
    return words
# Проверка слова
def check_word(guess, word):
    result = []
    for i, letter in enumerate(guess):
        if letter == word[i]:
            result.append('green')
        elif letter in word:
            result.append('yellow')
        else:
            result.append('black')
    return result
# Обновление интерфейса после попытки
def update_interface(guess, result):
    for i, letter in enumerate(guess):
        entry = entries[current_attempt][i]
        entry.delete(0, 'end')
        entry.insert('end', letter)
        entry.config(disabledforeground=result[i], state='disabled')
# Обработка попытки
def submit():
    global current_attempt
    guess = guess_var.get().upper()
    if len(guess) != 5:
        result_label.config(text="Слово должно быть длиной 5 букв!")
        return

    result = check_word(guess, current_word)
    update_interface(guess, result)

    if guess == current_word or current_attempt == 5:
        result_label.config(text=f"Слово: {current_word}")
        for entry_row in entries:
            for entry in entry_row:
                entry.config(state='disabled')
    else:
        current_attempt += 1
        result_label.config(text="")
        guess_var.set("")
# Перезапуск игры
def restart():
    global current_word, current_attempt
    current_word = random.choice(words)
    current_attempt = 0
    guess_var.set("")
    result_label.config(text="")

    for entry_row in entries:
        for entry in entry_row:
            entry.config(state='normal')
            entry.delete(0, 'end')
words = load_words('words.txt')
current_word = random.choice(words)
current_attempt = 0
root = tk.Tk()
root.title("Wordle Game")
root.geometry("800x600")  # Установка размера окна
root.config(bg='blue')  # Установка синего фона окна
light_blue = '#ADD8E6'
main_frame = tk.Frame(root, bg='blue')
main_frame.pack(expand=True)
entries = [[tk.Entry(main_frame, font=('Consolas', 24), width=2, bg=light_blue, fg='black') for _ in range(5)] for _ in range(6)]
for i, row in enumerate(entries):
    for j, entry in enumerate(row):
        entry.grid(row=i, column=j)
guess_var = tk.StringVar()
guess_entry = tk.Entry(main_frame, textvariable=guess_var, font=('Consolas', 24), width=7, bg=light_blue, fg='black')
guess_entry.grid(row=7, column=0, columnspan=5)
submit_button = tk.Button(main_frame, text="saada", command=submit, bg=light_blue, fg='black')
submit_button.grid(row=8, column=0, columnspan=5)
result_label = tk.Label(main_frame, text="", font=('Consolas', 24), bg='blue', fg='white')
result_label.grid(row=9, column=0, columnspan=5)
restart_button = tk.Button(main_frame, text="tee uuesti", command=restart, bg=light_blue, fg='black')
restart_button.grid(row=10, column=0, columnspan=5)

root.mainloop()



