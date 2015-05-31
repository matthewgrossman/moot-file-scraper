import argparse
import os.path
import mootgif

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download .gifs from 4Chan")
    parser.add_argument("-b", "--board", dest="boardname", default="b")
    parser.add_argument("-d", "--dest", dest="dest", default="")
    options = parser.parse_args()

    absolute_path = os.path.join(os.getcwd(), options.dest)

    threads = mootgif.thread_ids(options.boardname)
    for thread in threads:
        tims = mootgif.gif_tims_for_thread(options.boardname, thread)
        for tim in tims:
            mootgif.download_gif(tim, options.boardname, absolute_path)
