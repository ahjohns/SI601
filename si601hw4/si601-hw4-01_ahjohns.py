# -*- coding: utf-8 -*-
import facebook, urllib2, json, csv, codecs
from time import sleep
from collections import Counter

### go to https://developers.facebook.com/tools/explorer/
### click 'Get Access Token' on the top-right, check all the permissions for friends (2nd tab), and press submit
### copy the token string in the Access Token text box
### paste it in access_token = ''

##All work is my own, I worked with Elizabeth Kunze to talk about varying approaches to getting the data from the json string
##specifically I discussed my if/else approach for searching for key/value pairs.
##Danny pointed me to the right direction in getting the education data complete.
##csv files are hashtagged out because I didn't want to tragically rewrite my data with by accident


#friendsprofile = codecs.open('friend_profile_ahjohns.csv', 'wb', encoding='utf-8')
#educationprofile  = codecs.open('friend_education_ahjohns.csv', 'wb', encoding='utf-8')
#test = open('test.txt', 'w')
access_token = 'CAACEdEose0cBAF8exs7PDlgdos5Y54ZADtEjBNLOITG03SvmuEpEyDbpOHtL4TJ3mOCZAXM65EsbcI2Ndt1MpS8eBzQRiArwq7hhHUZAoUhguVqpQrg5qd6r3CgKkJjdp69FS5QIURY4OA2MYZCTOZBTpMVZBbOVX9K72qZCKZCB7xVZASWGg8xIfwMCh7fLV4kgZD'
### use Graph API to get friends
graph = facebook.GraphAPI(access_token)
profile = graph.get_object('me')
friends = graph.get_connections('me', 'friends')

for friend in friends['data']:
    #print friend['id'], friend['name']

    ### the url to get friend information
    url = 'https://graph.facebook.com/%s?access_token=%s&fields=gender,birthday,hometown,location,education,checkins' % (friend['id'], access_token)

    ### do something here to get the response json string from the api
    response = urllib2.urlopen(url)
    response_string = json.load(response)

    #some stuff I tried

    # friend_idlist = []
    # school_id = []
    # school_name = []
    # school_type = []

    # test1 = json.dump(response)
    # for line in test1:
    #      print line
    #      test.writelines(line +'\n')
    #for key, value in response_string.items():

        # if key == 'id':
        #     count = 1
        #     while True:
        #         friend_id = count
        #         count +=1
        #         print friend_id
        #         break
        # while key == 'id':
        #     friend_ids = count
        #     #friend_ids = str(friend_ids)
        #     count = count + 1
        #     friend_id.append(friend_ids)
        #     break
        # print friend_id
# if key exists in response_string, variable == value, else NULL
    if 'id' in response_string:
        friend_id = response_string['id']
        #friend_idlist.append(friend_id)

    if 'gender' in response_string:
        gender = response_string['gender']
    else:
        gender = 'NULL'

    if 'birthday' in response_string:

        birthyears = str(response_string['birthday'])
        birthyears = birthyears.split('/')
        for birthyear in birthyears:
            if len(birthyear) == 4:
                birthyear = birthyear
            else:
                birthyear = 'NULL'
    else:
        birthyear = 'NULL'

    if 'hometown' in response_string:
        hometown_id = response_string['hometown']['id']
        hometown_name = response_string['hometown']['name']
    else:
        hometown_id = 'NULL'
        hometown_name = 'NULL'

    if 'location' in response_string:
        location_id = response_string['location']['id']
        location_name = response_string['location']['name']
    else:
        location_id = 'NULL'
        location_name = 'NULL'

    if 'checkins' in response_string:
        #checkins = response_string['checkins']['paging']['next']
        checkins = response_string['checkins']['data']
        checkins = len(checkins)
        checkins = str(checkins)
    else:
        checkins = 'NULL'

#gets the max length on education key, returning the values in range. Hat-Tip Danny
    if 'education' in response_string:
        max_edu = len(response_string['education'])
        for i in range(0, max_edu):
            school_id = response_string['education'][i]['school']['id']
            school_name = response_string['education'][i]['school']['name']
            school_type = response_string['education'][i]['type']

#write out education file in utf8

            #education_out = csv.writer(educationprofile, delimiter=',')
            #education_out.writerow([friend_id.encode('utf8'), school_id.encode('utf8'), school_name.encode('utf8'), school_type.encode('utf8')])

#some other stuff /test
    # else:
    #      school_id = 'NULL'
    #      school_name = 'NULL'
    #      school_type = 'NULL'
    #print friend_id

#write out the profile data in utf8
    #profile_out = csv.writer(friendsprofile, delimiter=',')
    #profile_out.writerow([friend_id.encode('utf8'), gender.encode('utf8'), birthyear.encode('utf8'), hometown_id.encode('utf8'), hometown_name.encode('utf8'), location_id.encode('utf8'), location_name.encode('utf8'), checkins.encode('utf8')])




    ### stop a while
    sleep(5)