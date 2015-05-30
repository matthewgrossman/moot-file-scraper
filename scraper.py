import pprint
import urllib.request
import json

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--board", type="string", dest="boardname", default="b")
parser.add_option("-d", "--dest", type="string", dest="dest", default="")
(options, args) = parser.parse_args()

# makes one request
def thread_ids(boardname):
    response = urllib.request.urlopen("http://a.4cdn.org/"+ boardname + "/threads.json")
    data = json.loads(response.read().decode())

    return [thread["no"] for page in data for thread in page["threads"]]
    
    # list comprehensions are pretty, but the code is doing this:
    #thread_ids = []
    #for page in data:
    #    for thread in page["threads"]:
    #        thread_ids.append(thread["no"])
    #return thread_ids

print(thread_ids('pol'))
