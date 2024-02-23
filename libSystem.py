#emre çınar py kod 200209019
import tkinter as tk
from tkinter import messagebox

# Öğrenci ve Kitap Bilgilerini Saklamak İçin Listeler
borrowed_books = []

# Mevcut Kitaplar
available_books = [
            {"title": "Küçük Prens", "author": "Antoine de Saint-Exupéry", "stock": 10},
            {"title": "Harry Potter", "author": "J.K. Rowling", "stock": 15},
            {"title": "Yüzüklerin Efendisi", "author": "J.R.R. Tolkien", "stock": 8},
            {"title": "Da Vinci Şifresi", "author": "Dan Brown", "stock": 20},
            {"title": "1984", "author": "George Orwell", "stock": 30},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "stock": 4},
            {"title": "Bülbülü Öldürmek", "author": "Harper Lee", "stock": 6},
            {"title": "Don Quijote", "author": "Miguel de Cervantes", "stock": 6},
            {"title": "Suç ve Ceza", "author": "Fyodor Dostoyevski", "stock": 13},
            {"title": "Sefiller", "author": "Victor Hugo", "stock": 17},
            {"title": "Dorian Gray'in Portresi", "author": "Oscar Wilde", "stock": 18},
            {"title": "Oniki Levha", "author": "Anton Çehov", "stock": 3},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "stock": 44},
            {"title": "Savaş ve Barış", "author": "Lev Tolstoy", "stock": 30},
            {"title": "Jane Eyre", "author": "Charlotte Brontë", "stock": 8},
            {"title": "Ulysses", "author": "James Joyce", "stock": 19},
            {"title": "Romeo ve Juliet", "author": "William Shakespeare", "stock": 22},
            {"title": "Martı", "author": "Anton Çehov", "stock": 5},
            {"title": "Moby Dick", "author": "Herman Melville", "stock": 11},
            {"title": "Prens", "author": "Niccolò Machiavelli", "stock": 19},
            {"title": "İnce Mehmed", "author": "Halit Ziya Uşaklıgil", "stock": 10},
            {"title": "Kuyucaklı Yusuf", "author": "Sabahattin Ali", "stock": 15},
            {"title": "Sineklerin Tanrısı", "author": "Ahmet Ümit", "stock": 8},
            {"title": "İstanbul Hatırası", "author": "Ahmet Ümit", "stock": 20},
            {"title": "Beyaz Gemi", "author": "Cengiz Aytmatov", "stock": 12},
            {"title": "Aşk-ı Memnu", "author": "Halit Ziya Uşaklıgil", "stock": 7},
            {"title": "Fatih-Harbiye", "author": "Peyami Safa", "stock": 5},
            {"title": "Kürk Mantolu Madonna", "author": "Sabahattin Ali", "stock": 9},
            {"title": "İnci", "author": "John Steinbeck", "stock": 14},
            {"title": "Bir İdam Mahkûmunun Son Günü", "author": "Victor Hugo", "stock": 11},
            {"title": "Çalıkuşu", "author": "Reşat Nuri Güntekin", "stock": 8},
            {"title": "Kardeşimin Hikayesi", "author": "Zülfü Livaneli", "stock": 6},
            {"title": "Baba ve Piç", "author": "Zülfü Livaneli", "stock": 10},
            {"title": "Bir Gün", "author": "David Nicholls", "stock": 15},
            {"title": "Sırça Köşk", "author": "Sabahattin Ali", "stock": 20},
            {"title": "Dönüşüm", "author": "Franz Kafka", "stock": 25},
            {"title": "Uçurtma Avcısı", "author": "Khaled Hosseini", "stock": 30},
            {"title": "Beyhude", "author": "Halit Ziya Uşaklıgil", "stock": 8},
            {"title": "Fareler ve İnsanlar", "author": "John Steinbeck", "stock": 18},
            {"title": "Sefiller", "author": "Victor Hugo", "stock": 22},
            {"title": "Kumarbaz", "author": "Fyodor Dostoyevski", "stock": 12},
            {"title": "Bir Delinin Hatıra Defteri", "author": "Nikolai Gogol", "stock": 15},
            {"title": "Dracula", "author": "Bram Stoker", "stock": 20},
            {"title": "Küçük Kara Balık", "author": "Samed Behrengi", "stock": 10},
            {"title": "Simru", "author": "Halit Ziya Uşaklıgil", "stock": 5},
            {"title": "İstanbul'un Altınları", "author": "Sait Faik Abasıyanık", "stock": 13},
            {"title": "Cevdet Bey ve Oğulları", "author": "Orhan Pamuk", "stock": 17},
            {"title": "Köle", "author": "Isaac Bashevis Singer", "stock": 9},
            {"title": "Ölü Canlar", "author": "Nikolai Gogol", "stock": 14},
            {"title": "Eylül", "author": "Mehmet Rauf", "stock": 11},
            {"title": "Küçük Prens", "author": "Antoine de Saint-Exupéry", "stock": 10},
            {"title": "Harry Potter", "author": "J.K. Rowling", "stock": 15},
            {"title": "Yüzüklerin Efendisi", "author": "J.R.R. Tolkien", "stock": 8},
            {"title": "Da Vinci Şifresi", "author": "Dan Brown", "stock": 20},
            {"title": "1984", "author": "George Orwell", "stock": 30},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "stock": 4},
            {"title": "Bülbülü Öldürmek", "author": "Harper Lee", "stock": 6},
            {"title": "Don Quijote", "author": "Miguel de Cervantes", "stock": 6},
            {"title": "Suç ve Ceza", "author": "Fyodor Dostoyevski", "stock": 13},
            {"title": "Sefiller", "author": "Victor Hugo", "stock": 17},
            {"title": "Dorian Gray'in Portresi", "author": "Oscar Wilde", "stock": 18},
            {"title": "Oniki Levha", "author": "Anton Çehov", "stock": 3},
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "stock": 44},
            {"title": "Savaş ve Barış", "author": "Lev Tolstoy", "stock": 30},
            {"title": "Jane Eyre", "author": "Charlotte Brontë", "stock": 8},
            {"title": "Ulysses", "author": "James Joyce", "stock": 19},
            {"title": "Romeo ve Juliet", "author": "William Shakespeare", "stock": 22},
            {"title": "Martı", "author": "Anton Çehov", "stock": 5},
            {"title": "Moby Dick", "author": "Herman Melville", "stock": 11},
            {"title": "Prens", "author": "Niccolò Machiavelli", "stock": 19},
            
            
            
  
]

