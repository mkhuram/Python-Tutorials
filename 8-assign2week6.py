hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, Please enter numeric input.")
    quit()

def computepay(h,r):
    if(h <= 40):
        return(h * r)
    elif(h > 40):
        overtime = h - 40
        h = 40
        overtimepay = r * 1.50
        return(h * r + overtime * overtimepay)


p = computepay(h,r)
print("Pay",p)
