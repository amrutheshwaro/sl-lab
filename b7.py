from prettytable import PrettyTable

def ctoF(c):
    return ((c * 9 / 5) + 32)

def ftoC(f):
    return ((f - 32) * 5 / 9)

def cToK(c):
    return (c + 273.15)

def kToC(k):
    return (k - 273.15)

def fToK(f):
    return cToK(ftoC(f))

def kToF(k):
    return ctoF(kToC(k))

conversion_history = []
ch1 = 1
ch2 = 1
t = 0.0

print("1. CtoF\n", "2. FtoC\n", "3. CtoK\n", "4. KtoC\n", "5. FtoK\n", "6. KtoF\n", "7. Quit\n")
while (ch1 != 7):
    ch1 = int(input("Enter your conversion choice.\n"))
    if (ch1 == 1):
        t = float(input("Enter temperature in Celsius.\n"))
        k = ctoF(t)
        print("Temperature in Fahrenheit is", k)
        conversion_history.append((t, k, "CtoF"))
    elif (ch1 == 2):
        t = float(input("Enter temperature in Fahrenheit.\n"))
        k = ftoC(t)
        print("Temperature in Celsius is", k)
        conversion_history.append((t, k, "FtoC"))
    elif (ch1 == 3):
        t = float(input("Enter temperature in Celsius.\n"))
        k = cToK(t)
        print("Temperature in Kelvin is", k)
        conversion_history.append((t, k, "CtoK"))
    elif (ch1 == 4):
        t = float(input("Enter temperature in Kelvin.\n"))
        k = kToC(t)
        print("Temperature in Celsius is", k)
        conversion_history.append((t, k, "KtoC"))
    elif (ch1 == 5):
        t = float(input("Enter temperature in Fahrenheit.\n"))
        k = fToK(t)
        print("Temperature in Fahrenheit is", k)
        conversion_history.append((t, k, "FToK"))
    elif (ch1 == 6):
        t = float(input("Enter temperature in Kelvin.\n"))
        k = kToF(t)
        print("Temperature in Kelvin is", k)
        conversion_history.append((t, k, "KtoF"))
    elif (ch1 == 7):
        break
    else:
        print("Invalid choice entered.")
    conversion_history.sort(key=lambda x: x[0])
    ch2 = int(input("Enter 1 to view the coversion history.\n"))
    if (ch2 == 1):
        print(conversion_history)
    


