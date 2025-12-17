# آرای ههای پایتون

# دسترسی به عناصر یک آرایه

import math
import array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

# ---------


# ایجاد آرایه از نوع عدد صحیح
arr = array.array('i', [1, 2, 3, 4])

arr.append(5)
arr[1] = 10

print(arr)

# --------------------------

# لیست و آرایه

# لیست
lst = [1, 2, 3]
lst.append(4)
print("LIST=", lst)

# آرایه
arr = array.array('i', [1, 2, 3])
arr.append(4)
print(arr)
# ایجاد آرایه از نوع عدد صحیح
arr = array.array('i', {1, 2, 3, 4})
arr.append(5)
arr[1] = 10
print(arr)

# ------------------------

# ورودی کاربر پایتون

# پایتون وقتی به تابع input() م یرسد ،اجرا را متوقف می کند و وقتی کاربر مقداری ورودی داد، ادامه می دهد

print("Enter your name:")
name = input()
print(f"Hello {name}")

# ----------------------

# ورود ی های چندگانه

name = input("Enter your name:")
print(f"Hello {name}")

fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")

print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# --------------------------

# شماره ورودی


x = input("Enter a number:")
# find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")

# ---------------------------

# اعتبارسنجی ورودی

y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")

# ------------------------

# try/except

try:
    print(x)
except:
    print("An exception occurred")

# -----------

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

    # ------------

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# ----------

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# --------------------

# ریاضی پایتون

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

# ---------

x = abs(-7.25)
print(x)

# ----------

x = pow(4, 3)
print(x)

# --------------------------

# ماژول ریاضی

x = math.sqrt(64)
print(x)

# ---------


x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # returns 2
print(y)  # returns 1
