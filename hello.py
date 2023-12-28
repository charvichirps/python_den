print("hello")

#get number of elements in the list without using the function len:
my_list = [10, 25, 32, 4, 5]

count = 0
for n in my_list:
    count += 1

print("Number of elements in the list:", count)


#python program for finding the sum of the numbers in the list



my_list = [1, 2, 3, 4, 5]

total_sum = 0
for number in my_list:
    total_sum += number

print("Sum of numbers in the list:   ", total_sum)

#python program to find the average of the numbers in the list
my_list = [1, 2, 3, 4, 5]

total_sum = 0
count = 0

for number in my_list:
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
    print("Average of numbers in the list:", average)
else:
    print("The list is empty.")
    
    
#python program to find and print factorial of given number

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

# Example: Calculate the factorial of 5
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")

        
        
