import time
print(time.ctime())
import matplotlib.pyplot as plt
def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result
p = float(input("Enter the principal amount: "))
r = float(input("Enter the interest rate: "))
endyear = float(input("Enter the Year : "))
yearlist = []
pamountlist = []
interestlist = []
for i in range(int(endyear)):
    yearlist.append(i)
    amount = compound_interest(p, r, i)
    intamount = int(amount)
    pamountlist.append(intamount)
    interest = amount - p
    intins = int(interest)
    interestlist.append(intins)
print(yearlist)
print(pamountlist)
print(interestlist)
plt.plot(yearlist,pamountlist,interestlist)
plt.xlabel('years')
plt.ylabel('Principal Amount')
plt.show()