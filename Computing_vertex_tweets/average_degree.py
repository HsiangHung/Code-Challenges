import unicodedata
import re
import time
import string
from datetime import datetime


f2=open('Output/ft2.txt', 'w+')


def bond_collection(vertex0, vertex1, post, time):
    global tag_bond, tag_vertex
    global tag_bond_time
    tag_bond.insert(post, [vertex0,vertex1])
    tag_bond_time.insert(post,time)
    tag_vertex[vertex0] = tag_vertex.get(vertex0,0)+1
    tag_vertex[vertex1] = tag_vertex.get(vertex1,0)+1
        
        
def rolling_degree(tag_vertex):
    if len(tag_vertex)==0: return 0
    ave=0
    for key in tag_vertex:
        ave += tag_vertex[key]
    return ave/len(tag_vertex)


def time_convert(time1, time2):
        datetime1=tag_bond_time[0].split()
        datetime2=tag_bond_time[len(tag_bond_time)-1].split()
        month1 = monthConvt[datetime1[1]]
        month2 = monthConvt[datetime2[1]]
        day1=int(datetime1[2])
        day2=int(datetime2[2])
        time1=datetime1[3].split(':')
        time2=datetime2[3].split(':')
        year1 =int(datetime1[5])
        year2 =int(datetime2[5])
        date1 = datetime(year1,month1,day1,int(time1[0]),int(time1[1]),int(time1[2]))
        date2 = datetime(year2,month2,day2,int(time2[0]),int(time2[1]),int(time2[2]))
        diff = date2 -date1
        return get_sec(str(diff))

    
def get_sec(s):
    l = s.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])    
 
    
# this function is used to determin if we want to evict the very first hashtag or not
# we need to check if the first one to the last updated one has interval of 60 s or not.
def evict():
    global tag_bond,tag_bond_time,tag_vertex
    if len(tag_bond_time) !=0 :
        while True:
            #print (tag_bond_time[0],tag_bond_time[len(tag_bond_time)-1],file=f2)
            timeDiff = time_convert(tag_bond_time[0],tag_bond_time[len(tag_bond_time)-1])
            #print(timeDiff,file=f2)
            if timeDiff <= 60: break
            vertex0 = tag_bond[0][0]
            vertex1 = tag_bond[0][1]
            tag_vertex[vertex0] -= 1
            tag_vertex[vertex1] -= 1
            tag_bond.pop(0)
            tag_bond_time.pop(0)
            
        #print(' \n',file=f2)        
        #print('now tag',tag_bond, file=f2)   
        #print('now tag time', tag_bond_time, file=f2)


            
hand = open('Output/ft1.txt')


hashTag     = list()
hashTag_time= list()
tag_bond      = list()
tag_bond_time = list()

tag_vertex = dict()

exclude = set(string.punctuation)

month_name = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
monthConvt = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5, 'Jun':6, 'Jul':7, 'Aug':8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}


#for event in evt:
for event in hand:    
#for i in range(len(evt)):
    event = event.rstrip()
    #event      = evt[i].rstrip()
    #event_time = evt_time[i]
    tagExist = re.search('#',event)
    if tagExist:    
        #print ('------',file=f2)
        words = event.split(' ')
        #print (event,'('+event_time+')')
        #print (event,file=f2)
        
        ##########################################
        time_index = event.find("(timestamp: ")
        event_time = event[time_index:]
        event_time = event_time.replace("(timestamp: ","")
        event_time = event_time.replace(")","")
        #print (event_time,file=f2)
        ##############################################
        
        ## This step filters out the words with "#" at the beginning.
        ## "sub_tag" stores the sub-list within the same tweet.
        ## Also, the "sub_bond" records the sub-bond connecting vertices
        ## of this tweet.
        sub_tag  = list()
        sub_bond = list()
        for word in words:
            if  not word.startswith("#"): continue
            word = word.replace("#","").lower()
            word = ''.join(ch for ch in word if ch not in exclude)
            if len(sub_tag)!=0:
                if word == sub_tag[len(sub_tag)-1]: continue
            if word == '': continue        
            sub_tag.append(word)
            if len(sub_tag)==1: continue
            bond_collection(sub_tag[len(sub_tag)-2], word, len(tag_bond), event_time)
        
        if len(sub_tag)==0 : continue  ## this is used to check if the hastag is empty ""
                                       ## since it is possible after removing "#", nothing
            
        #print ('sub',sub_tag, file=f2)
        
        ## The followings are used to rearrange (classified)
        ## the hashtag in all tweets.
        if len(sub_tag)==1:           ## if the tweet has only one hashtag:
            if len(hashTag)==0:       ##    if the tweest is the first tweet, created the edge
                hashTag.append(sub_tag)
            else:                     ##    else the hashtag of this tweet is absorbed to preivous tweet.
                oldTag = hashTag[len(hashTag)-1]
                bond_collection(oldTag[len(oldTag)-1],sub_tag[0], len(tag_bond), event_time)
                hashTag.remove(oldTag)
                oldTag.append(sub_tag[0])
                hashTag.append(oldTag)
        else:                         ## if the tweet has two/more hashtags:
            if len(hashTag) !=0:
                if len(hashTag[0])==1:  ## if the first tweet has only one hashtag, we need to absorb it
                    oldTag = hashTag[len(hashTag)-1]
                    bond_collection(oldTag[0],sub_tag[0], 0, event_time)
                    hashTag.remove(oldTag)
                    sub_tag.insert(0,oldTag[0])
                    hashTag.append(sub_tag)
                else:
                    hashTag.append(sub_tag)
            else:
                hashTag.append(sub_tag)
  
        #print (tag_vertex,file=f2)
    
        ## determine if drop the early bond when a new tweet comes in
        evict()
        
        
        avg = format(rolling_degree(tag_vertex),'.2f')
        print (avg, file=f2)

