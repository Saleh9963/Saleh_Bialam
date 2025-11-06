# متد های لیست

# یک عنصر را به انتهای لیست اضافه می کندappend() متد

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

# -----

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

# تمام عناصر یک لیست را حذف میکندclear() متد

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

# متد copy() یک کپی از لیست مشخص شده را برمیگرداند.

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

# متد count() تعداد شمارش عناصر با مقدار مشخص شده را برم یگرداند

fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

# -----

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

# متد extend() عناصر لیست مشخص شده )یا هر عنصر تکرارشونده( را به انتهای لیست فعلی اضافه م یکند.

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

# متد index() موقعیت اولین وقوع مقدار مشخص شده را برم یگرداند.

fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

# -----

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index("cherry", 4)
print(x)

# متد insert() مقدار مشخص شده را در موقعیت مشخص شده درج م یکند

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

# متد pop() عنصر را در موقعیت مشخص شده حذف م یکند

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

# متد remove() اولین مورد از عنصری که مقدار مشخص شده را دارد، حذف م یکند

fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove("banana")
print(fruits)

# متد del این دستور می تونه یه آیتم خاص رو از لیست حذف کنه یا حتی کل لیست رو از حافظه پاک کند

my_list = [1, 2, 3]
del my_list[1]
# del my_list
print(my_list)

# متد reverse() ترتیب مرتب سازی عناصر را معکوس م یکند

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

# متد sort() به طور پی شفرض لیست را به صورت صعودی مرتب م یکند

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# ------------------------------------

# تاپل های پایتون

# وقتی می گوییم تاپل ها مرتب هستند، به این معنی است که آیتمها ترتیب مشخصی دارند و این ترتیب تغییر نخواهد کرد

thistuple = ("apple", "banana", "cherry")
print(thistuple)

# از آنجایی که تاپ لها اندی سگذاری شد هاند، می توانند آیتم هایی با مقادیر یکسان داشته باشند:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# می توان از سازنده ی tuple() برای ایجاد یک تاپل استفاده کرد.

thistuple = tuple(("apple", "banana", "cherry"))
# note the double round-brackets
print(thistuple)

# -----

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

# دسترسی به آیتم های تاپل با اندیس

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# -----

# thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# -----

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# -----

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# -----

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# ------------------------------------

# بررسی وجود یک آیتم در تاپل با کلمه کلیدی in

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# به روزرسانی تاپل ها

# تبدیل تاپل به یک لیست برای ایجاد تغییر

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# -----

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# -----

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# -----

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# ------------------------------------

# بسته بندی تاپل

fruits = ("apple", "banana", "cherry")
print(fruits)

# -----

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# استفاده از ستاره

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# -----

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# ------------------------------------

# پیمایش آیتم ها با حلقه for

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# -----

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

# ------------------------------------

# اتصال تاپل ها با عملگر +

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# -----

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# ------------------------------------

# متد های تاپل

# متد count() تعداد دفعاتی که یک مقدار مشخص شده در تاپل ظاهر می شود را برمی گرداند

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# متد index() اولین رخداد مقدار مشخص شده را پیدا می کند

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# ------------------------------------

# مجموعه های پایتون

thisset = {"apple", "banana", "cherry"}
print(thisset)

# سازنده set() برای ایجاد یک مجموعه

thisset = set(("apple", "banana", "cherry"))
# note the double round-brackets
print(thisset)

# -----

myset = {"apple", "banana", "cherry"}
print(type(myset))

# حلقه for  کلمه کیدی و in

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# برای اضافه کردن یک آیتم به یک مجموعه از متد add() استفاده کنید

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# برای اضافه کردن آیتم ها از یک مجموعه دیگر به مجموعه فعلی، از این متد update() استفاده کنید

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# -----

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

# برای حذف یک آیتم در یک مجموعه، از متد remove ، یا discard استفاده کنید.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# -----

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

# حذف تصادفی یک آیتم با pop()

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# متد clear() مجموعه را خالی م یکند:

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# پیمایش با for

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

# متد union() یک مجموعه جدید با تمام آیت مهای هر دو مجموعه را برم یگرداند

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# -----

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

# -----

x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)

# متد update() تمام آیت مهای یک مجموعه را در مجموعه دیگر درج م یکند. مجموعه اصلی را تغییر می دهد و مجموعه جدیدی را برنمیگرداند

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# متد intersection() یک مجموعه جدید برم یگرداند که فقط شامل آیت مهایی است که در هر دو مجموعه وجود دارند

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

# تابع frozenset() برای فریز کردن لیست و غیر قابل تغییر کردن آن

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

# ------------------------------------

# دیکشنریهای پایتون

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# -----

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# استفاده از dict() برای ساخت دیکشنری

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# شما می توانید با اشاره به نام کلید یک دیکشنری، داخل کروشه، به آیتم های آن دسترسی پیدا کنید:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

# روشی به نام get() وجود دارد که همان نتیجه را به شما می دهد

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.get("model")
print(x)

# متد keys() لیستی از تمام کلیدهای موجود در دیکشنری را برم یگرداند.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.keys()
print(x)

# یک آیتم جدید به دیکشنری اصلی اضافه کنید و ببینید که لیست کلیدها نیز ب هروزرسانی م یشود:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change
print(car)

# متد values() لیستی از تمام مقادیر موجود در دیکشنری را برم یگرداند

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.values()
print(x)

# متد items() هر آیتم را در یک دیکشنری، به عنوان تاپل در یک لیست، برم یگرداند

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)

# بررسی وجود کلید مشخص شده با کلمه in

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# متد update() ، دیکشنری را با آیت مهای موجود در آرگومان داده شده به روزرسانی م یکند

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# اضافه کردن یک آیتم به دیکشنری با استفاده از یک کلید اندیس جدید و اختصاص دادن یک مقدار به آن انجام م یشود:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# متد pop() ، آیتمی را که نام کلید مشخص شده را دارد، حذف م یکند

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# متد popitem آخرین آیتم درج شده را حذف می کند

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# کلمه کلیدی del ، آیتمی را که نام کلید مشخص شده را دارد، حذف م یکند:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# متد clear() ، دیکشنری را خالی م یکند:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# با استفاده از حلقه For می توانید در یک دیکشنری حلقه بزنید.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)

# -----

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(thisdict[x])

# -----

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x, thisdict[x])

# از متد values() برای برگرداندن مقادیر یک دیکشنری استفاده کنید:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.values():
    print(x)

# از متد keys() برای برگرداندن کلیدهای یک دیکشنری استفاده کنید:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict.keys():
    print(x)

# با استفاده از متد items() ، روی کلیدها و مقادیرحلقه بزنید:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x, y in thisdict.items():
    print(x, y)

# با استفاده از متد copy() ، یک کپی از دیکشنری تهیه کنید

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# راه دیگر برای ایجاد کپی، استفاده از متد dict است

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# دیکشنر یهای تو در تو

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

# -----

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# دسترسی به آیت مها در دیکشنر یهای تو در تو

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily["child2"]["name"])

# می توانید با استفاده از items() روی یک دیکشنری حلقه بزنید:

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
