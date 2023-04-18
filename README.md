# Twitter-Scrapper


REQUIRED SKILLS:

Python scripting
MongoDB
Streamlit
Snscrape

OVERVIEW:

The GUI for this application is made using the Streamlit

USer can input any keyword  to be searched,
select the start date
select the end date
Number of tweets that the user want to be scrapped.
After scraping is done, the user can choose among the following option :-

Download data as CSV
Download data as JSON
Display All the Scrapped Tweets 
Upload data to DATABASE ( mongodb )


WORKING:

Step1: Initially the user will input the Keyword, Start date, End date, and Number of tweets on the GUI made using streamlit

Step 2: The above details are fed to TwitterSearchScraper. A dataframe is created to store the entire scraped data from where the user can download this scraped data in the form of CSV or JSON format

Step3: The database connection is established using pymongo A new collection will be created and data is uploaded into that collection if the user wish to upload



You can now view your Streamlit app in your browser.
                                                  
  Local URL: http://localhost:8501                    
  Network URL: http://192.168.1.4:8501
  
After clicking on the above url you can see the app in your browser
