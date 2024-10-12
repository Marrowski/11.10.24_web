from tkinter import *
from tkinter import ttk
import requests

root = Tk()
root.title('Yemelianov Oleh. HTTP-client')
root.geometry('900x500')
root.configure(bg = 'burlywood2')

def send_request():
    selected = combobox.get()
    url = http_req.get()

    if selected == 'GET':
        response = requests.get(url)
        message.set(response.text)
    elif selected == 'POST':
        data_response = requests.post(url, data = {'name': 'Ivan', 'surname': 'Petrov', 'language': 'Python'})
        message.set(data_response.text)
    elif selected == 'DELETE':
        resp_del = requests.delete(url)
        message.set(resp_del.text)

message = StringVar()

name_label = Label(root, text='HTTP-client. Made by Yemelianov Oleh', font=('Arial Bold', 20))
name_label.pack(expand=True, side=TOP)

prog_title = Label(root, text='Enter link here:', font=('Arial Bold', 20))
prog_title.pack(side=TOP)

http_req = Entry(root, width=50)
http_req.pack(expand=True, side=TOP)

types_query = ['GET', 'POST', 'DELETE']
combobox = ttk.Combobox(values=types_query)
combobox.pack(anchor=CENTER, padx=6, pady=6)

btn = ttk.Button(text='Send request', command=send_request)
btn.pack(expand=True)

info = ttk.Label(width=50, textvariable=message)
info.pack(anchor=CENTER, padx=6, pady=6)

label_output = Label(text='Result:')
label_output.pack(anchor=CENTER)

root.mainloop()