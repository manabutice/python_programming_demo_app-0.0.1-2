import tkinter as tk
  
def set_text():
  str_var.set("こんにちは")

def get_text():
  print(str_var.get())

root = tk.Tk()
# entry = tk.entry

str_var = tk.StringVar()



entry = tk.Entry(root, width=20, textvariable=str_var)
entry.pack()
button1 = tk.Button(root, text="取得", command=get_text)
button1.pack(side=tk.LEFT)
button2 = tk.Button(root, text="設定", command=set_text)
button2.pack(side=tk.LEFT)

label = tk.Label(root, text="text")
label.pack(side=tk.LEFT)

root.mainloop()