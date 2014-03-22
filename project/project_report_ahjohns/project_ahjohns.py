import csv, json, urllib2
from time import sleep



def main():

#Open/read Genderstats.csv, grab JSON responses for 2011/2012 from foreignassistance.gov API
#Filter by type of transaction, sector, and year
    opengenderstats = open('Genderstats_Data.csv', 'rb')
    usaidanalysis = open('usaidanalysis.csv', 'wb')
    genderstats = csv.reader(opengenderstats)
    assistanceurl = "http://foreignassistance.gov/dashboardservice/dashboardserviceapi.svc/JSON/GetData?type=spent&filter=sector&option=maternal&year=2011"
    assistance2url = "http://foreignassistance.gov/dashboardservice/dashboardserviceapi.svc/JSON/GetData?type=spent&filter=sector&option=maternal&year=2012"
    response = urllib2.urlopen(assistanceurl)
    response_string = json.load(response)
    response2 = urllib2.urlopen(assistance2url)
    response_string2 = json.load(response2)

#Create lists for countrynames, each statistic(7), and lists for the parsing of each JSON string.
#A lot of lists I know.
    testdict = {}
    usaidlist = []
    usaidlist2 = []
    countrylistaid = []
    countrylistaid2 = []
    countrylist = []
    deathlist2012 = []
    mortalitylist2012 = []
    mleavelist2012 = []
    prenatallist2012 = []
    contraprevlist2012 = []
    contrametlist2012 = []
    infantmortlist2012 = []
    aidamountlist = []
    aidamountlist2 = []


#Get the data for 2011
#max_data technique was originally done for HW 4, and originally it was Danny Wu who pointed me to the right direction.
#For item in the range of the length of max JSON string, assign variables for aid and countries, create temp dictionary for those keys/values
#Append temp dictionary to first initial usaidlist
    max_data = len(response_string['JSONDataResult'])
    for i in range(0, max_data):
        #how do i add up the values?
        temp = {}
        unicountry = response_string['JSONDataResult'][i]['BenefitingLocation']
        country = str(unicountry)
        countrylistaid.append(country)
        year = response_string['JSONDataResult'][i]['FiscalYear']
        sector = response_string['JSONDataResult'][i]['Sector']
        aidamount = response_string['JSONDataResult'][i]['Amount']
        agency = response_string['JSONDataResult'][i]['AgencyName']
        temp[country] = aidamount
        usaidlist.append(temp)


#Get the data for 2012
#max_data technique was originally done for HW 4, and originally it was Danny Wu who pointed me to the right direction.
#For item in the range of the length of max JSON string, assign variables for aid and countries, create temp dictionary for those keys/values
#Append temp dictionary to second initial usaidlist
    max_data2 = len(response_string2['JSONDataResult'])
    for i in range(0, max_data2):
        temp2 = {}
        unicountry2 = response_string2['JSONDataResult'][i]['BenefitingLocation']
        country2 = str(unicountry2)
        countrylistaid2.append(country2)
        year2 = response_string2['JSONDataResult'][i]['FiscalYear']
        sector2 = response_string2['JSONDataResult'][i]['Sector']
        aidamount2 = response_string2['JSONDataResult'][i]['Amount']
        agency2 = response_string2['JSONDataResult'][i]['AgencyName']
        temp2[country2] = aidamount2
        usaidlist2.append(temp2)


#I had some problems figuring out how to do this next step but used http://stackoverflow.com/questions/19330184/python-merging-multiple-dictionaries-in-a-list-with-an-update-of-values
#As a guide.  I found it helpful, and was able to get the results through trial/error
#2011-2012: Add similar key/value pairs from both usaidlists, assign to dictionaries
    usaiddict = {}
    for i in usaidlist:
        for country, aidamount in i.items():
            if country not in i.items():
                usaiddict[country] = aidamount
            else:
                aidtotal = usaiddict[country] + aidamount
                usaiddict[country] = aidtotal

    usaiddict2 = {}
    for i2 in usaidlist2:
        for country2, aidamount2 in i2.items():
            if country2 not in i2.items():
                usaiddict2[country2] = aidamount2
            else:
                aidtotal2 = usaiddict2[country2] + aidamount2
                usaiddict2[country2] = aidtotal2

