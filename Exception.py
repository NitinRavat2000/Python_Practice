a=5
b=0

try:
    print("resource open")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)




except ZeroDivisionError as e:
    print("not divided by zero",e)

except ValueError:
    print("invalid input")

except Exception:
    print("something went wrong")

finally:
    print("Resourse closed")