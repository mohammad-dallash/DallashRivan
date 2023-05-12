from functools import reduce
import pandas as pd
import numpy as np
import re


df = pd.read_csv('Features.csv')
#1.	Replace the empty values in the actions column with zero
df.replace({'actions': np.nan}, {'actions': 0}, inplace=True)
print(df['actions'])

#2.	Print the summation of the followers for all tweets by using reduce stream
sum = reduce(lambda x, y: x + y, df['followers'])
print(sum)
 #3
filtered = df[(df['location'] == 'UK') ]

id_values = filtered['Id'].tolist()

print(id_values)
# 4. Print how many spam tweets there are in this data set

spam_count = len(df[df['Type'] == 'Spam'])
print(f"Number of spam tweets: {spam_count}")


# 5. Print the tweet IDs of tweets with more than 5000 followers
high_follower_tweets = df[df['followers'] > 5000]
print("IDs of tweets with more than 5000 followers:")
print(high_follower_tweets['Id'].tolist())

# 6. Print all tweet IDs that include '#' in the tweet text
hashtag_tweets = df[df['Tweet'].str.contains('#')]
print("IDs of tweets with hashtags:")
print(hashtag_tweets['Id'].tolist())

# 7. Print all tweet IDs that include a URL in the tweet text using regex
url_tweets = df[df['Tweet'].str.contains(r'(http[s]?://\S+)')]
print("IDs of tweets with URLs:")
print(url_tweets['Id'].tolist())