import pandas as pd
import praw
import datetime as dt

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='Python:CRE-Scraper-#:v1.0.1 (by /u/CRE-Developer')

posts_df = pd.read_csv("AllPostIDs_input.csv")

CoinID_list = []
CoinName_list = []
CoinSymbol_list = []
SubReddit_list = []
PostID_list = []
PostFullname_list = []
Title_list = []
Text_list = []
AuthorUsername_list = []
AuthorID_list = []
AuthorFullname_list = []
SubmissionURL_list = []
Permalink_list = []
NumComments_list = []
Score_list = []
UpvoteRatio_list = []
Distinguished_list = []
Edited_list = []
IsSelfPost_list = []
IsLocked_list = []
IsNSFW_list = []
IsSpoiler_list = []
IsStickied_list = []
PostTimestamp_list = []

loop_start = dt.datetime.utcnow()

for ind in posts_df.index:
    post_id = posts_df['PostID'][ind]
    submission = reddit.submission(id=post_id)
    author = submission.author

    CoinID_list.append(posts_df['CoinID'][ind])
    CoinName_list.append(posts_df['CoinName'][ind])
    CoinSymbol_list.append(posts_df['CoinSymbol'][ind])
    SubReddit_list.append(posts_df['Subreddit'][ind])
    PostID_list.append(post_id)
    PostFullname_list.append(submission.fullname)
    Title_list.append(submission.title)
    Text_list.append(submission.selftext)

    if author is None:
        AuthorUsername_list.append(None)
        AuthorID_list.append(None)
        AuthorFullname_list.append(None)
    else:
        AuthorUsername_list.append(author.name)
        try:
            AuthorID_list.append(author.id)
        except:
            AuthorID_list.append(None)

        try:
            AuthorFullname_list.append(author.fullname)
        except:
            AuthorFullname_list.append(None)

    SubmissionURL_list.append(submission.url)
    Permalink_list.append(submission.permalink)
    NumComments_list.append(submission.num_comments)
    Score_list.append(submission.score)
    UpvoteRatio_list.append(submission.upvote_ratio)
    Distinguished_list.append(submission.distinguished)
    Edited_list.append(submission.edited)
    IsSelfPost_list.append(submission.is_self)
    IsLocked_list.append(submission.locked)
    IsNSFW_list.append(submission.over_18)
    IsSpoiler_list.append(submission.spoiler)
    IsStickied_list.append(submission.stickied)
    PostTimestamp_list.append(submission.created_utc)

loop_end = dt.datetime.utcnow()

print(loop_end - loop_start)

list_of_tuples = list(zip(CoinID_list,
                          CoinName_list,
                          CoinSymbol_list,
                          SubReddit_list,
                          PostID_list,
                          PostFullname_list,
                          Title_list,
                          Text_list,
                          AuthorUsername_list,
                          AuthorID_list,
                          AuthorFullname_list,
                          SubmissionURL_list,
                          Permalink_list,
                          NumComments_list,
                          Score_list,
                          UpvoteRatio_list,
                          Distinguished_list,
                          Edited_list,
                          IsSelfPost_list,
                          IsLocked_list,
                          IsNSFW_list,
                          IsSpoiler_list,
                          IsStickied_list,
                          PostTimestamp_list))

post_data_df = pd.DataFrame(list_of_tuples, columns=['CoinID',
                                                     'CoinName',
                                                     'CoinSymbol',
                                                     'Subreddit',
                                                     'PostID',
                                                     'PostFullname',
                                                     'Title',
                                                     'Text',
                                                     'AuthorUsername',
                                                     'AuthorID',
                                                     'AuthorFullname',
                                                     'SubmissionURL',
                                                     'Permalink',
                                                     'NumComments',
                                                     'Score',
                                                     'UpvoteRatio',
                                                     'Distinguished',
                                                     'Edited',
                                                     'IsSelfPost',
                                                     'IsLocked',
                                                     'IsNSFW',
                                                     'IsSpoiler',
                                                     'IsStickied',
                                                     'PostTimestamp'])

post_data_df.to_csv("AllRedditPostData.csv")