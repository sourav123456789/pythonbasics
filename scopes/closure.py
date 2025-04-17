# x = 88
#
#
# def f1():
#     x = 12
#
#     def f2():
#         print(x)
#
#     return f2
#
# res = f1()
# res()
#

def chai_aur_code(num):
    def actual(x):
        return x ** num
    return actual

f1 = chai_aur_code(2)
f2 = chai_aur_code(3)

print(f1(3))
print(f2(3))
