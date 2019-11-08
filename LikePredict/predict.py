import numpy as np
import pandas as pd
import random
import os
# from sklearn import tree

# f=open("./data_final.csv","r")
# arr1=[s for s in f.readline().split(',')]
# arr2=[float(s) for s in f.readline().split(',')]
# print(arr2)

columns = ['categoryId','channel_subscriberCount','definition','likeCount','dislikeCount','viewCount','commentCount','viewCount/channel_month_old','viewCount/video_month_old','viewCount/http_in_descp','viewCount/NoOfTags','viewCount/tags_in_desc','social_links','subscriberCount/videoCount','channelViewCount/channeVideoCount','channelViewCount/socialLink']
df = pd.read_csv('data_final.csv', sep = ',', names = columns)
df.head()

df.drop('likeCount',axis=1)
df.head()

print(df)
