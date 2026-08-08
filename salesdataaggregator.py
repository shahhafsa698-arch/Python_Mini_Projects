#Sales data aggregator
count=0
tot_sale=0
highest_sale=None
lowest_sale=None

for sale in[4,6,5,8,10]:
    count=count+1
    tot_sale=tot_sale+sale
    if highest_sale is None or sale>highest_sale:
        highest_sale=sale
    if lowest_sale is None or sale<lowest_sale:
        lowest_sale=sale

print("Total Transactions Processed:", count)
print("Total Sales Revenue: $" ,(tot_sale))
print("Average Sale Amount: $" ,(tot_sale / count))
print("Highest Single Sale: $" ,(highest_sale))
print("Lowest Single Sale: $" ,(lowest_sale))