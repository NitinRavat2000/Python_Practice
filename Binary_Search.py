pos = -1

def search(list,n):
    l=0
    u=len(list)+1

    while l<=u:
        mid=(l+u) // 2

        if list[mid]==n:
            globals() ['pos']= mid
            return True
        elif n > list[mid]:
                l=mid+1
        elif n < list[mid]:
                u=mid-1

        else:
            return False


list=[32,45,76,77,99,203,10010101010010101]
n=88

if search(list,n):
    print("Found",pos+1)
else:
    print("not found")