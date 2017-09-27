#formula A=P(1+r//n)**(n*t)
p=10000
n=12
r=0.08
T= int(input("what are the years of investing?"))
t=float(T)
A=p*(1+r/n)**(n*t)
print(A)