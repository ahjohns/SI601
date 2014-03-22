import datetime
import math
import csv 

indicator_data = []
region_data = []
asia = []
europe = []
africa = []
the_americas = []
oceania = []
middle_east = []


input_file = open("world_bank_indicators.txt", "rU")
input_file2 = open("world_bank_regions.txt", "rU")
indicator_lines = input_file.readlines()[1:]
region_lines = input_file2.readlines()[1:]
input_file.close()
input_file2.close()
#  f = open("world_bank_indicators.csv", "wb")
#     for line in f:
#         writer = csv.writer(f)
#         writer.writerows(line[0], line[1], line[4])#

#     csv_in = csv.reader(open("world_bank_indicators.txt", "rb"), delimiter = "\t")
#     csv_out = csv.writer(open("world_bank_indicators.csv", "wb"), delimiter = ",")
#     for line in csv_in:
#         csv_out.writerows([name, line[1], line[4], line[5], line[6], line[9], line[19]])     


country_2000_dict = {}
country_2010_dict = {}

for line in region_lines:
    line = line.strip('\n').split('\t')
    if line[0] == "Asia":
        asia.append(line[2])
    if line[0] == "Europe":
        europe.append(line[2])
    if line[0] == "Africa":
        africa.append(line[2])
    if line[0] == "The Americas":
        the_americas.append(line[2])
    if line[0] == "Oceania":
        oceania.append(line[2])
    if line[0] == "Middle East":
        middle_east.append(line[2])
    print asia
    
for line in indicator_lines:
    if "/2000" in line or "/2010" in line:
        line = line.strip('\n').split('\t')
        if "/2000" in line[1]:
            line[1] = "2000"
        if "/2010" in line[1]:
            line[1] = "2010"
#delete data points
        del line[10:19]
        del line[7:9]
        del line[2:4]
        
        name = line[0]
        date = line[1]
        mobile = line[2].replace(',','').replace('"','').strip()
        if mobile == '':
            continue
        net_user = line[3].replace(',','').replace('"','').strip()
        mortality = line[4].replace(',','').replace('"','').strip()
        if mortality == '':
            continue
        pop = line[5].replace(',','').replace('"','').strip()
        gdp = line[6].replace(',','').replace('"','').strip()
        if gdp == '':
            continue
        line[6] = gdp
        mobile_per_pop = "{0:.5f}".format(float(mobile)/float(pop))
        line.append(str(mobile_per_pop))
        log_gdp = "{0:.5f}".format(math.log(float(gdp)))
        line.append(str(log_gdp))
        log_mortality = "{0:.5f}".format(math.log(float(mortality)))
        line.append(str(log_mortality))
    
        
        if line[0] in africa:
            line.append("Africa")
        elif line[0] in the_americas:
            line.append("The Americas")
        elif line[0] in europe:
            line.append("Europe")
        elif line[0] in asia:
            line.append("Asia")
        elif line[0] in oceania:
            line.append("Oceania")
        elif line[0] in middle_east:
            line.append("Middle East")
            
        if line[6] == '':
            gdp1 = line[6].replace('','0')
            line[6] = gdp1
        
        line[2], line[5] = line[5], line[2]
        line[3], line[5] = line[5], line[3]
        if len(line) == 11:
            indicator_data.append(line)
        indicator_data = sorted(indicator_data, key=lambda line: (line[1], line[10], int(line[6])))
    print indicator_data
        
        
with open('world_bank_indicators.csv', 'wb') as out:
   csv_out=csv.writer(out)
   csv_out.writerow(['Country Name', 'Date', 'Total Population', 'Mobile subscribers', 'Health: mortality under-5', 'Internet users per 100 people', 
   'GDP per capita', 'Mobile subscribers per capita', 'log(GDP per capita)', 'log(Health: mortality under-5)', 'Region'])
   for line in indicator_data:
       csv_out.writerow(line)   


#   for column in region_data:
#         if column[0] == "Asia":
#             asia.append(column[2])
#         if column[0] == "Europe":
#             europe.append(column[2])
#         if column[0] == "Africa":
#             africa.append(column[2])
#         if column[0] == "The Americas":
#             the_americas.append(column[2])
#         if column[0] == "Oceania":
#             oceania.append(column[2])
#         if column[0] == "Middle East":
#             middle_east.append(column[2])
#     print asia

    # region = column[0].strip()
#         country = column[2].strip()
#         print country

# for column in indicator_data:
#     temp_dict = {}
#     year = column[1].split('/')[2]
#     if year == "2000" or year == "2010":
#         name = column[0].strip()
#         date = column[1].strip()
#         mobile = column[4].replace(',','').replace('"','').strip()
#         if mobile == '':
#             continue
#         net_user = column[5].replace(',','').replace('"','').strip()
#         mortality = column[6].replace(',','').replace('"','').strip()
#         if mortality == '':
#             continue
#         pop = column[9].replace(',','').replace('"','').strip()
#         gdp = column[19].replace(',','').replace('"','').strip()
#         if gdp == '':
#             continue
#         mobile_per_pop = "{0:.5f}".format(float(mobile)/float(pop))
#         log_gdp = "{0:.5f}".format(math.log(float(gdp)))
#         log_mortality = "{0:.5f}".format(math.log(float(mortality)))
            
      #   temp_dict["date"] = date
#             temp_dict["mobile"] = mobile
#             temp_dict["net_user"] = net_user
#             temp_dict["mortality"] = mortality
#             temp_dict["pop"] = pop
#             temp_dict["gdp"] = gdp
#             temp_dict["mobile_per_pop"] = mobile_per_pop
#             temp_dict["log_gdp"] = log_gdp
#             temp_dict["log_mortality"] = log_mortality
#             #temp_dict["region"] = region
#         
#             if year == "2000":
#                 country_2000_dict[name] = temp_dict
#             elif year == "2010":
#                 country_2010_dict[name] = temp_dict
#             
#         
#       
#             if name not in country_2010_dict.keys():
#                 continue
#             if name not in country_2000_dict.keys():
#                 continue
#             country_2010_dict['Afghanistan']['region'] = 'Asia'
#             country_2010_dict['Albania']['region'] = 'Europe'
#             country_2000_list = country_2000_dict.items()
#             country_2010_list = country_2010_dict.items()
#             print country_2000_list[0], country_2010_list[0]
         
#Need to figure out how to map correct regions, and if there is no 2000/2010 data for a country how do I skip it               
#  print sorted(country_2010_dict, key=lambda x: (x["date"],x["region"],x["gdp"]))
#     print sorted(country_2000_dict, key=lambda x: (x["date"],x["region"],x["gdp"]))
#Need to figure how to write the dict to csv, one value per line  
# csv_in = csv.reader(open("world_bank_indicators.txt", "rb"), delimiter = "\t")
# csv_out = csv.writer(open("world_bank_indicators.csv", "wb"), delimiter = ",")
#     writer = csv.writer(csv_out)
#     for key, val in sorted(country_2010_dict.items()
#         writer.writerows([key, val])
#     csv_out.close()
# for line in csv_in:
#      csv_out.writerows(["Country Name", "Date", "Mobile subscribers", "Internet users (per 100 people)", "Health: Mortality, under-5", "Total Population", "GDP per capita", "Mobile subscribers per capita", "log(GDP per capita)", "log(Health: mortality under 5)"])    
            