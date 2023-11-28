from collections import Counter

txt = input("Enter txt:").replace(" ","")

for key, value in Counter(txt).items():
    print(f"{key} - {value} time(s)")
