import sys
# # # class CustomException(Exception):
# # #     pass

# # # try:
# # #     raise CustomException("Aman caused error")
# # # except CustomException as e:
# # #     print("Error catched", e)

# # class A:
# #     def say(self):
# #         print("A")

# # class Aa(A):
# #     pass

# # class B:
# #     def say(self):
# #         print("B")

# # class Bb(A):
# #     pass

# # class C(Aa, Bb):
# #     pass

# # print(C.__mro__)

# import sys
# import dis

# dis.dis('a = [1, 2, 3]')
# # x = a
# # print(sys.getrefcount(a))
# # print(sys.getrefcount([1, 2, 3]))
a=5
b=5
c=5
d=5
print(sys.getrefcount(5))

import platform

print("getrefcount(5) =", sys.getrefcount(5))
print("implementation =", platform.python_implementation())
print("version =", sys.version)
print("architecture =", platform.architecture())