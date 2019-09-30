# from igramscraper.instagram import Instagram
from igramscraper.deskgram import Deskgram
import pprint as pp
import traceback

instagram = Instagram()
instagram.with_credentials('username', 'password')
instagram.login()
for id in range(1, 10):
    try:
        account = instagram.get_account_by_id(id)
        print('Id: ', account.identifier)
        print('Username: ', account.username)
        print('Full name: ', account.full_name)
        print('Biography: ', account.biography)
        print('Number of followers: ', account.followed_by_count)
        # print(account)
        print('========')
    except Exception as e:
        traceback.print_exc()

deskgram = Deskgram()
for id in range(1, 10):
    try:
        account = deskgram.get_account_by_id(id)
        print('Id: ', account.identifier)
        print('Username: ', account.username)
        print('Full name: ', account.full_name)
        print('Biography: ', account.biography)
        print('Number of followers: ', account.followed_by_count)
        # print(account)
        print('========')
    except Exception as e:
        traceback.print_exc()
        
