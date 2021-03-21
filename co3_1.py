import platform
x = platform.system()
print(x)
print()
x = dir(platform)
print(x)
print()
import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))