import dns.resolver
import dns
import dns.query
import time
import os

class mydig(object):
    def __init__(self, resolverIP):
        self.mResolver = dns.resolver.Resolver()
        self.mResolver.timeout = 0.5
        self.mResolver.lifetime = 0.5
        self.mResolver.nameservers = [resolverIP]

    def getSingleNameResolved(self, domain, queryType):
            try:
                ans = self.mResolver.query(domain, queryType, raise_on_no_answer = False)
            except:
                pass
            else:
                if ans is not None and ans.response.rcode != dns.rcode.NOERROR:
                    return ans

    def getHostName(self, line, key, col):
        return line.strip("}").split(",")[col].split(key+"\":")[1].strip("\"")

def main():
    resolverIP = "8.8.8.8"
    mydigTool = mydig(resolverIP)
    os.chdir(r'../..')
    dataFile = open("data/random_dns_records.txt", 'r')
    counter = 0
    totalTime = 0
    for line in dataFile:
        startTime = time.time()
        domainName = mydigTool.getHostName(line.strip(), "name", 1)
        actualResoledIpAddr = mydigTool.getHostName(line.strip(), "value", 3)
        queryResult = mydigTool.getSingleNameResolved(domainName, "AAAA")
        if queryResult != None and queryResult.response != None:
            if len(queryResult.response.answer) > 0:
                resolvedIpaddr = queryResult.response.answer[0][0]
                print(resolvedIpaddr)
                # if str(resolvedIpaddr).__contains__(actualResoledIpAddr):
                endTime = time.time()
                totalTime += (endTime - startTime)
                counter += 1
                print(counter)

    print("Total ip addresses resolved correctly = ", counter)
    print("Total time taken to reolve ip addresses = ", totalTime)
    print("Total Average Time Taken = ", totalTime/counter)


if __name__ == "__main__":
    main()