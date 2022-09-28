año = int(input("escribe el año: "))

if año % 4 == 0:
    if año % 100 != 0:
        print("año bisiesto")
    elif año % 400 == 0:
        print("año bisiesto")
    else:
        print("año no bisiesto")
else:
    print("año no bisiesto")
 