# Kütüphaneci Arayüzü Değişkenleri
librarian_window = None
new_title_entry = None
new_author_entry = None
new_stock_entry = None

# Kitap İşlemleri Fonksiyonları
def update_book_listbox(listbox, books):
    listbox.delete(0, tk.END)
    for book in books:
        listbox.insert(tk.END, f"{book['title']} - Stok: {book['stock']}")

def delete_book(title, listbox):
    global available_books
    for book in available_books:
        if book["title"] == title:
            available_books.remove(book)
            update_book_listbox(listbox, available_books)
            update_book_listbox(book_listbox, available_books)
            messagebox.showinfo("Bilgi", f"{title} kitabı kütüphaneden ve mevcut kitaplar listesinden silindi.")
            break
    else:
        messagebox.showwarning("Uyarı", f"{title} kitabı bulunamadı.")

def add_book(listbox):
    new_title = new_title_entry.get()
    new_author = new_author_entry.get()
    new_stock = int(new_stock_entry.get())

    available_books.append({"title": new_title, "author": new_author, "stock": new_stock})
    update_book_listbox(listbox, available_books)
    update_book_listbox(book_listbox, available_books)
    messagebox.showinfo("Bilgi", f"{new_title} kitabı kütüphaneye ve mevcut kitaplar listesine eklendi.")

def librarian_interface():
    global librarian_window, new_title_entry, new_author_entry, new_stock_entry

    librarian_window = tk.Toplevel(app)
    librarian_window.title("Kütüphaneci Paneli")
    librarian_window.geometry("600x400")  # Genişletilmiş pencere boyutu
    librarian_window.configure(bg="#013220")

    tk.Label(librarian_window, text="Mevcut Kitaplar", bg="#013220", fg="white").grid(row=0, column=0, pady=10)
    librarian_listbox = tk.Listbox(librarian_window, selectmode=tk.SINGLE, bg="#013220", fg="white", width=50)
    update_book_listbox(librarian_listbox, available_books)
    librarian_listbox.grid(row=1, column=0, padx=20, pady=10, rowspan=8)  # Genişletilmiş listbox

    tk.Label(librarian_window, text="Kitap Sil", bg="#013220", fg="white").grid(row=2, column=1, pady=10)
    tk.Label(librarian_window, text="Kitap Adı:", bg="#013220", fg="white").grid(row=3, column=1)
    delete_title_entry = tk.Entry(librarian_window, bg="#013220", fg="white")
    delete_title_entry.grid(row=3, column=2)

    delete_button = tk.Button(librarian_window, text="Kitap Sil", command=lambda: delete_book(delete_title_entry.get(), librarian_listbox), bg="#013220", fg="white")
    delete_button.grid(row=4, column=1, pady=10)

    tk.Label(librarian_window, text="Yeni Kitap Ekle", bg="#013220", fg="white").grid(row=5, column=1, pady=10)
    tk.Label(librarian_window, text="Kitap Adı:", bg="#013220", fg="white").grid(row=6, column=1)
    new_title_entry = tk.Entry(librarian_window, bg="#013220", fg="white")
    new_title_entry.grid(row=6, column=2)

    tk.Label(librarian_window, text="Yazar:", bg="#013220", fg="white").grid(row=7, column=1)
    new_author_entry = tk.Entry(librarian_window, bg="#013220", fg="white")
    new_author_entry.grid(row=7, column=2)

    tk.Label(librarian_window, text="Stok Sayısı:", bg="#013220", fg="white").grid(row=8, column=1)
    new_stock_entry = tk.Entry(librarian_window, bg="#013220", fg="white")
    new_stock_entry.grid(row=8, column=2)

    add_button = tk.Button(librarian_window, text="Kitap Ekle", command=lambda: add_book(librarian_listbox), bg="#013220", fg="white")
    add_button.grid(row=9, column=1, pady=10)

