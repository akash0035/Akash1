a=5
b=25
c=50
d='gugan'
e='pooj'
print(a+b+c)
print((a+b)*c)
print(((c-a)*b)/c)
print(d+e)
while a<=25:
    print('gugan loves pooja...')
    a=a+1
else:
        print("done")
while a<=5:
    print('gugan')
    a=a+1
else:
 print('end')
i=1
for i in range(i<=a):
    print('143')
    i=i+1
else:
    print('end')
a = int(input("Enter a Number: "))


if a%2 == 0:

            print("Number is even ")

elif a%2 != 0:

         print("Number is odd")

else:

       print("invalid")

def recurse(n):
    if n == 5:
        return
    else:
        recurse(n + 1)

try:
    ...
except SomeException:
    tb = sys.exc_info()[2]
    raise OtherException(...).with_traceback(tb)

