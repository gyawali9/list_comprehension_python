#!/usr/bin/env python
# coding: utf-8

# # BMI calculator for Adults

# In[1]:


print('Enter your height in centimetres:')
height_cm = float(input())


# In[2]:


print('Enter your weight in kilogram:')
weight_kg = float(input())


# In[3]:


height_m = height_cm / 100
BMI = weight_kg /(height_m * height_m)
print('Your BMI is ' + str(BMI))


# In[4]:


if BMI < 18.5:print("Status: Underweight")
elif BMI >= 18.5 and BMI < 25:print("Status: Normal weight")
elif BMI >= 25 and BMI < 30:print("Status: Overweight")
elif BMI >= 30 and BMI < 35:print("Status: Obese")
else:print("Status: Morbidly Obese")

