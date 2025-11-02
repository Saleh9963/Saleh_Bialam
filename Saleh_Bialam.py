# print() متغیر ها و دستور

x = 5
y = "John"
print(x)
print(y)

# -----------------------------------

# متغیر ها نیازی به تعریف نوع خاصی ندارند و حتی میتوانند پس از تنظیم نوع خود را تغییر دهند

x = 4             # x is of type int
x = "Sally"       # x is now of type str
print(x)

# -----------------------------------

# ریخته گری (casting)

x = str(3)          # x will be '3'
y = int(3)          # y will be 3
z = float(3)        # z will be 3.0
print(x)
print(y)
print(z)

# -----------------------------------

# برای به دست آوردن نوع داده type() تابع

x = 5
y = "John"
z = 7j
print(type(x))
print(type(y))
print(type(z))

# -----------------------------------

# متغیر های رشته ای را میتوان با استفاده از علامت نقل قول تکی یا دوتایی تعریف کرد

x = "John"
y = 'John'
print(x)
print(y)

# -----------------------------------

# حساس به حروف بزرگ و کوچک
a = 4
A = "Sally"
print(a)
print(A)

# -----------------------------------

# مقدار دهی برای چندین متغیر

x, y, z = "Orange", "Banana", "cherry"
print(x)
print(y)
print(z)

# -----------------------------------

# یک مقدار برای چندین متغیر

x = y = z = "Orange"
print(x)
print(y)
print(z)

# -----------------------------------

# (unpacking)باز کردن یک مجموعه

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# -----------------------------------

# خروجی دادن چندین متغیر

x = "python is awesome"
print(x)

# -----

x = "python"
y = "is"
z = "awesome"
print(x, y, z)

# -----

x = "python"
y = "is"
z = "awesome"
print(x + y + z)

# -----

x = 5
y = 10
print(x + y)

# -----

x = 5
y = "John"
print(x, y)

# -----------------------------------

# متغیر های سراسری و محلی

x = "awesome"


def myfunc():
    print("python is " + x)


myfunc()

# -----

x = "awesome"


def myfunc():
    x = "fantastic"
    print("python is " + x)


myfunc()

print("python is " + x)

# -----

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("python is " + x)

# -----------------------------------

# نوع داده

x = "Hello World"
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----

x = 20
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----

x = ["apple ", "banana ", "cherry"]
# display x:"
print(x)
# display the data type of x:
print(type(x))

# -----

x = frozenset({"apple", "banana", "cherry"})
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----------------------------------

# توابع سازنده

x = int(20)
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----

x = str("Hello World")
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----

x = list(("apple", "banana", "cherry"))
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----

x = bool(5)
# display x:
print(x)
# display the data type of x:
print(type(x))

# -----------------------------------

# رشته های چند خطی

a = """Lorem ipsum dolor sit amet
consectetur adipiscing elit, sed do
eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# -----

a = '''Lorem ipsum dolor sit amet
consectetur adipiscing elit, sed do
eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# -----------------------------------

# رشته ها آرایه هستند

a = "Hello, World!"
print(a[1])

# -----------------------------------

# پیمایش با استفاده از حلقه

for x in "banana":
    print(x)

# -----------------------------------

# len() به دست آوردن طول رشته با استفاده از تابع

a = "Hello, World!"
print(len(a))

# -----------------------------------

# بررسی رشته

txt = "the best things in life are free!"
print("free" in txt)

# -----------------------------------

# Slicing Strings

b = "Hello, World!"
print(b[2:5])

# -----

b = "Hello, World!"
print(b[:5])

# -----

b = "Hello, World!"
print(b[2:])

# -----

b = "Hello, World!"
print(b[-5:-2])

# -----------------------------------

# Modify Strings

a = "Hello, World!"
print(a.upper())

# -----

a = "Hello, World!"
print(a.lower())

# -----

a = "Hello, World!"
print(a.strip())

# -----

a = "Hello, World!"
print(a.replace("H", "J"))

# -----

a = "Hello, World!"
b = a.split(",")
print(b)

# -----------------------------------

# String Concatenation

a = "Hello"
b = "World"
c = a + b
print(c)

# -----

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# -----------------------------------

# قالب بندی در رشته ها

age = 36
txt = f"My name is John, I am {age}"
print(txt)

# -----

price = 59
txt = f"The price is {price} dollars"
print(txt)

# -----

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# -----

txt = f"The price is {20 * 59} dollars"
print(txt)

# -----

name = "Alice"
age = 30
greeting = f"Hello, I'm {name} and I'm {age} years old."
print(greeting)

# -----

x = 10
y = 20
result = f"The sum of {x} and {y} is {x + y}."
print(result)

# -----------------------------------

# Escape Character

txt = 'It\'s alright.'
print(txt)

# -----

txt = "This will insert one \\(backslash)."
print(txt)

# -----

txt = "Hello\nWorld!"
print(txt)

# -----

txt = "Hello\tWorld!"
print(txt)

# -----

txt = "Hello \bWorld!"
print(txt)

# -----

txt = "Hello\rWorld!"
print(txt)

# -----------------------------------

# بولین های پایتون

print(10 > 9)
print(10 == 9)
print(10 < 9)

# -----

x = 200
print(isinstance(x, int))

# -----

a = 200
b = 33
if b > a:
    print("b is not greater than a")
else:
    print("b is not greater than a")

# -----------------------------------

# عملگر های حسابی پایتون

x = 5
y = 3
print(x + y)

# -----

x = 12
y = 3
print(x / y)

# -----

x = 15
y = 2
print(x // y)

# -----

x = 5
y = 3
print(x-y)

# -----

x = 5
y = 3
print(x * y)

# -----

x = 2
y = 5
print(x ** y)

# -----------------------------------

# عملگر های انتساب پایتون

x = 5
print(x)

# -----

x = 5
x += 3
print(x)

# -----

x = 5
x %= 3
print(x)

# -----

x = 5
x **= 3
print(x)

# -----------------------------------

# عملگرهای مقایسه ای پایتون

x = 5
y = 3
print(x == y)

# -----

x = 5
y = 3
print(x != y)

# -----

x = 5
y = 3
print(x >= y)

# -----------------------------------

# عملگرهای منطقی پایتون

x = 5

print(x > 3 and x < 10)

# -----

x = 5

print(x > 3 or x < 4)

# -----

x = 5

print(not (x > 3 and x < 10))

# -----------------------------------

# عملگرهای هویت پایتون

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# -----

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)

# -----------------------------------

# عملگرهای عضویت پایتون

x = ["apple", "banana"]
print("banana" in x)

# -----

x = ["apple", "banana"]
print("pineapple" not in x)

# -----------------------------------

# عملگرهای بیتی پایتون

print(6 & 3)

# -----

print(6 | 3)

# -----------------------------------

# اولویت عملگرها

print((6 + 3)-(6 + 3))
