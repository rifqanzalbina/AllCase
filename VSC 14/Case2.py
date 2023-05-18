import nltk
import random
from nltk.chat.util import Chat,reflections

# Mengatur pattern dan responsnya

patterns = [
    (r'hai', ['Halo!', 'Hai!', 'Apa kabar?']),
    (r'apa kabar', ['Baik-baik saja', 'Sedang sibuk', 'Saya baik-baik saja, terima kasih']),
    (r'siapa namamu', ['Saya adalah Chatbot', 'Nama saya Chatbot']),
    (r'terima kasih', ['Sama-sama', 'Tidak masalah', 'Senang bisa membantu']),
    (r'keluar', ['Selamat tinggal!', 'Sampai jumpa lagi!']),
]

chatbot = Chat(patterns, reflections)

print("Halo! Saya adalah chatbot sederhana. Ketik 'Keluar' untuk keluar ",chatbot.converse())
