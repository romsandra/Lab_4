#Вариант_5
import tkinter as tk


def clicked():
    symbols = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
               'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
               'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
               'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
               '0': 27, '1': 28, '2': 29, '3': 30, '4': 31, '5': 32, '6': 33, '7': 34,
               '8': 35, '9': 36}

    inv_symbols = {value: key for key, value in symbols.items()}
    STROKA = str(arg_A.get())
    B = ''
    C = ''
    A = STROKA

    if len(STROKA) == 5:
        for number in STROKA:
            b = symbols.get(number)
            b = b + 3
            if b > 36:
                b = b - 36
            b = inv_symbols.get(b)
            B += b

        for number in STROKA:
            c = symbols.get(number)
            c = c - 5
            if c < 0:
                c = c + 36
            c = inv_symbols.get(c)
            C += c

        lbl_result.configure(text=f'{A}-{B}-{C}')

    else:
        lbl_result.configure(text='Введено неверное \n количество символов')


def close():
    window.destroy()


window = tk.Tk()
window.title('Tignari super lover 3000')
window.geometry('540x680')
bg = tk.PhotoImage(file='genshin.png')

label_bg = tk.Label(window, image=bg)
label_bg.place(relx=0, rely=0)

lbl_A = tk.Label(window, text='GENSHIN', font=('Arial', 30), bg='#4d9900')
lbl_A.grid(column=0, row=0, padx=10, pady=20)
arg_A = tk.Entry(window, width=15, font=('Arial', 15))
arg_A.insert(0, '')
arg_A.grid(column=0, row=2, padx=10, pady=20)

lbl_roots = tk.Label(window, text='Введите 5 символов:', font=('Arial', 15), bg='#4d9900')
lbl_roots.grid(column=0, row=1)
lbl_result = tk.Label(window, text='Результат', font=('Arial', 15))
lbl_result.grid(column=0, row=4)

btn = tk.Button(window, text='Сгенерировать ключ', font=('Arial', 15), bg='#4d9900', command=clicked)
btn.grid(column=0, row=3)
exit = tk.Button(window, text='Выход', font=('Arial', 15), bg='#4d9900', command=close)
exit.grid(column=0, row=7)

window.mainloop()

