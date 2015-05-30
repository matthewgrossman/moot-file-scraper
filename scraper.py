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

# get all thread_ids for a given board
def thread_ids(boardname):
    response = urllib.request.urlopen("http://a.4cdn.org/"+ boardname + "/threads.json")
    data = json.loads(response.read().decode())

    return [thread["no"] for page in data for thread in page["threads"]]

# get tims of all gifs in a given thread
def gif_urls_for_thread(boardname, thread_id):
    response = urllib.request.urlopen("http://a.4cdn.org/" + boardname+ "/thread/" + str(thread_id) + ".json")
    data = json.loads(response.read().decode())

    # use post.get(key) because not all posts have a 'ext' attribute
    return [post['tim'] for post in data['posts'] if post.get('ext') == '.gif' ]

# download a gif given its tim and board name at a specified path
def download_gif(gif_tim, boardname, save_path):
    out_path = save_path + boardname + '_' + str(gif_tim)
    gif_url = "http://i.4cdn.org/" + boardname + "/" + str(gif_tim) + ".gif"

    with urllib.request.urlopen(gif_url) as response, open(out_path, 'wb') as out_file:
        out_file.write(response.read())

print(gif_urls_for_thread('vg', 104844212))
#download_gif(1432997104636, 'vg', options.dest) 