def borrow_return_book(is_borrow, listbox):
    student_name = student_name_entry.get()
    student_id = student_id_entry.get()
    selected_book = listbox.get(tk.ACTIVE)

    if not selected_book:
        messagebox.showwarning("Uyarı", "Lütfen bir kitap seçin.")
        return

    for book in available_books:
        if book["title"] in selected_book:
            if is_borrow:
                if book["stock"] > 0:
                    book["stock"] -= 1
                else:
                    messagebox.showwarning("Uyarı", f"{book['title']} stokta bulunmuyor.")
                    return

                borrowed_books.append({
                    'student_name': student_name,
                    'student_id': student_id,
                    'book_name': book['title'],
                    'author': book['author']
                })

                display_info()
                messagebox.showinfo("Bilgi", f"{student_name}, {book['title']} kitabını ödünç aldı.")
                break
            else:
                for borrowed_book in borrowed_books:
                    if borrowed_book['student_name'] == student_name and borrowed_book['book_name'] == book["title"]:
                        book['stock'] += 1
                        borrowed_books.remove(borrowed_book)
                        display_info()
                        messagebox.showinfo("Bilgi", f"{student_name}, {book['title']} kitabını geri getirdi.")
                        break
                else:
                    messagebox.showwarning("Uyarı", f"{student_name}, {book['title']} kitabını ödünç almadı veya başkasının aldığı bir kitabı geri getirmeye çalıştı.")
                break

def display_info():
    info_text.delete(1.0, tk.END)
    for borrowed_book in borrowed_books:
        info_text.insert(tk.END, f"{borrowed_book['student_name']} {borrowed_book['student_id']} "
                                   f"{borrowed_book['author']}'dan {borrowed_book['book_name']} kitabını aldı.\n")

# Ana Uygulama Arayüzü
app = tk.Tk()
app.title("Kütüphane Yönetim Sistemi")
app.geometry("800x600")  # Genişletilmiş pencere boyutu
app.configure(bg="#013220")

# Öğrenci Bilgileri Arayüzü
student_frame = tk.Frame(app, bg="#013220")
student_frame.pack(pady=10)

tk.Label(student_frame, text="Öğrenci Adı:", bg="#013220", fg="white").grid(row=0, column=0)
student_name_entry = tk.Entry(student_frame, bg="#013220", fg="white")
student_name_entry.grid(row=0, column=1)

tk.Label(student_frame, text="Öğrenci ID:", bg="#013220", fg="white").grid(row=1, column=0)
student_id_entry = tk.Entry(student_frame, bg="#013220", fg="white")
student_id_entry.grid(row=1, column=1)

# Kitap Bilgileri Arayüzü
book_frame = tk.Frame(app, bg="#013220")
book_frame.pack(pady=10)

tk.Label(book_frame, text="Mevcut Kitaplar:", bg="#013220", fg="white").grid(row=0, column=0)
book_listbox = tk.Listbox(book_frame, selectmode=tk.MULTIPLE, bg="#013220", fg="white", width=50)
for book in available_books:
    book_listbox.insert(tk.END, f"{book['title']} - Stok: {book['stock']}")
book_listbox.grid(row=0, column=1, padx=20)

# Kitap İşlemleri Butonları
borrow_button = tk.Button(app, text="Kitap Ödünç Al", command=lambda: borrow_return_book(True, book_listbox), bg="#013220", fg="white")
borrow_button.pack(pady=5)

return_button = tk.Button(app, text="Kitap Geri Getir", command=lambda: borrow_return_book(False, book_listbox), bg="#013220", fg="white")
return_button.pack(pady=5)

# Bilgileri Gösterme Alanı
info_text = tk.Text(app, height=10, width=50, bg="#013220", fg="white")
info_text.pack(pady=10)

# Kütüphaneci Arayüzü Butonu
librarian_button = tk.Button(app, text="Kütüphaneci Paneli", command=librarian_interface, bg="#013220", fg="white")
librarian_button.pack(pady=10)

app.mainloop()
