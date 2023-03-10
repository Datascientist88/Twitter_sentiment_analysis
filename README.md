# Twitter_sentiment_analysis
[YOU CAN ACCESS THE WEB APPLICATION BY CLICKING THIS LINK](https://datascientist88-twitter-sentiment-ana-streamlitsentiment-laa2dt.streamlit.app/)
# paper on my application [Twitter Sentiment Analysis.pdf](https://github.com/Datascientist88/Twitter_sentiment_analysis/files/10472162/Twitter.Sentiment.Analysis.pdf)
<p><img align="center" alt="gif" src="https://user-images.githubusercontent.com/119727641/214800363-f01aa386-cb51-4516-a47e-bf2b8183ff6d.gif" width="1800" height="500" /></p>


Introduction :

This idea began two weeks ago when I began to think about a project in which I can apply deep learning concepts, in particular Natural Language processing or NLP and one of the best places to extract texts and analyze them is the social media especially twitter since it has a wide range of applications in marketing and so on  
I began to think about using an API to get connected to twitter and streamline tweets from twitter however this task was particularly challenging since it required my  twitter account to be verified using my Saudi mobile number but I was confronted with another challenge which is the twitter did not accept my Saudi number  presumably because they have restrictions on Saudi numbers oddly enough , fortunately I managed to overcome this frustrating experience by contacted a friend of mine who  lives in the UK and have had my account authenticated from there , then I managed to developed an API and received the consumer key , consumer secret , access token and access token secret which are incredibly sensitive pieces of information and they raised confidentially concerns in my mind as to how I will deploy this app on the cloud once its ready for deployment once I got to grips with this issue I realized that I will  only be granted a limited access to tweets consequently I decided to rub my hands of this idea and this about another way , luckily I managed to find an alternative to the use of an API  which is the use of a powerful library in python called SNSCRAPE which allowed me to get inexhaustible supply of tweets . 

Application Concept : 
This application snscrape library in python to extract tweets from based on specific terms to query the tweets in my case the user name , the period of time as well as the amount of tweets to be analyzed , then the tweets are streamlined and cleaned through regular expressions or REGEX to remove unwanted parts such as links or @ signs and so on  , once the cleaning is completed I converted them into a pandas DATAFRAME by iterating over the other aspects of the text such as the likes , Date , and retweets , then comes the most significant aspect of my work which the analysis of all the tweets using TEXTBLOB a natural language processing library which tokenizes and computes the subjectivity and polarity of the tweets and I have accomplished this task by defining  two functions , one for subjectivity and the other for polarity and then applied both functions to compute them .

Application Layout : 
This application uses streamlit library as a main framework within which the app components will be coded and displayed in simple charts and data table , as well as a set of widgets to add element of interactivity with user , however I would like to emphasize the fact that this application is a preliminary version of twitter sentiment analysis as it requires further revisions and performance enhancement ideas as it is still beset with terribly slow processing capability and your input will be greatly appreciated in this respect . 

Conclusion : 
Twitter sentiment analysis is an important subject in data science , and ever evolving field with new ideas and approaches to be used to gauge sentiment of users and hashtags to measure the effectiveness of marketing campaigns and thus the use of such intelligent applications will make the process all the more easier . 
 
 
