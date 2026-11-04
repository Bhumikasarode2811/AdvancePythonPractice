# 1 Write a Python program to check whether a number is even or odd.
# num = float(input("Enter Your Number: "))
# if num %2 ==0:
#     print("Even")
# else:
#     print("Odd")

# 2 Write a program to find the largest of three numbers
# num1 =float(input("Enter Your Number1: "))
# num2 = float(input("Enter Your Number2: "))
# num3 = float(input("Enter Your Number3: "))
# if num1 > num2:
#     print("Greatest", num1)
# elif num2 > num3:
#     print("Greatest", num2)
# elif num3 > num1:
#     print("Greatest", num3)
# else:
#     print("Wrong Number")

# 3 Write a program to check whether a given number is prime.
# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")


# 4 Write a program to print the Fibonacci series up to n terms
# n = int(input("Enter number of terms: "))
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a+b
# print()



# 5 Write a program to find the factorial of a number using a loop.
# num = int(input("Enter a number: "))
# fact = 1
# if num < 0:
#     print("Factorial not defined for negative numbers")
# else:
#     for i in range(1, num + 1):
#         fact *= i
#     print("Factorial:", fact)


#  6 Write a program to reverse a string without using [::-1].
# text = input("Enter a string: ")
# reverse = ""
# for ch in text:
#     reverse = ch + reverse
# print("Reversed String:", reverse)


#  7 Write a program to check whether a string is a palindrome
# text = input("Enter a string: ")
# reverse = ""
# for ch in text:
#     reverse = ch + reverse
# if text == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#  8 Write a program to count the number of vowels and consonants in a string.
# text = input("Enter a string: ")
# vowels = 0
# consonants = 0
# for ch in text.lower():
#     if ch.isalpha():
#         if ch in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
# print("Vowels:", vowels)
# print("Consonants:", consonants)


#  9 Write a program to find the sum of all elements in a list.
# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# print("Sum:", total)




#  10 Write a program to find the largest and smallest element in a list without using max() or min().
# numbers = [10, 5, 30, 2, 50, 15]
# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
#     if num < smallest:
#         smallest = num
# print("Largest:", largest)
# print("Smallest:", smallest)


#  11 Write a program to remove duplicate elements from a lis
# numbers = [10, 20, 10, 30, 20, 40]
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print("Unique List:", unique)


#  12 Write a program to count how many times each element appears in a list using a dictionary.
# numbers = [10, 20, 10, 30, 20, 10]
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print("Frequency:", frequency)


#  13 Write a program to find the second-largest number in a list.
# numbers = [10, 50, 30, 20, 40]
# largest = float('-inf')
# second = float('-inf')
# for num in numbers:
#     if num > largest:
#         second = largest
#         largest = num
#     elif largest > num > second:
#         second = num
# if second == float('-inf'):
#     print("Second largest does not exist")
# else:
#     print("Second Largest:", second)


# 14 Write a program to sort a list without using sort() or sorted().
# numbers = [40, 10, 30, 20, 50]
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] > numbers[j]:
#             numbers[i], numbers[j] = numbers[j], numbers[i]
# print("Sorted List:", numbers)


# 15 Write a function that accepts a list of numbers and returns a list containing only the even numbers.
# def even_numbers(numbers):
#     result = []
#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num)
#     return result
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# print("Even Numbers:", even_numbers(numbers))


# 16 Write a program to find the frequency of each character in a string.
# text = input("Enter a string: ")
# frequency = {}
# for ch in text:
#     if ch in frequency:
#         frequency[ch] += 1
#     else:
#         frequency[ch] = 1
# print("Character Frequency:", frequency)


#  17 Write a program to check whether two strings are anagrams of each other.
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# str1 = str1.replace(" ", "").lower()
# str2 = str2.replace(" ", "").lower()
# if sorted(str1) == sorted(str2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")


#  18 Write a program to find all duplicate values in a list.
# numbers = [10, 20, 30, 10, 40, 20, 50]
# duplicates = []
# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)
# print("Duplicate Values:", duplicates)


#  19 Write a program that takes a sentence and finds the longest word.
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest Word:", longest)


#  20 Create a simple student marks program that:a. accepts marks for 5 subjects  b.calculates the total and percentage  c. assigns a grade,and displays whether the student passed or failed.
# marks = []
# for i in range(5):
#     m = float(input(f"Enter marks for subject {i+1}: "))
#     marks.append(m)
# total = sum(marks)
# percentage = total / 5
# print("Total Marks:", total)
# print("Percentage:", percentage, "%")
# if any(m < 35 or m > 100 for m in marks):
#     print("Result: Fail")
#     print("Grade: F")
# elif percentage >= 90:
#     print("Result: Pass")
#     print("Grade: A+")
# elif percentage >= 80:
#     print("Result: Pass")
#     print("Grade: A")
# elif percentage >= 70:
#     print("Result: Pass")
#     print("Grade: B")
# elif percentage >= 60:
#     print("Result: Pass")
#     print("Grade: C")
# else:
#     print("Result: Pass")
#     print("Grade: D")

