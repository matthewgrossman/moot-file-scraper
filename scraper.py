import os.path
import time
import urllib.request
import json
import argparse

# sleeps for time=limit before calling the function
def rate_limit(limit):
    def wrap(f):
        def wrapped_f(*args):
            time.sleep(limit)
            return f(*args)
        return wrapped_f
    return wrap

# get all thread_ids for a given board
@rate_limit(1.0)
def thread_ids(boardname):
    response = urllib.request.urlopen("http://a.4cdn.org/"+ boardname + "/threads.json")
    data = json.loads(response.read().decode())

    return [thread['no'] for page in data for thread in page['threads']]

# get tims of all gifs in a given thread
@rate_limit(1.0)
def gif_tims_for_thread(boardname, thread_id):
    response = urllib.request.urlopen("http://a.4cdn.org/" + boardname+ "/thread/" + str(thread_id) + ".json")
    data = json.loads(response.read().decode())

    # use post.get(key) because not all posts have a 'ext' attribute
    return [post['tim'] for post in data['posts'] if post.get('ext') == '.gif' ]

# download a gif given its tim and board name at a specified path
@rate_limit(1.0)
def download_gif(gif_tim, boardname, save_path):
    out_path = os.path.join(save_path, boardname + '_' + str(gif_tim) + ".gif")
    gif_url = "http://i.4cdn.org/" + boardname + "/" + str(gif_tim) + ".gif"

    with urllib.request.urlopen(gif_url) as response, open(out_path, 'wb') as out_file:
        out_file.write(response.read())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download .gifs from 4Chan")
    parser.add_argument("-b", "--board", dest="boardname", default="b")
    parser.add_argument("-d", "--dest", dest="dest", default="")
    options = parser.parse_args()

    absolute_path = os.path.join(os.getcwd(), options.dest)

    threads = thread_ids(options.boardname)
    for thread in threads:
        tims = gif_tims_for_thread(options.boardname, thread)
        for tim in tims:
            download_gif(tim, options.boardname, absolute_path)
