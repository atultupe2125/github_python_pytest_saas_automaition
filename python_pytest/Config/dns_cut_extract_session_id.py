#This class file is use to extract the TLTSID from the log file and find the unique
#TLTSID and then use the same to test the DNS cut test case
class dns_cut_extract_session:
 def dns_cust_extract_session(self):
    datalog = []
    # open the log file in read write mode
    with open('/Users/atultupe/Documents/Tealeaf/TLSaaS/dns_cut_files/TLSaaSFeeder_20221011.log', 'rt') as f:
        data = f.readlines()
    for line in data:
        # Filter only the ines contaning TLTSID and append it to python list (datalog)
        if 'New TLTSID:' in line:
            datalog.append(line)
    # open file in write mode
    with open(r'/Users/atultupe/Documents/Tealeaf/TLSaaS/TLTSID_EXTRACTED.txt', 'w') as fp:
        for item in datalog:
            # below code is data processing command use to filter out only the New TLSSID from the data
            index = int(item.find('New'))
            item = item.replace(item[:index], "")
            item = item.replace("New", "")
            index = int(item.find('D:'))
            item = item.replace(item[:index], "")
            item = item.replace(item[:3], "")
            fp.write(str(item))
    datalog = []
    a_file = open(r'/Users/atultupe/Documents/Tealeaf/TLSaaS/TLTSID_EXTRACTED.txt')
    number_of_lines = 1000
    for i in range(number_of_lines):
        line = a_file.readline()
        line = line[0:32]
        datalog.append(line)
    unique_list = []
    for x in datalog:
        if x not in unique_list:
            unique_list.append(x)
            print(unique_list)
    length = len(unique_list)
    return length