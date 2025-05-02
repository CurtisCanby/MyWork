import tkinter as tk

def display_text():
    input = textbox.get()
    label.config(text=f"You entered: {input}")
    if input == "red" or "blue" or "green" or "yellow" or "purple" or "orange" or "pink" or "black" or "white" or "gray" or "cyan":
        label.config(fg=input)

main = tk.Tk()
main.title("Test GUI")
textbox = tk.Entry(main, width=50)
textbox.pack(pady=10,padx=40)
button = tk.Button(main, text="Submit", command=display_text)
button.pack(pady=10)
label = tk.Label(main, text="Enter text.", fg="black")
label.pack(pady=10)

main.mainloop()
