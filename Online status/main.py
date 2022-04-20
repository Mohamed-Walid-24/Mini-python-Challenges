statuses={}
def online_count(statuses):
    i=0
    for names in statuses:
        if statuses[names] == "online":
            i=i+1
    return i
n = int(input("Number of persons: "))
for i in range(n):
    name = input("Enter your name: ")
    status = input("Enter your status: ")
    statuses[name]= status
print(online_count(statuses))