

theFile = open('/var/log/user.log', 'r')
FILE = theFile.readlines()
theFile.close()
calltxt = ""

# Parse log file

for line in FILE:
    calltxt = calltxt + line[int(line.find("connected")):int(line.find("connected")+30)]



print calltxt