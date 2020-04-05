
largest = None
smallest = None
"""
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        ival = int(num)
    except:
        print ("Invalid input")
        continue

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

    if largest is None:
        largest = num
    elif num > largest:
        largest = num


def done(largest,smallest):
    print ("Maximum is", largest)
    print ("Minimum is", smallest)

done(largest,smallest)
"""


# try block to handle the exception

my_list = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        intval = int(num)
        my_list.append(intval)
        # if input is not-integer, just print the list
    except:
        print("Invalid input")
        continue

print("Maximum is", max(my_list))
print("Minimum is", min(my_list))
