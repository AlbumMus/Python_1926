a = 56982
sec = a % 60
hour = a // 3600
min = a // 60 - hour * 60
print(f"{hour:02}:{min:02}:{sec:02}")