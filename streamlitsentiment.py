import pandas as pd 
import plotly.express as px 
import numpy as np 
import streamlit as st 
from textblob import TextBlob
import re
import matplotlib.pyplot as plt
from streamlit_lottie import st_lottie
import snscrape.modules.twitter as sntwitter
import datetime
import requests
import json
from streamlit.components.v1 import html
import plotly.graph_objects as go
import time 
from dateutil.relativedelta import relativedelta
## setting the application configurations and layout:
# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.set_page_config(page_title=" TWITTER SENTIMENT ANALYSIS ",layout='wide' )
st.sidebar.title('TWITTER SENTIMENT ANALYSIS')
url="https://assets7.lottiefiles.com/packages/lf20_i2eyukor.json"
r=requests.get(url)
Lottiecode=None if r.status_code !=200 else r.json()
try:
    with st.sidebar:
        st_lottie(Lottiecode,height=200,width=200,speed=1, loop=True)
except:
    pass
user_input=st.sidebar.text_input("Please Enter a Valid Twitter Username like elonmusk:", "billgates")
# the amount of tweets to be analyzed :
since=st.sidebar.date_input('choose the start date',datetime.date(2005,1,1)) 
until=st.sidebar.date_input('choose the end date ',datetime.date(2018,12,31))
Tweets_counter=st.sidebar.slider("choose the Amount of Tweets to Analyze:", 200 ,5000)
user_name=user_input
limit=Tweets_counter
start_date=since
end_date=until

# switch between two models Textblob & Roberta Model # if statement 
try:

        # the first one looking for tweets using the user name :
        query=f"(from:{user_name}) lang:en until:{end_date} since:{start_date}"
        # iterate over the tweets :
        tweets=[]
        limit=Tweets_counter
        for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                if len(tweets)==limit:
                 break
                else:
                    tweets.append([tweet.date,tweet.user.username,tweet.content,tweet.likeCount,tweet.retweetCount])
                    df=pd.DataFrame(tweets,columns=['Date','User','Tweet','Likes','Retweets'])
        # clean the Tweets 
        def cleanTxt(text):
                text=re.sub(r'@[A-Za-z0-9]+', '',text) # removes @ sign 
                text=re.sub(r'#','',text) # removes the hashtag
                text=re.sub(r'RT[\s]+','',text) #removes the retweet RT
                text=re.sub(r'https?:\/\/\S+','',text) # removes the hyperlink
                return text 
        # apply the function on the Tweets:
        df['Tweet']=df['Tweet'].apply(cleanTxt)
        # identify subjectivity and polarity :
        def getSubjectivity(text):
            return TextBlob(text).sentiment.subjectivity
        # another function for polarity :
        def getPolarity(text):
            return TextBlob(text).sentiment.polarity
        # apply the function on tweets 
        df['Subjectivity']=df['Tweet'].apply(getSubjectivity)
        df['Polarity']=df['Tweet'].apply(getPolarity)
        #Categorize the Sentiment into Positive , Negative and Neutral:
        ## create function to add positive , neutral and negative sentiment :
        def getAnalysis(score):
            if score<0.0000:
                return "Negative"
            elif score==0.0000:
                return "Neutral"
            else:
                return "Positive"
        df['Sentiment']=df['Polarity'].apply(getAnalysis)
        # visualise the result:

        df['Date']=pd.to_datetime(df['Date'],format='%Y-%m-%d-%H-%M-%S')
        df.set_index("Date")
        col1,col2=st.columns(2)
        with col1:
            labels = ['Negative','Neutral','Positive']
            values =df['Sentiment'].value_counts().sort_index()
            # Use `hole` to create a donut-like pie chart
            fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
            fig.update_layout(height=500 ,width=750 ,title=f"Sentiment analysis for {user_name} on {Tweets_counter} tweets",legend=dict(yanchor='top',y=0.99,xanchor='left',x=0.1)) 
            st.plotly_chart(fig)
        with col2:
            fig2=px.line(data_frame=df,x="Date",y=['Likes','Retweets'],title=f"The Trend for Like and Retweets for {user_name}")
            st.plotly_chart(fig2)
        st.write(df.head(Tweets_counter))


except:
        url2="https://assets2.lottiefiles.com/packages/lf20_5mhyg2hz.json"
        r2=requests.get(url2)
        Lottiecode2=None if r.status_code !=200 else r.json()
        st_lottie(Lottiecode2,height=600,width=600,speed=1, loop=True)
        st.write ('You have entered either the wrong user name or the wrong period')



        
