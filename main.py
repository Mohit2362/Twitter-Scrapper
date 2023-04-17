import pandas as pd
import streamlit as st
import snscrape.modules.twitter as smntwitter
import pymongo
import time

client = pymongo.MongoClient("mongodb://localhost:27017")  # To connect to MONGODB
mydb = client["Tweet_Database"]

tweets_df = pd.DataFrame()

Tweet_Word = st.text_input('Please enter the tweet word')
Start_Date = st.date_input("Select the start date:")
End_Date = st.date_input("Select the end date:")
Tweet_Count = st.number_input('Enter the number of tweets:')
tweet_list = []

for i, tweet in enumerate(smntwitter.TwitterSearchScraper(f'{Tweet_Word} + since:{Start_Date} until:{End_Date}').get_items()):
    if i >= Tweet_Count:
        break
    tweet_list.append([tweet.id, tweet.date,  tweet.content, tweet.user.username, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.source, tweet.url])

tweets_df = pd.DataFrame(tweet_list, columns=['ID', 'Date', 'Content',  'Username', 'ReplyCount', 'RetweetCount', 'LikeCount', 'Source', 'Url'])

@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')


if not tweets_df.empty:
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        csv = convert_df(tweets_df) # CSV
        a = st.download_button(label="Download data as CSV",data=csv,file_name='Twitter_data.csv',mime='text/csv',)
    with col2:
        json_string = tweets_df.to_json(orient ='records')
        j = st.download_button(label="Download data as JSON",file_name="Twitter_data.json",mime="application/json",data=json_string,)

    with col3:
        y = st.button('Show Filtered Tweets',key=2)

    with col4:
        z = st.button('Upload Tweets to Database',key=3)

if a:
    st.success("The Scraped Data is Downloaded as .CSV file:",icon="✅")
if j:
    st.success("The Scraped Data is Downloaded as .JSON file",icon="✅")

if y: # DISPLAY
    st.success("Tweets Scraped Successfully:",icon="✅")
    st.write(tweets_df)

if z: 
     coll=Tweet_Word
     coll=coll.replace(' ','_')+'_Tweets'
     mycoll=mydb[coll]
     dict=tweets_df.to_dict('records')
     if dict:
         mycoll.insert_many(dict)
         ts = time.time()
         mycoll.update_many({}, {"$set": {"KeyWord_or_Hashtag": Tweet_Word+str(ts)}}, upsert=False, array_filters=None)
         st.success('Successfully uploaded to database', icon="✅")
         st.snow()
     else:
         st.warning('Cant upload because there are no tweets', icon="⚠️")