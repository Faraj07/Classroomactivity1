import matplotlib.pyplot as plt

work_days = ["Mon", "Tue", "Wed", "Thur", "Frid", "Sat", "Sun"]
sales = [ 20,25,24,32,19,43,12,53,55,23,43,23,32,33]
sales_per_weekday = []
how_many = int(len(sales)//7)+ 1

for x in range(7):
    x_days = []
    for i in range(how_many):
        try:
            x_days.append(sales[(i)*7+x])


        except:
            pass
    final = 0
    for i in x_days:
        final = final + i
    sales_per_weekday.append(final)

print(sales_per_weekday)
n = 7
list_of_weeks = []

for uy in range (3):
    temp = []
    m = 0

    for l in range(5):
        try:
            temp.append(sales[(uy*5)+l])


        except:
            pass

    for i in temp:
        m = m + i
    list_of_weeks.append(m)


for f in range(len(list_of_weeks)):
    if list_of_weeks[f] == max(list_of_weeks):
        print(f)
print(list_of_weeks)

# Create a bar chart of sales by weekday
plt.bar(work_days, sales_per_weekday)
plt.title('Sales by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Sales')
plt.show()



