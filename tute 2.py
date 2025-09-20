#problem 1
#check if a number is prime numer or odd
# ...existing code...

a = int(input("Enter a number: "))
if a % 2 == 0:
	print("this is an even number\nthank you")
else:
	print("this is an odd number\nthank you")



# ...existing code...
#sum 1 to 50 using while loop
#problem 2
#sum 1 to 50 using for loop
# ...existing code...
a=int(input("if you get second answer type :1 to 10:"))
yes="yes"
sum = 0
for i in range(1,51):
	sum = sum + i
	print(sum)
if sum==1275:
	pass
else:
	print("this is correct answer")


