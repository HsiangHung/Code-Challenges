## Hsiang-Hsuan Hung's feature 1 solution

import unicodedata
import re

def removeNonAscii(s):  return re.sub(r'\\u\w{4}','',s)#return "".join(filter(lambda x: ord(x)<128, s))

hand = open('Input/tweets.txt')
#hand = open('hashtag.txt')

evt =list()
evt_time  =list()
unicode_count =0
for sentence in hand:
    sentence = sentence.rstrip()

    ## search for the context start with "text:"
    index_event = sentence.find(',"text":')
    if index_event !=-1:
        eventIndex_end = sentence.find('",',index_event)
        event = sentence[index_event:eventIndex_end].replace(',"text":"','').replace('",','')
        decodeEvent = removeNonAscii(event)
        if (decodeEvent != event): 
            unicode_count +=1 #unicode_exist = True
            event = decodeEvent
        event = event.replace("\\","").strip()
        evt.append(event)

    ## search for context start with "created_ at"
    index_time = sentence.find('{"created_at":')
    if index_time !=-1:
        time = sentence[index_time:].replace('{"created_at":"','')
        index_end = time.find('",')
        #print (time[:index_end])
        evt_time.append(time[:index_end])
 
 
f1=open('Output/ft1.txt', 'w+')

for i in range(len(evt)):
    print (evt[i]+" (timestamp: "+evt_time[i]+')',file=f1)

print ('      \n',file=f1)
print (str(unicode_count)+' tweets contained unicode.',file=f1)







