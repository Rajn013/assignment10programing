#!/usr/bin/env python
# coding: utf-8

# 1.Write a Python program to find sum of elements in list?

# In[1]:


number = [25,26,27,28,29]

sum = 0
for num in number:
    sum += num
print("the sum of element in the list is:",sum)


# 2.Write a Python program to  Multiply all numbers in the list?

# In[2]:


product = 1
for num in number:
    product *= num
    
print("the product of all number in the list is:",product)


# 3.Write a Python program to find smallest number in a list?

# In[6]:


number =[15,22,894,24189,1,3]
samllest = number[0]
for num in number :
    if num < samllest:
        smallest = num
print("the smallest number in the list is:",smallest)


# 4.Write a Python program to find largest number in a list?

# In[12]:


numbers = [56,251,22,63,2,3,85,479,8,9]
largest_number = max(numbers)
print("The largest number in the list is:", largest_number)


# 5.Write a Python program to find second largest number in a list?

# In[38]:


sorted_number = sorted(number, reverse=True)
print("the second largest number in the list is:",sorted_number[1])


# 6.Write a Python program to find N largest elements from a list?

# In[39]:


N =2
sorted_number = sorted(number , reverse=True)

print("the",N,"largest number in the list are:", sorted_number[:N])


# 7.Write a Python program to print even numbers in a list?

# In[40]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)


# 8.Write a Python program to print odd numbers in a List?

# In[49]:


for number in numbers:
    if number % 2 != 0:
        print(number)


# 9.Write a Python program to Remove empty List from List?

# In[50]:


list_of_lists =[[1,2,3],[],[4,5],[],[6,7,8],[]]

filtered_list = [lst for lst in list_of_lists if lst]
print(filtered_list)


# 10.Write a Python program to Cloning or Copying a list?

# In[51]:


original_list = [1,2,3,4,5]
new_list = original_list.copy()
new_list_2 = list(original_list)

print("Original list:", original_list)
print("cloned list using copy():",new_list)
print("cloned list using copy():", new_list_2)


# 11.Write a Python program to Count occurrences of an element in a list?

# In[53]:


my_list = [1,2,3,4,5,1,2,3,4,5]

element = 1
count = my_list.count(element)
print("The element", element, "appears",count, "time in thee list")


# In[ ]:




