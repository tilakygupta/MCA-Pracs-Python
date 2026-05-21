string = input("Enter a string: ").lower()

reverse_string = string[::-1]

vowels = "aeiouAEIOU"
vowel_counter = 0
for ch in string:
    if ch in vowels:
        vowel_counter += 1


if string == reverse_string:
    palindrome = True
else:
    palindrome = False

# Display results
print("\n--- String Operations ---")
print("Original String :", string)
print("Reversed String :", reverse_string)
print("Vowel Count     :", vowel_counter)
print("Palindrome :", palindrome)


nums = list(map(int,input("\nEnter numbers with spaces: ").split()))

sorted_nums = sorted(nums)

max_num = max(nums)
min_num = min(nums)

unique_num = list(set(nums))

print("\n--- List Operations ---")
print("Original List       :", nums)
print("Sorted List         :", sorted_nums)
print("Maximum Element     :", max_num)
print("Minimum Element     :", min_num)
print("List Without Duplicates :", unique_num)