import praw
from psaw import PushshiftAPI
import pandas as pd

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Python:CRE-Scraper-#:v1.0.1 (by /u/CRE-Developer')
api = PushshiftAPI(reddit)
subreddit_df = pd.read_csv("SubredditMap.csv")
counter = 1

CoinID_list = []
CoinName_list = []
CoinSymbol_list = []
Subreddit_list = []
PostID_list = []

for ind in subreddit_df.index:
    print(counter)
    counter = counter + 1

    coin_id = subreddit_df['CoinID'][ind]
    coin_name = subreddit_df['CoinName'][ind]
    coin_symbol = subreddit_df['CoinSymbol'][ind]
    subreddit = subreddit_df['Subreddit'][ind]

    pushshift_list = list(api.search_submissions(subreddit=subreddit,
                                                 filter=['id']))

    for ID in pushshift_list:
        CoinID_list.append(coin_id)
        CoinName_list.append(coin_name)
        CoinSymbol_list.append(coin_symbol)
        Subreddit_list.append(subreddit)
        PostID_list.append(str(ID))

list_of_tuples = list(zip(CoinID_list, CoinName_list, CoinSymbol_list, Subreddit_list, PostID_list))
final_df = pd.DataFrame(list_of_tuples, columns=['CoinID', 'CoinName', 'CoinSymbol', 'Subreddit', 'PostID'])
final_df.to_csv("AllPostIDs_df.csv")