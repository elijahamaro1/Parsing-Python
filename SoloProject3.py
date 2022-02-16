from pip._vendor import requests #imports library names requests from python standard libraries

URL = 'https://s3.amazonaws.com/tcmg476/http_access_log' #url used in lab

ActualRequest = requests.get(URL) #requests url from aws

filename = ActualRequest.url[URL.rfind('/')+1] #puts request into file named filename

#makes filename readable
with open(filename, 'wb') as f:
    for chunk in ActualRequest.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

#counts total number of requests
with open(filename, 'r') as fp:
    x = len(fp.readlines())
    print("Total requests:", x)
fp.close()

#creates array for the entire url
with open(filename) as fpcount:
    array = []
    for line in fpcount:
        array.append(line)

#must begine count with 0
count = 0

#stackoverflow became my best friend
for i in array:
    if i.find("Apr") != -1 and i.find("1995") != -1 and i.find("[11") != -1:
        count += 1
    elif i.find("May") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jun") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Jul") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Aug") != -1 and i.find("1995") != -1:
        count += 1
    elif i.find("Sep") != -1 and i.find("1995") != -1:
        count += 1
        array[count] = i
    elif i.find("Oct") != -1 and i.find("1995") != -1:
        count += 1

#use the count function to print the total amount of requests within the last 6 months
print("Requests made in the last 6 months:", count)


#april 11th is the first day in the last 6 months
#print the number of requests from 11/Apr/1995 to 11/Oct/1995
