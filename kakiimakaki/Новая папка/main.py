
import interface
from ciphers import caesar_encrypt , tabs
def encrypt():
    plaintext = interface.plaintextbox.get()
    key = int(interface.keybox.get())
    message = caesar_encrypt(plaintext, key)
    message1 = tabs(plaintext)
    interface.label4.config(text=message)
    interface.label6.config(text=message1)
interface.button.config(command=encrypt)
interface.window.mainloop()
