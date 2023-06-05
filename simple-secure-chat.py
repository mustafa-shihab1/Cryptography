import socket
import threading 
import rsa  
import ecdsa 
import hashlib 
import tkinter as tk 
import sqlite3 

public_key_rsa, private_key_rsa = rsa.newkeys(1024)
private_key_ecc = ecdsa.SigningKey.generate()
public_key_ecc = private_key_ecc.get_verifying_key()

public_partner_rsa = None
public_partner_ecc = None

conn = sqlite3.connect('chat.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS messages (
              sender TEXT,
              receiver TEXT,
              message TEXT,
              timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
          )
          ''')

root = tk.Tk()
root.title("RSA-ECC Chat")
frame = tk.Frame(root)
frame.pack()
label = tk.Label(frame, text="Choose (1)mustafa or (2)dark:")
label.pack()
choice_var = tk.StringVar()
choice_entry = tk.Entry(frame, textvariable=choice_var)
choice_entry.pack()


def print_messages():
    conn = sqlite3.connect('chat.db')
    c = conn.cursor()
    c.execute('SELECT sender, message FROM messages WHERE sender = "mustafa" OR sender = "dark"')
    messages = c.fetchall()
    for sender, message in messages:
        print(f"{sender}: {message}")
    conn.close()


def start_chat():

    global public_partner_rsa
    global public_partner_ecc
    choice = choice_var.get()

    if choice == "1":
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("localhost", 9999))
        server.listen()
        client, _ = server.accept()

        client.send(public_key_rsa.save_pkcs1("PEM"))
        client.send(public_key_ecc.to_pem())

        public_partner_rsa = rsa.PublicKey.load_pkcs1(client.recv(1024))
        public_partner_ecc = ecdsa.VerifyingKey.from_pem(client.recv(1024))

    elif choice == "2":
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("localhost", 9999))

        public_partner_rsa = rsa.PublicKey.load_pkcs1(client.recv(1024))
        public_partner_ecc = ecdsa.VerifyingKey.from_pem(client.recv(1024))

        client.send(public_key_rsa.save_pkcs1("PEM"))
        client.send(public_key_ecc.to_pem())

    else:
        exit()


    send_frame = tk.Frame(root)
    send_frame.pack()

    send_label = tk.Label(send_frame, text="Your message:")
    send_label.pack(side=tk.LEFT)

    send_var = tk.StringVar()
    send_entry = tk.Entry(send_frame, textvariable=send_var)
    send_entry.pack(side=tk.LEFT)


    def send_message():
        message = send_var.get()
        encrypted_message_rsa = rsa.encrypt(message.encode(), public_partner_rsa)
        signature_ecc = private_key_ecc.sign(message.encode(), hashfunc=hashlib.sha256)

        client.send(encrypted_message_rsa)
        client.send(signature_ecc)

        c.execute('''
              INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)
              ''', ('mustafa' if choice == '1' else 'dark', 'dark' if choice == '1' else 'mustafa', message))
        conn.commit()

        print('You: ' + message)
        send_var.set("")

    send_button = tk.Button(send_frame, text="Send", command=send_message)
    send_button.pack(side=tk.LEFT)


    def receive_messages(c):
        while True:
            encrypted_message_rsa = c.recv(1024)
            signature_ecc = c.recv(1024)

            decrypted_message_rsa = rsa.decrypt(encrypted_message_rsa, private_key_rsa).decode()
            is_verified = public_partner_ecc.verify(signature_ecc, decrypted_message_rsa.encode(), hashfunc=hashlib.sha256)
            if is_verified:
                print('mustafa: ' + decrypted_message_rsa if choice == '2' else 'dark: ' + decrypted_message_rsa)

    threading.Thread(target=receive_messages, args=(client,)).start()

    print_messages()


start_button = tk.Button(frame, text="Start Chat", command=start_chat)
start_button.pack()

root.mainloop()
