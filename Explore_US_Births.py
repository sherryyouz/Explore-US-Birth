#!/usr/bin/env python
# coding: utf-8

# # Explore U.S. Birth Data
# 
# This Project works with a [dataset](https://raw.githubusercontent.com/fivethirtyeight/data/master/births/US_births_1994-2003_CDC_NCHS.csv) on births in the U.S. In this project, we are using the dataset compiled by FiveThirtyEight.
# 
# The dataset contains the following columns:
# - `year` -- Year(1994 to 2003).
# - `month` -- Month(1 to 12).
# - `date_of_month` -- Day number of the month (1 to 31).
# - `day_of_week` -- Day of week (1 to 7).
# - `births` -- Number of births that day.

# ### First, open the file and convert it to a list. 

# In[1]:


f = open("US_births_1994-2003_CDC_NCHS.csv", "r")
file = f.read().split("\n")
file[0:10]


# ### Or create a function that can convert a dataset into a list of lists where each nested list contains integer values.

# In[5]:


def read_csv(csv):
    f = open(csv,"r")
    file = f.read().split("\n")
    string_list = file[1:len(file)-1]
    final_list = []
    for sl in string_list:
        int_fields = []
        string_fields = sl.split(',')
        for sf in string_fields:
            int_fields.append(int(sf))
            final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


# ### Then create a function to calculate the total number of births that occured in each month and each day of week, across all of the years in the dataset.

# In[6]:


def month_births(input_list):
    births_per_month = {}
    for ls in input_list:
        month = ls[1]
        births = ls[4]
        if month in births_per_month:
            births_per_month[month] = births_per_month[month] + births
        else:
            births_per_month[month] = births
    return births_per_month

cdc_month_births = month_births(cdc_list)
cdc_month_births


# In[7]:


def dow_births(input_list):
    births_per_dow = {}
    for ls in input_list:
        dow = ls[3]
        births = ls[4]
        if dow in births_per_dow:
            births_per_dow[dow] = births_per_dow[dow] + births
        else:
            births_per_dow[dow] = births
    return births_per_dow

cdc_day_births = dow_births(cdc_list)
cdc_day_births


# ### To make this process easier, create a function that can calculate the births based on the column we need.
# 
# The `column` can indicate year, month or day of week.

# In[9]:


def calc_counts(input_list, column):
    calc_result = {}
    for ls in input_list:
        calc_index = ls[column]
        result = ls[4]
        if calc_index in calc_result:
            calc_result[calc_index] = calc_result[calc_index] + result
        else:
            calc_result[calc_index] = result
    return calc_result

cdc_year_births = calc_counts(cdc_list, 0)
cdc_year_births


# ### We can then use the same function to calculate sum of births based on columns.

# In[13]:


cdc_month_births = calc_counts(cdc_list, 1)
cdc_dom_births = calc_counts(cdc_list, 2)
cdc_dow_births = calc_counts(cdc_list, 3)

cdc_dom_births


# ## Calculate the min and max births in certain dictionary.

# In[20]:


def find_most(input_dict):
    most_result = {}
    most_result["min_birth"] = min(input_dict.values())
    most_result["max_birth"] = max(input_dict.values())
    return most_result

min_max_month_birth = find_most(cdc_month_births)  
min_max_month_birth

