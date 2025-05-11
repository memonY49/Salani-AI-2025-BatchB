
import math
class Number:
    def __init__(self,num):
        self.num = num
    def __repr__(self):
        return str(self.num)
    def __add__(self, other):
        return Number(self.num+other)
    def __sub__(self, other):
        return Number(self.num - other)
    def __mul__(self, other):
        return Number(self.num * other.num)
    def __truediv__(self, other):
        return Number(self.num / other.num)
    def __mod__(self, other):
        return Number(self.num % other.num)
    def __round__(self, n=None):
        return round(self.num)
    def __rsub__(self, other):
        return Number(other - self.num)


n1 = Number(4.893)

print(n1+500)

class book:
    def __init__(self, title, pages, auther):
        self.title = title
        self.pages = pages
        self.auther = auther
    def __repr__(self):
        return f"Book Title: {self.title}\nAuther: {self.auther}"
    def __len__(self):
        return int(self.pages)
    def __add__(self, other):
        return f"{self.title} and {other.title}"
    def __del__(self):
        print(f"The Book :{self.title} is deleted")

# book1 = book("SMIT",200,"Yasir Nawaz")
# # book2 = book("SMIT2",500,"Yasir Nawaz")
# #
# print(len(book1))

# del book1

# print(book1)


