# plotbot
This is the code that powers https://twitter.com/WikiPlotBot, a Twitter bot that describes movies using only the links in their Wikipedia plot summaries.

To use this code:
- Get a Google App Engine envronment up and running
- Install the requirements from requirements.txt into the lib directory (`$ pip install -r requirements.txt -t lib`)
- Add your Twitter credentials to `twitter_keys.py` (you can use `twitter_keys_example.py` as a template)

To tweet a random movie, navigate to `/admin/tweet`

To tweet a specific movie, navigate to `/admin/tweet?page=wikipedia_slug`, where `wikipedia_slug` is something like `A_Star_Is_Born_(2018_film)`
