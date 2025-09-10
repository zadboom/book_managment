# 📚 Online Library / کتابخانه آنلاین

این پروژه یک کتابخانه آنلاین است که با **Django** و **Tailwind CSS** ساخته شده است.  
کاربران می‌توانند ثبت‌نام و ورود کنند، کتاب اضافه کنند، و کتاب‌ها را بر اساس دسته‌بندی، قیمت یا نویسنده فیلتر کنند.  

This project is an online library built with **Django** and **Tailwind CSS**.  
Users can sign up, log in, add books, and filter them by category, price, or author.

---

## ویژگی‌ها / Features
- ثبت‌نام و ورود کاربر / User signup & login
- افزودن، ویرایش و حذف کتاب / Add, edit, and delete books
- دسته‌بندی کتاب‌ها / Book categories
- جستجو و فیلتر بر اساس عنوان، نویسنده، قیمت و دسته‌بندی / Search and filter by title, author, price, and category
- افزودن کتاب به علاقه‌مندی‌ها / Add books to favorites
- طراحی زیبا با Tailwind CSS / Styled with Tailwind CSS

---

## پیش‌نیازها / Requirements
- Python >= 3.10
- Django >= 5.2
- Node.js و npm (برای Tailwind) / Node.js & npm (for Tailwind)

---

## نصب پروژه / Installation

### 1. کلون کردن پروژه / Clone the repository:
```bash
git clone https://github.com/username/bookmanagement.git
cd bookmanagement

### 2.ساخت virtualenv و فعال‌سازی / Create and activate virtual environment:
python -m venv venv
# ویندوز / Windows
venv\Scripts\activate
# لینوکس / مک / Linux / Mac
source venv/bin/activate
3. نصب وابستگی‌ها / Install dependencies:
pip install -r requirements.txt

4. مهاجرت دیتابیس / Apply database migrations:
python manage.py migrate
5. نصب Tailwind CSS / Install Tailwind CSS:
npm install
npm run build
6. اجرای سرور توسعه / Run development server:
python manage.py runserver
سپس به آدرس / Then go to: http://127.0.0.1:8000/books/

فایل‌های مهم / Important Files

bookmanagement/online_books/models.py → مدل‌های Book، Category و UserProfile / Models: Book, Category & UserProfile

bookmanagement/online_books/forms.py → فرم‌ها (Django + Tailwind) / Forms (Django + Tailwind)

bookmanagement/online_books/views.py → منطق اپلیکیشن / Application logic

bookmanagement/online_books/templates/online_books/ → قالب‌ها / Templates

مشارکت / Contributing

اگر می‌خواهید مشارکت کنید / If you want to contribute:

پروژه را فورک کنید / Fork the project

تغییرات خود را اعمال کنید / Make your changes

Pull Request ارسال کنید / Submit a Pull Request

bookmanagement/online_books/static/css/output.css → CSS تولید شده توسط Tailwind / Tailwind generated CSS
