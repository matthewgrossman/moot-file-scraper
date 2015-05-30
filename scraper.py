import os.path
import time
import urllib.request
import json

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--board", type="string", dest="boardname", default="b")
parser.add_option("-d", "--dest", type="string", dest="dest", default="")
(options, args) = parser.parse_args()

absolute_path = os.path.join(os.getcwd(), options.dest)

# sleeps for time=limit before calling the function
def rate_limit(limit):
    def wrap(f):
        def wrapped_f(*args):
            time.sleep(limit)
            f(*args)
        return wrapped_f
    return wrap

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

# get urls of all gifs in a given thread
def gif_urls_for_thread(boardname, thread_id):
    response = urllib.request.urlopen("http://a.4cdn.org/" + boardname+ "/thread/" + thread_id + ".json")
    data = json.loads(response.read().decode())

    # parse the JSON and add all the gif urls to the array
    gif_urls = []
    print(data['posts'][0]['now'])

    return gif_urls

def download_gif(gif_tim, boardname, save_path):
    out_path = save_path + boardname + '_' + str(gif_tim)
    gif_url = "http://i.4cdn.org/" + boardname + "/" + str(gif_tim) + ".gif"
    print(gif_url)
    with urllib.request.urlopen(gif_url) as response, open(out_path, 'wb') as out_file:
        out_file.write(response.read())

download_gif(1432997104636, 'vg', options.dest) 
