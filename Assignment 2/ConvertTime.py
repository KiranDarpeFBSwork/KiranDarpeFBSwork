#convert entered time in to hour's minet's and second's 
time=int(input("Enter Time:"))
temp=time
hours=temp//3600
temp=temp%3600
minets=temp//60
temp=temp%60
seconds=temp%60
print(f"given time in hours:{hours} minets:{minets} seconds:{seconds}")
