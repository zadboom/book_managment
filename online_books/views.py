from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Book, Category, UserProfile
from .forms import CustomLoginForm,CustomSignupForm,BookForm  # فرم سفارشی با برچسب‌های فارسی
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# ثبت‌نام کاربر
def signup_view(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ورود خودکار پس از ثبت‌نام
            return redirect('book_list')
    else:
        form = CustomSignupForm()
    
    context = {
        'form': form
    }
    return render(request, 'online_books/signup.html', context)
# ورود کاربر
def login_view(request):
    if request.method == "POST":
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')  # بعد از ورود، به لیست کتاب‌ها می‌رود
    else:
        form = CustomLoginForm()
    
    context = {
        'form': form
    }
    return render(request, 'online_books/login.html', context)
# خروج کاربر
def logout_view(request):
    logout(request)
    return redirect('login')

# لیست کتاب‌ها + فیلتر دسته‌بندی
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Book, Category, UserProfile

# لیست کتاب‌ها + فیلتر دسته‌بندی
@login_required(login_url='login')
def book_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()   # همه دسته‌بندی‌ها برای نمایش در دراپ‌داون

    query = request.GET.get('q')                 # فیلتر بر اساس عنوان یا نویسنده
    min_price = request.GET.get('min_price')     # قیمت حداقل
    max_price = request.GET.get('max_price')     # قیمت حداکثر
    category_id = request.GET.get('category')    # دسته‌بندی انتخابی

    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    if min_price:
        books = books.filter(price__gte=min_price)

    if max_price:
        books = books.filter(price__lte=max_price)

    if category_id and category_id.isdigit():  # اگر دسته‌بندی انتخاب شده بود
        books = books.filter(category_id=category_id)

    context = {
        'books': books,
        'categories': categories,        # برای نمایش در HTML
        'selected_category': category_id # برای انتخاب پیش‌فرض در دراپ‌داون
    }
    return render(request, 'online_books/book_list.html', context)


# افزودن کتاب
@login_required(login_url='login')   # اگر لاگین نکرده باشه، به صفحه لاگین هدایت میشه
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'online_books/add_book.html', {'form': form})

# ویرایش کتاب
@login_required(login_url='login')   # اگر لاگین نکرده باشه، به صفحه لاگین هدایت میشه
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'online_books/edit_book.html', {'form': form, 'book': book})

# حذف کتاب
@login_required(login_url='login')   # اگر لاگین نکرده باشه، به صفحه لاگین هدایت میشه
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

# افزودن یا حذف کتاب به علاقه‌مندی‌ها

def toggle_favorite(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    user = request.user

    # ایجاد UserProfile در صورت نبود
    profile, created = UserProfile.objects.get_or_create(user=user)

    if book in profile.favorite_books.all():
        profile.favorite_books.remove(book)
    else:
        profile.favorite_books.add(book)
    return redirect('book_list')

