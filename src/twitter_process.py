#Access Twitter API
######################

import twitter  # pip install twitter


def oauth_login():
    consumer_key = '2mQXmAHdjUpEAFot3MomS3vsy'
    consumer_secret = 'T7cfTwSEtsLRh2Gsx7f5z4wA9PhvP09eqnuDP0oAS1kV6HPRFm'
    access_token = '2790391620-gm2N85wEpOpkCUawd5CR4FJFINqkwVDmffujqxO'
    access_token_secret = 'DbcsV2KH6Wx5HpdmjTrbCP7R9df2urxJk1cn1Fcw1L4nU'

    auth = twitter.oauth.OAuth(access_token, access_token_secret,
                               consumer_key, consumer_secret)

    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


twitter_api = oauth_login()

print(twitter_api)

# ############################
#
#
# # Avoiding Rate Limit and Other Errors
# #####################################
# import sys
# import time
# from urllib3.exceptions import HTTPError
# from http.client import BadStatusLine
# import json
#
# def make_twitter_request(twitter_api_func, max_errors=10, *args, **kw):
#     def handle_twitter_http_error(e, wait_period=2,
#             sleep_when_rate_limited=True):
#
#         if wait_period > 3600:  # Seconds
#             print(sys.stderr, 'Too many retries. Quitting.')
#             raise e
#
#         if e.e.code == 401:
#             print(sys.stderr, '401 Error (Not Authorized)')
#             return None
#         elif e.e.code == 404:
#             print(sys.stderr, '404 Error (Not Found)')
#             return None
#         elif e.e.code == 429:
#             print(sys.stderr, '429 Error (Rate Limit Exceeded)')
#             if sleep_when_rate_limited:
#                 print(sys.stderr, "Retry in 15 minutes")
#                 sys.stderr.flush()
#                 time.sleep(60 * 15 + 5)
#                 print(sys.stderr, 'End of 15 mins.... Trying again.')
#                 return 2
#             else:
#                 raise e
#         elif e.e.code in (500, 502, 503, 504):
#             print(sys.stderr, 'Encountered %i Error. Retrying in %i seconds' % \
#             (e.e.code, wait_period))
#             time.sleep(wait_period)
#             wait_period *= 1.5
#             return wait_period
#         else:
#             raise e
#
#     wait_period = 2
#     error_count = 0
#
#     while True:
#         try:
#             return twitter_api_func(*args, **kw)
#         except twitter.api.TwitterHTTPError as e:
#             error_count = 0
#             wait_period = handle_twitter_http_error(e, wait_period)
#             if wait_period is None:
#                 return
#         except HTTPError as e:
#             error_count += 1
#             print(sys.stderr, "HTTPError encountered. Continuing.")
#             if error_count > max_errors:
#                 print(sys.stderr, "Too many consecutive errors")
#                 raise
#         except BadStatusLine as e:
#             error_count += 1
#             print(sys.stderr, "BadStatusLine encountered. Continuing.")
#             if error_count > max_errors:
#                 print(sys.stderr, "Too many consecutive errors")
#                 raise
#
# #####################################


tweets_per_query = 100
tweet_list = []
last_id = None
max_id = -1

try:
    while True:
        if len(tweet_list) == 0:
            query = twitter_api.search.tweets(q = "#NVDA", count=tweets_per_query)
        else:
            query = twitter_api.search.tweets(
                q="#NVDA", count=tweets_per_query, max_id=str(max_id-1)
            )
        # max_id = query['statuses'][-1]['id']
        # last_id = query['statuses'][0]['id']
        for result in query['statuses']:
            if result['text'] not in tweet_list:
                tweet_list.append(result['text'])
            # if result['id'] < last_id or last_id == 0:
            #     last_id = result['id']
            if result['id'] < max_id or max_id == -1:
                max_id = result['id']
            if len(tweet_list) >= 600:
                break
except Exception as e:
    print (e)

p = query['statuses'][00]['text']


# api = twitter.Api(consumer_key='2mQXmAHdjUpEAFot3MomS3vsy',
#   consumer_secret='T7cfTwSEtsLRh2Gsx7f5z4wA9PhvP09eqnuDP0oAS1kV6HPRFm',
#   access_token_key='2790391620-gm2N85wEpOpkCUawd5CR4FJFINqkwVDmffujqxO',
#   access_token_secret='DbcsV2KH6Wx5HpdmjTrbCP7R9df2urxJk1cn1Fcw1L4nU')
#
# print(api.VerifyCredentials())

