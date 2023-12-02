import nltk 
from nltk.corpus import stopwords
from yelpapi import YelpAPI
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

analyzer = SentimentIntensityAnalyzer()

api_key = "XiHb8JTHxYv-Jy79utp6nbaqFNAsLPoqmgOtwkwDZe_u6FluTf4GyV4_AN55hednVAFJRtzOhtUDVUMB2jVGxwhYDZMkpnrHfJEadMFWXSiDhr-BQnbW7FtGJPJMZXYx"
yelp_api_instance = YelpAPI(api_key)

## Searching for 7 sushi restrurants at random that will be chosen for further analysis

food = 'sushi'
city = 'San Diego , CA'
search_rslts = yelp_api_instance.search_query(
    term = food, location = city, 
    sort_by = 'rating', limit = 15, offset = 15
)

# print(search_rslts)

# Functions for each resturant 

# def tanuki():
#     for busi in search_rslts['businesses']:
#         print('\n')
#         print(busi)

#         id_for_rvws = 'tanuki-san-diego'

#         review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

#         for rvw in review_rpnse['reviews']:
#             return print("\n", rvw)
            
# def toratora():
#     for busi in search_rslts['businesses']:
#         print('\n')
#         print(busi)

#         id_for_rvws = 'tora-tora-sushi-san-diego'

#         review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

#         for rvw in review_rpnse['reviews']:
#             return print("\n",rvw)

# def tadokoro():
#     for busi in search_rslts['businesses']:
#         print('\n')
#         print(busi)

#         id_for_rvws = 'sushi-tadokoro-san-diego'

#         review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

#         for rvw in review_rpnse['reviews']:
#             return print("\n",rvw)
        
# def kaki():
#     for busi in search_rslts['businesses']:
#         print('\n')
#         print(busi)

#         id_for_rvws = 'kaki-sushi-san-diego'

#         review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

#         for rvw in review_rpnse['reviews']:
#             return print("\n",rvw)
        
# def ota():
#     for busi in search_rslts['businesses']:
#         print('\n')
#         print(busi)

#         id_for_rvws = 'sushi-ota-san-diego'

#         review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

#         for rvw in review_rpnse['reviews']:
#             return print("\n",rvw)
        
# def urbn():
#     for busi in search_rslts['businesses']:
#         print('\n')
#         print(busi)

#         id_for_rvws = 'urbn-sushi-san-diego'

#         review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

#         for rvw in review_rpnse['reviews']:
#             return print("\n",rvw['text'])

# print(urbn())
# print(toratora())
# print(tadokoro())
# print(kaki())
# print(ota())
# print(tanuki())

# reviews_coll = [toratora(),urbn(),ota(),kaki(),tadokoro(),kaki(),tanuki()]
# df = pd.DataFrame.from_dict(reviews_coll)
# df.to_csv('rvws.txt',sep = '\t', index = False)


def urbn():
    for busi in search_rslts['businesses']:
        print('\n')
        print(busi)

        id_for_rvws = 'urbn-sushi-san-diego'

        review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

        for rvw in review_rpnse['reviews']:
            return rvw

urban = pd.DataFrame.from_dict(urbn())
urban.to_csv('urban.txt', sep = '\t', index = False)

def toratora():
    for busi in search_rslts['businesses']:
        print('\n')
        print(busi)

        id_for_rvws = 'tora-tora-sushi-san-diego'

        review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

        for rvw in review_rpnse['reviews']:
            return rvw

tora = pd.DataFrame.from_dict(toratora())
tora.to_csv('toratora.txt', sep = '\t', index = False)

def ota():
    for busi in search_rslts['businesses']:
        print('\n')
        print(busi)

        id_for_rvws = 'sushi-ota-san-diego'

        review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

        for rvw in review_rpnse['reviews']:
            return rvw

otaa = pd.DataFrame.from_dict(ota())
otaa.to_csv('ota.txt', sep = '\t', index = False)

def tadokoro():
    for busi in search_rslts['businesses']:
        print('\n')
        print(busi)

        id_for_rvws = 'sushi-tadokoro-san-diego'

        review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

        for rvw in review_rpnse['reviews']:
            return rvw

tado = pd.DataFrame.from_dict(tadokoro())
tado.to_csv('tadokoro.txt', sep = '\t', index = False)

def kaki():
    for busi in search_rslts['businesses']:
        print('\n')
        print(busi)

        id_for_rvws = 'kaki-sushi-san-diego'

        review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

        for rvw in review_rpnse['reviews']:
            return rvw

kak = pd.DataFrame.from_dict(kaki())
kak.to_csv('kaki.txt', sep = '\t', index = False)

def tanuki():
    for busi in search_rslts['businesses']:
        print('\n')
        print(busi)

        id_for_rvws = 'tanuki-san-diego'

        review_rpnse = yelp_api_instance.reviews_query(id = id_for_rvws)

        for rvw in review_rpnse['reviews']:
            return rvw

tanu = pd.DataFrame.from_dict(tanuki())
tanu.to_csv('tanuki.txt', sep = '\t', index = False)

# Using pandas 

rslt_df = pd.DataFrame.from_dict(search_rslts['businesses'])
rslt_df.to_csv('Resturants.csv', index = False)


resturant_list = ['tora-tora-sushi-san-diego','sushi-tadokoro-san-diego'
                      ,'kaki-sushi-san-diego','sushi-ota-san-diego'
                      ,'tanuki-san-diego','urbn-sushi-san-diego']


## Text analysis using tags 

urban_reviews = open('urban.txt')
stopwords = stopwords.words('english')


# for review in urban_reviews:
#     print('\n')
#     # print(review)
#     tokens = nltk.word_tokenize(review)
#     # print(tokens)
#     pos_tags = nltk.pos_tag(tokens)
#     new_txt = []
#     for tag in pos_tags:
#         if tag[1] == 'NN' or tag[1] == 'NNP' or tag[1] == 'NNS':
#             print(tag)
#         if tag[0] not in stopwords:
#             new_txt.append(tag[0])            
#     print("\nOriginal")
#     print(review)
#     print("\nNew")
#     print(" ".join(new_txt))


## Sentiment scores

urban_rvws = open('urban.txt')

for review in urban_rvws:
    sentiment_score = analyzer.polarity_scores(review)
    print('\n')
    print(review)
    print('URBN Sushi score:', sentiment_score)

tanuki_rvws = open('tanuki.txt')

for review in tanuki_rvws:
    sentiment_score = analyzer.polarity_scores(review)
    print('\n')
    print(review)
    print('Tanuki score:',sentiment_score)

otaa_rvws = open('ota.txt')

for review in otaa_rvws:
    sentiment_score = analyzer.polarity_scores(review)
    print('\n')
    print(review)
    print('Sushi Ota score:',sentiment_score)

kaki_rvws = open('kaki.txt')

for review in kaki_rvws:
    sentiment_score = analyzer.polarity_scores(review)
    print('\n')
    print(review)
    print('Kaki Sushi score:',sentiment_score)

tadokoro_rvws = open('tadokoro.txt')

for review in tadokoro_rvws:
    sentiment_score = analyzer.polarity_scores(review)
    print('\n')
    print(review)
    print('Sushi Tadokoro score:',sentiment_score)

tora_rvws = open('toratora.txt')

for review in tora_rvws:
    sentiment_score = analyzer.polarity_scores(review)
    print('\n')
    print(review)
    print('Tora Tora Sushi score:',sentiment_score)
