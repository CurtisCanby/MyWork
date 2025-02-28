#FILE HANDLING AND DATA PROCESSING
import re
pathtofile = 'C:/Users/16812/OneDrive/Desktop/access.log'

def loglist(path):
    log = []
    newlist = []
    pattern = re.compile(r'\b141\.98\.11\.114\b')

    # Makes a list of log entries
    with open(pathtofile, 'r') as file:
        for line in file:
            log.append(line)
            
    # Uses the regex pattern to ignore everything that is botpoke
    for element in log:
        if not pattern.search(element):
            newlist.append(element)
    return newlist

def makeiplist(log):
    setofIPs = set()
    NoDuplicates = []
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

    # Makes a list of ips from a log that contains no duplicates
    for element in log:
        ip_address = re.search(ip_pattern, element).group()
        setofIPs.add(ip_address)
    
    for i in setofIPs:
        NoDuplicates.append(i)
    return NoDuplicates

nobotpokes = loglist(pathtofile)
print(len(nobotpokes))
iplist = makeiplist(nobotpokes)
print(iplist)