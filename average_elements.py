# #Command to run the code:
# #python3 error_handing.py

while True:

    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("Not a proper input. Please input a integer");

if((year % 4==0 and year % 100 !=0) or (year % 400 ==0)):
    print("Leap year")
else:
    print(" Not a Leap year")
