# 📚 Book Management Project  

This project is a simple **Library/Book Management System** built with Python and Django.  
It allows users to manage books, authors, and related information.  

---

## 🚀 Installation and Setup  

### 1. Clone the Repository  
```bash
git clone https://github.com/your-username/bookmanagement.git
cd bookmanagement
```

### 2. Create a Virtual Environment  
(Recommended to avoid conflicts)  
```bash
python -m venv venv
```

Activate the virtual environment:  

- **Windows**  
```bash
venv\Scripts\activate
```

- **Linux / Mac**  
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

---

### 4. Database Migration  
```bash
python manage.py migrate
```

---

### 5. Create Superuser (Admin Access)  
```bash
python manage.py createsuperuser
```
👉 Follow the instructions to set **username, email, and password**.  

---

### 6. Run the Development Server  
```bash
python manage.py runserver
```

Now open your browser and go to:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 🛠 Features  
- Add / Edit / Delete Books  
- Manage Authors  
- Search Functionality  
- Django Admin Panel  

---

## 📄 Requirements  
- Python 3.10+  
- Django 5+  
- SQLite (default, no setup required)  

---

# 🌍 فارسی (راهنمای نصب و راه‌اندازی)  

### ۱. کلون کردن مخزن  
```bash
git clone https://github.com/your-username/bookmanagement.git
cd bookmanagement
```

### ۲. ساخت محیط مجازی  
```bash
python -m venv venv
```

فعال‌سازی:  

- **ویندوز** →  
```bash
venv\Scripts\activate
```

- **لینوکس / مک** →  
```bash
source venv/bin/activate
```

---

### ۳. نصب وابستگی‌ها  
```bash
pip install -r requirements.txt
```

---

### ۴. اجرای مهاجرت پایگاه داده  
```bash
python manage.py migrate
```

---

### ۵. ساخت کاربر ادمین  
```bash
python manage.py createsuperuser
```

---

### ۶. اجرای سرور  
```bash
python manage.py runserver
```

سپس مرورگر را باز کنید:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## ✨ امکانات  
- افزودن / ویرایش / حذف کتاب  
- مدیریت نویسندگان  
- قابلیت جستجو  
- دسترسی به پنل مدیریت جنگو  

---

## 📌 پیش‌نیازها  
- Python 3.10+  
- Django 5+  
- SQLite (به‌صورت پیش‌فرض نیاز به تنظیم ندارد)  