#Iterate through lines of the Genderstats CSV.
#If/elif statements to find the right statistics
#Within each statement, if/else statements to find data for 2011, convert to 'Null' if doesn't exist
#Append each stat to a separate list. Append countries to list (only had to append within one if/elif stat search

    for line in genderstats:
        if line[2] == 'Number of maternal deaths':
            if line[55] == '':
                 line[55] = 'Null'
                 maternaldeath2012 = line[55]
                 countrylist.append(line[0])
            else:
                 maternaldeath2012 = line[55]
            deathlist2012.append(maternaldeath2012)
            #countrylist.append(line[0])
            #print line[2], line[55]
        elif line[2] == "Mortality rate, female child (per 1,000 female children age one)":
            #print line[2]
            if line[55] == '':
                 line[55] = 'Null'
                 maternalmortality2012 = line[55]
            else:
                 maternalmortality2012 = line[55]
            mortalitylist2012.append(maternalmortality2012)
            #countrylist.append(line[0])
        elif line[2] == "Maternal leave benefits (% of wages paid in covered period)":
            if line[55] == '':
                 line[55] = 'Null'
                 maternalleave2012 = line[55]
            else:
                 maternalleave2012 = line[55]
            mleavelist2012.append(maternalleave2012)
            #countrylist.append(line[0])

        elif line[2] == "Pregnant women receiving prenatal care (%)":
            if line[55] == '':
                 line[55] = 'Null'
                 prenatal2012 = line[55]
            else:
                 prenatal2012 = line[55]
            prenatallist2012.append(prenatal2012)
            #countrylist.append(line[0])
        elif line[2] == "Contraceptive prevalence (% of women ages 15-49)":
            if line[55] == '':
                 line[55] = 'Null'
                 contraceptiveprev2012 = line[55]
            else:
                 contraceptiveprev2012 = line[55]
            contraprevlist2012.append(contraceptiveprev2012)
            #countrylist.append(line[0])
        elif line[2] == "Met need for contraception (% of married women ages 15-49)":
            if line[55] == '':
                 line[55] = 'Null'
                 contraceptivemet2012 = line[55]
            else:
                 contraceptivemet2012 = line[55]
            contrametlist2012.append(contraceptivemet2012)
            #countrylist.append(line[0])
        elif line[2] == "Mortality rate, infant (per 1,000 live births)":
            if line[55] == '':
                 line[55] = 'Null'
                 infantmortality2012 = line[55]
            else:
                 infantmortality2012 = line[55]
            infantmortlist2012.append(infantmortality2012)

        else:
            continue

#Change the countrylist names that are different from the usaid countries to get accurate results for analysis
    countrylist[49] = 'Democratic Republic of Congo'
    countrylist[224] = 'Sudan, Pre-2011 Election'
    #countrylist = sorted(countrylist)

#Match item of countrylist with key of the dictionaries for 2011/2012 US Aid. Append values to list, 'Null' if no country match
    for count in countrylist:
        tempdict2 = {}
        if count not in tempdict2:
            tempdict2[count] = 'Null'
            for k, v in usaiddict.items():
                if k == count:
                    tempdict2[count] = v
        for k, v in tempdict2.items():
            aidamountlist.append(v)

    for count in countrylist:
        tempdict3 = {}
        if count not in tempdict3:
            tempdict3[count] = 'Null'
            for k2, v2 in usaiddict2.items():
                if k2 == count:
                    tempdict3[count] = v2
            for k2, v2 in tempdict3.items():
                aidamountlist2.append(v2)

#Zip all the lists
    zips = zip(countrylist, deathlist2012, mortalitylist2012, mleavelist2012,prenatallist2012,contraprevlist2012,contrametlist2012,infantmortlist2012, aidamountlist, aidamountlist2)


#Write out rows and items of zipped list
    csv_out=csv.writer(usaidanalysis)
    csv_out.writerow(['Country Name', 'Number of maternal deaths (2011)', 'Mortality rate, female child (per 1,000 female children age one)(2011)', 'Maternal leave benefits (% of wages paid in covered period)(2011)', 'Pregnant women receiving prenatal care (%)(2011)', 'Contraceptive prevalence (% of women ages 15-49)(2011)',
   'Met need for contraception (% of married women ages 15-49)(2011)', 'Mortality rate, infant (per 1,000 live births)(2011)', 'US Aid Amount(2011)', 'US Aid Amount(2012)'])
    for item in zips:
        for i in item:
            i = i.replace('"', '')
            #print i
        csv_out.writerow(item)

    sleep(3)
if __name__ == '__main__':
  main()