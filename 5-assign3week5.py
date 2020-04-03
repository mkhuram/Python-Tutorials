hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, Please enter numeric input.")
    quit()

print(h, r)
if(h <= 40):
    print("Your pay is:",h * r)
elif(h > 40):
    overtime = h - 40
    h = 40
    overtimepay = r * 1.50
    print(h * r + overtime * overtimepay)
