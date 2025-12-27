import sys
import json
sys.stdout.reconfigure(encoding='utf-8')
with open("initial_data.txt", encoding='utf-8') as f:
    content = f.read()
    # print(content)

data=content.split("\n\n")
# print(data)

data=[c for c in data if len(c)>3]
# print(data[0])

def parsing_data(data):
        data=data.strip()
        new_data=data.split("\n")
        username=new_data[0]
        no_of_posts=int(new_data[1].split(" post")[0].replace(",", ""))
        no_of_followers=float(new_data[2].split(" follower")[0].replace(",", "").replace("K", "").replace("M", ""))
        if("K" in new_data[2]):
            no_of_followers = int(no_of_followers * 1000)
        elif("M" in new_data[2]):
            no_of_followers = int(no_of_followers * 1000000)
        else:
            no_of_followers = int(no_of_followers)
             
        no_of_following=float(new_data[3].split(" following")[0].replace(",", "").replace("K", "").replace("M", ""))
        if("K" in new_data[3]):
            no_of_following = int(no_of_following * 1000)
        elif("M" in new_data[3]):
            no_of_following = int(no_of_following * 1000000)
        else:
            no_of_following = int(no_of_following)
             
        name=new_data[4]
        if(len(new_data)>5):
            categories = new_data[5]
            bio = "\n".join(new_data[6:])
        else:
            categories = "Unknown"
            bio = ""
        return{"username":username,"no_of_posts":no_of_posts,"no_of_followers":no_of_followers,"no_of_following":no_of_following,"name":name,"categories":categories,"bio":bio}

# print(parsing_data(data[0]))
list_parsed_data=[]
for dat in data:
    data_p=parsing_data(dat)
    list_parsed_data.append(data_p)
    
with open("formated_data.json","w") as f:
     json.dump(list_parsed_data,f)

# print(list_parsed_data)
max=0
for lpd in list_parsed_data:
    if(max<lpd['no_of_posts']):
        max = lpd['no_of_posts']
        chunk_with_max_posts = lpd
print(f"maximum number of posts:{chunk_with_max_posts}\n")

max=0
for lpd in list_parsed_data:
    if(max<lpd['no_of_followers']):
        max = lpd['no_of_followers']
        chunk_with_max_posts = lpd
print(f"maximum number of followers:{chunk_with_max_posts}\n")


max=0
for lpd in list_parsed_data:
    if(max<lpd['no_of_following']):
        max = lpd['no_of_following']
        chunk_with_max_posts = lpd
print(f"maximum number of following:{chunk_with_max_posts}\n")

sets=set()
for lpd in list_parsed_data:
    
    sets.add(lpd["categories"])

print(f"the number of categories is {len(sets)}")