


#Importing the libraries


import numpy as np
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report,accuracy_score
import urllib.request
from bs4 import BeautifulSoup
import re
from gensim.summarization.summarizer import summarize


# define the path of the data which has to be trained:


path=#type your bbc.rar path here


# load the data :


data=load_files(path) 
print("program loaded the data successfully")

#splitting the data
x_train,x_test,y_train,y_test=train_test_split(data.data,data.target)
print("program exited successfully from splitting for training ")
#using vectorizer to convert the words into integr format
vectorizer=TfidfVectorizer(stop_words='english',max_features=1000,decode_error="ignore")
print(vectorizer)
vectorizer.fit(x_train)
print("vectorizer fitted successfully")

#creating the instance for the model

cls=MultinomialNB()
print("Successfully created instance for MultinomialNB ")

#fitting the model for prediction
print("Fitting the model ")
cls.fit(vectorizer.transform(x_train),y_train)

#Value predicted for accuracy_score
print("predicting the y_pred")
y_pred=cls.predict(vectorizer.transform(x_test))
print("Succesfully predicted the y_pred")

#accuracy_score checker
print("Checking the Accuracy score")
acc_score=accuracy_score(y_test,y_pred)
print("Accuracy score for this model is ",acc_score*100,'%')


# Wikipedia scrapping :


url="https://en.wikinews.org/wiki/Main_Page"
page=urllib.request.urlopen(url)
soup=BeautifulSoup(page,features='lxml')
latest_news=soup.find(id="MainPage_latest_news_text")
latest_news=str(latest_news)
pattern=re.compile('"(/.*?)"')
matches=pattern.findall(latest_news)
match_list=[]
main_news_url="https://en.wikinews.org"
latest_news_pages_downloaded=[]
replace_list=["xa0nnnnnn","[...]","Share this:\xa0\n\n\n\n\n\n","'Share this:\xa0\n\n\n\n\n\n'","\\","Have an opinion on this story? Share it!","\xa0\n","\n",'\\n"',"\s","\\n","\\n\'","\'\\n\'","\'s","\'",",","-","'\n'","\'Have an opinion on this story? Share it!","Share this:","\\xa0\\n\"","\\xa0","\'Share this:\\n\\n\\n\\n\\n\\n\'","n n n xa0nnnnnn","xa0n","xa0"]
converted_string=[]
Business_news=[]
Business_news_sum=[]
Entertainment_news=[]
Entertainment_news_sum=[]
Politics_news=[]
Politics_news_sum=[]
Technology_news=[]
Technology_news_sum=[]
error_predicted=[]




#separating the urls:
#text only taken
#removing the unnecessary letters


for match in matches:
    match_list.append(match)
for i in match_list:
    download_news_url=main_news_url+i
    temp_page=urllib.request.urlopen(download_news_url)
    temp_soup=BeautifulSoup(temp_page,features="lxml")
    temp_news_list=[]
    for i in range(len(temp_soup.find_all("p"))):
        temp_news=temp_soup.find_all("p")[i].get_text()
        temp_news_list.append(str(temp_news))
    converted_string=str(temp_news_list)
    count=0
    for j in replace_list:
        replaced_string=converted_string.replace(j,"")
        count+=1
        if(count<=len(replace_list)):
            converted_string=replaced_string
    latest_news_pages_downloaded.append(replaced_string)

    


# predicting the text :


predicted=cls.predict(vectorizer.transform(latest_news_pages_downloaded))


# segrating the text:


for i in range(len(predicted)):
    if (predicted[i]==0):
        Business_news.append(latest_news_pages_downloaded[i])
        Business_news_sum.append(summarize(latest_news_pages_downloaded[i],ratio=0.40))
    elif (predicted[i]==1):
        Entertainment_news.append(latest_news_pages_downloaded[i])
        Entertainment_news_sum.append(summarize(latest_news_pages_downloaded[i],ratio=0.40))
    elif (predicted[i]==2):
        Politics_news.append(latest_news_pages_downloaded[i])
        Politics_news_sum.append(summarize(latest_news_pages_downloaded[i],ratio=0.40))
    elif(predicted[i]==3):
        Technology_news.append(latest_news_pages_downloaded[i])
        Technology_news_sum.append(summarize(latest_news_pages_downloaded[i],ratio=0.40))
    else:
        error_predicted.append(latest_news_pages_downloaded[i])


# defined for printing the segregated text


def print_business_news():
    print("***Business News***")
    print("\n")
    for i in range(len(Business_news)):
        print(Business_news[i],"\n")
def print_business_news_summ():
    print("***Business News Summaries***")
    print("\n")
    for i in range(len(Business_newss)):
        print(Business_news_sum[i],"\n")
def print_entertainment_news():
    print("***Entertainment News***")
    print("\n")
    for i in range(len(Entertainment_news)):
        print(Entertainment_news[i],"\n")
def print_entertainment_news_summ():
    print("***Entertainment News Summaries***")
    print("\n")
    for i in range(len(Entertainment_news_sum)):
        print(Entertainment_news_sum[i],"\n")
def print_politic_news():
    print("***Politics News***")
    print("\n")
    for i in range(len(Politics_news)):
        print(Politics_news[i],"\n")
def print_politics_news_summ():
    print("***Politics News Summaries***")
    for i in range(len(Politics_news_sum)):
        print(Politics_news_sum[i],"\n")
