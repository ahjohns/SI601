import re
#import panda
import csv

def main():
    #open input, output files. read lines of input file
    input_file = open("access_log.txt", "rU")
    invalid_access = open("invalid_access_log_ahjohns.txt", "w")
    valid_log = open("valid_log_summary_ahjohns.txt", "w")
    access_lines = input_file.readlines()
    input_file.close()


#create list for invalid lines, two dictionaries for valid lines
    invalid = []
    access = {}
    access2 = {}


    for line in access_lines:
#split new lines, conversion to strings, split at spaces
        #line = re.split('\s+', line)
        #kunze
        # if re.search(r'GET|POST', line) and re.search(r'^https?://[a-zA-Z]+', line1[6]) and re.search(r'" 200 ', line):
        #     f = f + 1
        #     line3 = line1[3].split(':')
        #     logdate = line3[0].strip('[')
        #     m = re.search(r'\.([a-zA-Z]+)/', line1[6])\.(\D{,3})/$
#search for lines gets/posts + 200 + starts with http or https
#finds all domains, then splits the date at :, makes sure the domain is lower case
         if re.search(r'"GET|"POST', line) and re.search(r'" 200', line) and re.search(r'https://[a-zA-Z]+|http://[a-zA-Z]+', line):
             #line = re.split('\s+', line)
            # print line
             domains = re.findall(r'\.([a-zA-Z]+)/', line)#, re.IGNORECASE)
             if domains:
                line = re.split('\s+', line)
                dates = re.split(':', line[3])
                date = dates[0].strip('[')
                domain = domains[0]
                domain = domain.lower()
#creates keys for dates and domains and their values in first dict
                access['date'] = date
                access['domain'] = domain
#for each key in first dict, adds key to second dict, counts the domains for each date key. counts is now the value for the nested dictionary
                for key in access:
                    datekey = date
                    domainkey = domain
                    if datekey in access2:
                        if domainkey in access2[datekey]:
                            access2[datekey][domainkey] += 1
                        else:
                            access2[datekey][domainkey] = 1
                    else:
                        access2[datekey] = {}
                        access2[datekey][domainkey] = 1


                else:
                    continue


         else:
#added invalid lines to list, writes to file and adds newline. I also tried joining the list with .join, clearly didn't work
            #but I hope you can see what I was trying to do
            # invalidtemp = invalid
            # invalidtemp = str(invalidtemp)
            # invalidtemp = (''.join(invalidtemp))
            # print invalidtemp
            # #     invalidstring = str(inv) + '\t'
            # #     print type(invalidstring)
            if line == '':
                continue
            invalid.append(line)
            invalid_access.writelines(line)

#this code is sorting for keys for the big dictionary, it was supposed to put in a new line for formatting issues, but the display
        #is different depending on the what editor or display you use
    dates = access2.keys()
    sort_dates = sorted(dates)
    for date in sort_dates:
        out_string = str(date) + "\t"
        out_string = out_string# + "\n"
        pairs = access2[date]
        domains = pairs.keys()
        ##print domains
        sort_domains = sorted(domains)
        for d in sort_domains:
            out_string += str(d) + ":" + str(pairs[d]) + "\t"
        
        print out_string
        valid_log.writelines(out_string + "\n")

if __name__ == '__main__':
   main()