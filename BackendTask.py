input_string = input("Enter leads of various company: ") 
userList = input_string.split(",")
def leads(User_list):
    Lead_list={}
    count={}
    for i in User_list:
        domain_name=i[i.index('@')+1:]
        name=i[0:i.index('@')]
        if(domain_name not in Lead_list):
            Lead_list[domain_name]=[]
            Lead_list[domain_name].append(name)
            count[domain_name]=1 
            
        else:
            Lead_list[domain_name].append(name)
            count[domain_name]+=1
    return Lead_list, count
print(leads(userList))
