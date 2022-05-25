# Twitter Spell Checking Project

## Crawl Twitter Data

In order to crawl the raw data, we should run the `script.sh` file in the root of our project with `crawl` argument:

```bash
sh script.sh crawl
```

It crawls the recent tweets searching for the recent tweets about `subjects` array defined in `src/crawler.py`. You can change the `repeat_count` variable in `main` function to change the number of iterations.