def print_technology_news():
    print("***Technology News***")
    for i in range(len(Technology_news)):
        print(Technology_news[i],"\n")
def print_technology_news_summ():
    print("***Technology News Summaries***")
    for i in range(len(Technology_news_sum)):
         print(Technology_news_sum[i],"\n")
def print_news_fully():
    
    print("***Business News***")
    print("\n")
    for i in range(len(Business_news)):
        print(Business_news[i],"\n")
        
    
    print("***Entertainment News***")
    print("\n")
    for i in range(len(Entertainment_news)):
        print(Entertainment_news[i],"\n")
    
    print("***Politics News***")
    print("\n")
    for i in range(len(Politics_news)):
        print(Politics_news[i],"\n")
    
    print("***Technology News***")
    print("\n")
    for i in range(len(Technology_news)):
        print(Technology_news[i],"\n")
        
def print_news_summ():
    
    print("***Business News Summaries***")
    print("\n")
    for i in range(len(Business_news)):
        print(Business_news_sum[i],"\n")
    
    print("***Entertainment News Summaries***")
    print("\n")
    for i in range(len(Entertainment_news_sum)):
        print(Entertainment_news_sum[i],"\n")
    
    print("***Politics News Summaries***")
    for i in range(len(Politics_news_sum)):
        print(Politics_news_sum[i],"\n")
    
    print("***Technology News Summaries***")
    for i in range(len(Technology_news_sum)):
        print(Technology_news_sum[i],"\n")
        

def print_news_full_summ():
    
    print("***Business News Full***")
    print("\n")
    for i in range(len(Business_news)):
        print(Business_news[i],"\n")
        
    print("***Business news Summaries***")
    print("\n")
    for i in range(len(Business_news)):
        print(Business_news_sum[i],"\n")
      
    print("***Entertainment News Full*** ")
    print("\n")
    for i in range(len(Entertainment_news)):
        print(Entertainment_news[i],"\n")
    
    print("***Entertainment News Summaries***")
    for i in range(len(Entertainment_news_sum)):
        print(Entertainment_news_sum[i],"\n")
         
    print("***Politics News Full***")
    print("\n")
    for i in range(len(Politics_news)):
        print(Politics_news[i],"\n")
        
    print("***Politics News Summaries***")
    print("\n")
    for i in range(len(Politics_news_sum)):
        print(Politics_news_sum[i],"\n")
        
    print("***Technology News Full***")
    print("\n")
    for i in range(len(Technology_news)):
        print(Technology_news[i],"\n")
        
    print("***Technology News Summaries***")
    for i in range(len(Technology_news_sum)):
        print(Technology_news_sum[i],"\n")


# Main Menu for accessing:


def get_print_input():
    print("Types of news :")
    print("1 : Business News")
    print("2 : Entertainment News ")
    print("3 : Politics News")
    print("4 :Technology News")
    print("5 : All the News ")
    input_from_user=input("waiting to serve: ")
    if(input_from_user=="1"):
        print("Business News Selected")
        print("1: Bussines News Full ")
        print("2: Bussiness News Summarized")
        input_from_user_sub=input("waiting for input : ")
        if(input_from_user_sub=="1"):
            print_business_news()
        elif(input_business=="2"):
            print_business_news_summ()
        else:
            print("wrong input try again")
            get_print_input()
    elif(input_from_user=="2"):
        print("Entertainment News Selected")
        print("1: Entertainment News Full")
        print("2: Entertainment News Summarized ")
        input_from_user_sub=input("Waiting for input : ")
        if(input_from_user_sub=="1"):
            print_entertainment_news()
        elif(input_from_user_sub=="2"):
            print_entertainment_news_summ()
        else:
            print("wrong input try again")
            get_print_input()
        
    elif(input_from_user=="3"):
        print("Politics News Selected")
        print("1: Politics News Full")
        print("2: Politics News Summarized")
        input_from_user_sub=input("waiting for input: ")
        if(input_from_user_sub=="1"):
            print_politic_news()
        elif(input_from_user_sub=="2"):
            print_politics_news_summ()
        else:
            print("wrong input try again")
            get_print_input()
        
    elif(input_from_user=="4"):
        print("Technology News Selected")
        print("1: Technology News Full")
        print("2: Technology News summarized" ) 
        input_from_user_sub=input("Waiting for input: ")
        if(input_from_user_sub=="1"):
            print_technology_news()
        elif(input_from_user_sub=="2"):
            print_technology_news_summ()
        else:
            print("wrong input try again")
            get_print_input()
    
    elif(input_from_user=="5"):
        print("All the News Selected")
        print("1: All the News Full")
        print("2: All the News Summarized")
        print("3: All the News Full and Summarized")
        input_from_user_sub=input("Waiting for input: ")
        if(input_from_user_sub=="1"):
            print_news_fully()
        elif(input_from_user_sub=="2"):
            print_news_summ()
        elif(input_from_user_sub=="3"):
            print_news_full_summ()
        else:
            print("wrong input try again")
            get_print_input()
    print("Want to try again:")
    print("type 'yes' to try again")
    print("type 'no' to exit the program")
    input_from_user=input("waiting for input: ")
    if(input_from_user=="yes"):
        get_print_input()
    elif(input_from_user=="no"):
        exit()
            


# Calling function for the main menu:


get_print_input()







