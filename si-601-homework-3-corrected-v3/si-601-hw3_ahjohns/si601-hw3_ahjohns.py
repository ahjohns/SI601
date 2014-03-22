#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re, json, time, itertools, urllib2

import pydot

def main():
#open link using urllib, read the html, decode/encode with unicode and writing lines to step 1,
#create files for step 2 and step 3. open step 1 using BeautifulSoup
    response = urllib2.urlopen('http://www.imdb.com/search/title?at=0&sort=num_votes&count=100')
    step1 = open("step1.html", "w")
    step2 = open("step2.txt", "w")
    #step3 = open("step3.txt", "w")
    step3r = open('step3.txt', "rU")
    step4 = open("step4.txt", "w")
    step3rstring = step3r.readlines()


    html_doc = response.read().decode('utf-8')
    utfhtml_doc = html_doc.encode('utf-8')
    step1.writelines(utfhtml_doc)
    soup = BeautifulSoup(open("step1.html"))

#create three lists for ids, ratings and titles
    ident = []
    rat = []
    title = []
    movielist = []
    actorlist = []


#compile a tags with href + titles, append instances to corresponding lists
    for ids in soup.find_all('a', {'href': re.compile('/title/.+/')}):#, title != 'Delete'):
        titles = ids.get('title')
        if titles == None:
            continue
        if titles == 'Delete':
            continue
        else:
            id = ids.string
            id = ids.get('href')
            id = id.split('/')
            id = id[2]
        title.append(titles)
        ident.append(id)

#find all td tags for number class, convert to a string, and append to a list
    for ratings in soup.find_all("td", {"class":"number"}):
        rating = ratings.string
        rating = rating.replace('.', '')
        rat.append(rating)

#zip the three lists into one single list, join the items together, encoding them as unicode 8 and a new line
    zips = zip(ident, rat, title)
    for item in zips:
        item = '\t'.join(item)
        item = item + '\t'
        step2.writelines(item.encode('utf8') + '\t' + '\n')

    #for item in ident:
#gets the url for each string of each it, reads, decodes/encodes in UTF8, then writes to step 3
        # apiresponse = urllib2.urlopen('http://omdbapi.com/?i=' + str(item)).read()
        # #time.sleep(5)
        # apipageinfo = apiresponse.decode('utf-8')
        # apipageinfo2 = apipageinfo.encode('utf-8')
        # print apipageinfo2
        # step3.writelines(apipageinfo2 + '\n')
        # #print type(jsonoutput)
        # data = json.dumps(jsonoutput)
        # print data
        # # data = str(data)

#iterate through lines in step3.txt, find all actor strings, split into a list, replace and add content, append to a list. Split line to find movies, replace content, add to a list.
    for line in step3rstring:
        matches = re.findall(r'"Actors".*"Plot"', str(line))
        for match in matches:
            match = match.split(':')

            match[1] = match[1].replace(',"Plot"', '')
            match[1] = '[' + match[1] + ']'
            actorlist.append(match[1])

        line = line.split(':')
        line[1] = line[1].replace('"', '').replace(',Year', '')
        movielist.append(line[1])

#zip lists, make a giant list
    zips2 = zip(movielist, actorlist)
    # actordata = json.dumps(actorlist)
    # print actordata
    # print actordata
    # actorlist3.append(actordata)
    # print actorlist3
    #a4 = json.loads(actordata)
    #print a4

    #zips3 = zip(movielist, a4)
    #print zips3.decode('utf8')

    for item in zips2:
        item = '\t'.join(item)
        item = item + '\t'
        item = item.decode('utf8')
        step4.writelines(item.encode('utf8') + '\t' + '\n')

    step4out = open("step4.txt", "rU")
    step4str = step4out.readlines()
    graph = pydot.Dot(graph_type='graph', charset="utf8")
    for actors in step4str:
        #print actors
        #actor = actors.split('\t')
        actor = re.findall(r'".*"', actors)
        for a in actor:
            a = a.decode('utf8')
            a = a.replace('"', '')
            a = a.split(',')
            a = list(itertools.combinations(a, 2))
            for i in a:
                edge = pydot.Edge(i[0], i[1])
                graph.add_edge(edge)

    graph.write_dot('actors_graph_output.dot')

if __name__ == '__main__':
  main()

