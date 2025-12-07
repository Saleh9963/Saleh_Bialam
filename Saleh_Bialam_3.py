# شرط ها و حلقه ها در پایتون

# شر طها و دستورات

# دستور if ساده

a = 33
b = 200

if b > a:
    print("b is greater than a")

# -----------------------------------

# تورفتگی

# پایتون برای تعریف محدوده کد به تورفتگی )فضای خالی در ابتدای خط( متکی است.

a = 33
b = 200

if b > a:
    print("b is greater than a")

# -----------------------------------

# دستور elif

# کلمه کلیدی elif در پایتون به این صورت است که میگوید اگر شرایط قبلی درست نبود این شرط را امتحان کن

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# -----------------------------------

# دستور else

# کلمه کلیدی else هر چیزی را که توسط شرایط قبلی گرفته نشده است، م یگیرد.

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# -----------------------------------

# همچنین می توان else را بدون elif داشته باشید:

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# -----------------------------------

# کلمه کلیدی and یک عملگر منطقی است و برای ترکیب عبارات شرطی استفاده م یشود:

a = 200
b = 33
c = 500

if a > b and c > a:
    print("Both conditions are True")

# -----------------------------------

# کلمه کلیدی or یک عملگر منطقی است و برای ترکیب عبارات شرطی استفاده م یشود:

a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")

# -----------------------------------

#: کلمه کلیدی not یک عملگر منطقی است و برای معکوس کردن نتیجه عبارت شرطی استفاده می شود:

a = 33
b = 200

if not a > b:
    print("a is NOT greater than b")

# -----------------------------------

# IF تو در تو

# شما می توانید دستورات if را درون دستورات if دیگر داشته باشید، به این حالت دستورات if تو در تو م یگویند .

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# -----------------------------------

# شر طهای ترکیبی با عملگرهای منطقی

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# -----------------------------------

# دستورات انتخاب

# دستور match برای انجام اقدامات مختلف بر اساس شرایط مختلف استفاده م یشود

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# -----------------------------------

# اگر می خواهید یک بلوک کد زمانی که هیچ تطابق دیگری وجود ندارد اجرا شود، از کاراکتر زیرخط _ به عنوان آخرین مقدار case استفاده کنید:

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

# -----------------------------------

# می توانید در ارزیابی case از if ، به عنوان یک بررسی شرط اضافی، دستوراتی اضافه کنید

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

# -----------------------------------

# حلقه While

# با حلقه while می توانیم مجموع های از دستورات را تا زمانی که یک شرط درست باشد، اجرا کنیم.

i = 1
while i < 6:
    print(i)
    i += 1

# -----------------------------------

# با دستور break می توانیم حلقه را حتی اگر شرط while درست باشد، متوقف کنیم:

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# -----------------------------------

# با استفاده از دستور continue می توانیم تکرار فعلی را متوقف کنیم و تکرار بعدی را ادامه دهیم:

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# -----------------------------------

# دستور else در حلقه

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# -----------------------------------

# حلقه for

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# -----------------------------------

# با استفاده از دستور break می توانیم حلقه را قبل از اینکه تمام آیتم ها را پیمایش کند، متوقف کنیم:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# -----

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
