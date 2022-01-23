hm = {}

def check(req):
    # insert data
    if hm.get(req["ip"], None) is None: # nice to show
        hm[req["ip"]] = []
    hm[req["ip"]].append(req["dt"])

    # slice the list ....
    while hm[req["ip"]][0] < req["dt"] - 6000:
        hm[req["ip"]] = hm[req["ip"]][1:]

    # check the condition
    if len(hm[req["ip"]]) >= 1000:
        # prevent additional requests
        return


if __name__ == "__main__":
    req = {
        "ip" : "127.0.0.1",
        "dt" : 1
    }
    check(req)

# python3 limit_req.py

# Luca notes in terminal

# python3 
# Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a = [1,2,3,4,5]
# >>> a[0]
# 1
# >>> a[-1]
# 5
# >>> a[2:4]
# [3, 4]
# >>> a[2:-1]
# [3, 4]
# >>> a[2:]
# [3, 4, 5]
# >>> a[::-1]
# [5, 4, 3, 2, 1]
# >>> a[:]
# [1, 2, 3, 4, 5]

# more notes on the above

# >>> a
# [1, 2, 3, 4, 5]
# >>> a = a[1:]
# >>> a
# [2, 3, 4, 5]
# >>> a = a[1:]
# >>> a
# [3, 4, 5]
# >>> a = a[1:]
# >>> a
# [4, 5]
# >>> a = a[1:]\
# ... 
# >>> 
# >>> a
# [5]
# >>> a = a[1:]
# >>> a
# []
# >>> a[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range

# our hm[req["ip"]].append(req["dt"]) line will ensure that the above never happens

# cool things in Python

# python3
# Python 3.8.10 (default, Nov 26 2021, 20:14:08) 
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a = 5
# >>> def f(x):
# ...     x = x + 1
# ... 
# >>> f(a)
# >>> a
# 5
# >>> b = [5]
# >>> f(*b)
# >>> 
# >>> def f1(a, b):
# ...     print(a)
# ...     print(b)
# ... 
# >>> c = [1, 2]
# >>> f1(*c)
# 1
# 2
# >>> c = [1, 2]
# >>> c
# [1, 2]
# >>> [ i for i in c ]
# [1, 2]
# >>> [ i+1 for i in c ]
# [2, 3]
# >>> [ i**2 for i in c ]
# [1, 4]