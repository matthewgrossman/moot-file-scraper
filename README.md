# mootgif

Now that FB supports gifs, I need to build my reactions folder. I've been casually going through 4chan threads to find good ones, but this isn't fast enough. We will use the 4chan API to download all gifs and then I can choose which ones I want. Mostly an exercise in using their API and parsing the JSON

Yes Jon, I know what giphy is.

Who knows where it'll end; if we're bored, we can use some CV to filter out the NSFW

Uses the [4chan API](https://github.com/4chan/4chan-API)

### Example Usage
```bash
mkdir gifs && python3 scraper.py -b g -d gifs
```
