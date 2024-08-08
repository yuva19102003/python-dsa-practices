# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#

exp = [2200, 2350, 2600, 2130, 2190]
print("---------------------------------------------------------------")

# 1. In Feb, how many dollars you spent extra compare to January?
ans1 = exp[1] - exp[0]
print("difference is : ", ans1)
print("---------------------------------------------------------------")


# 2. Find out your total expense in first quarter (first three months) of the year.
ans2 = exp[0]+exp[1]+exp[2]
print("the quarter is :",ans2)
print("---------------------------------------------------------------")


# 3. Find out if you spent exactly 2000 dollars in any month
ans3 = 2000 in exp
print("if you spent exactly 2000 dollars in any month :",ans3)
print("---------------------------------------------------------------")


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print(exp)
print("---------------------------------------------------------------")


# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("correction is :",exp[3])
print(exp)
print("---------------------------------------------------------------")