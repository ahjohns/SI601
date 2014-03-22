# -*- coding: utf-8 -*-
import facebook, urllib2, json, csv, codecs
from time import sleep
from collections import Counter

### go to https://developers.facebook.com/tools/explorer/
### click 'Get Access Token' on the top-right, check all the permissions for friends (2nd tab), and press submit
### copy the token string in the Access Token text box
### paste it in access_token = ''
friendsprofile = codecs.open('friend_profile_ahjohns2.csv', 'wb', encoding='utf-8')
educationprofile  = codecs.open('friend_education_ahjohns2.csv', 'wb', encoding='utf-8')
test = open('test.txt', 'w')
access_token = 'CAACEdEose0cBAJBEHxt3OOzXoLeRqm9xKyXSYGc5fvZCPL5JfU5B5tfwPHmbs0h0ODbyQnpsqIevX44Ohaodw8CUArGi5zxn0FqnxyBbKRYnCZA2Cd51PspQ08L0s3ofFZAS8ZCUZCgvPSqJ5ZCC4ps5hxO41h2QsKe2B6l158dfIrsksWxlEqTRitPfWdL2EZD'
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

    if 'education' in response_string:
        max_edu = len(response_string['education'])
        for i in range(0, max_edu):
            school_id = response_string['education'][i]['school']['id']
            school_name = response_string['education'][i]['school']['name']
            school_type = response_string['education'][i]['type']
            education_out = csv.writer(educationprofile, delimiter=',')
            education_out.writerow([unicode(friend_id).encode('utf8'), unicode(school_id).encode('utf8'), unicode(school_name).encode('utf8'), unicode(school_type).encode('utf8')])
    # else:
    #      school_id = 'NULL'
    #      school_name = 'NULL'
    #      school_type = 'NULL'
    print friend_id
    profile_out = csv.writer(friendsprofile, delimiter=',')
    profile_out.writerow([unicode(friend_id).encode('utf8'), unicode(gender).encode('utf8'), unicode(birthyear).encode('utf8'), unicode(hometown_id).encode('utf8'), unicode(hometown_name).encode('utf8'), unicode(location_id).encode('utf8'), unicode(location_name).encode('utf8'), unicode(checkins).encode('utf8')])

    #education_out = csv.writer(educationprofile, delimiter=',')
    #education_out.writerow([friend_id.encode('utf8'), school_id.encode('utf8'), school_name.encode('utf8'), school_type.encode('utf8')])


    ### stop a while
    sleep(2)