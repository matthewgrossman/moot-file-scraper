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

@rate_limit(1.0)
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

@rate_limit(1.0)
def download_gif(gif_url, save_path):
    out_path = save_path + '/' + gif_url.split('/')[-1]
    with urllib.request.urlopen(gif_url) as response, open(out_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)

download_gif("http://i.4cdn.org/b/1433004501165.gif", absolute_path)

    
# def gif_urls_for_threads(thread_ids):
#     for thread in thread_ids:

