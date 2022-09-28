# Surfs_Up
Jupyter Notebook, VS Code(Flask) and GitHub
## Overview of the Analysis:

My vacation visit to Hawaii last year intrigued me to my new found passion for surfing. My passion led me to start thinking about moving to Hawaii for good. Prior to the move I had to make sure I have a good source of income to support my current life style.  A Surf and Shake shop was the best option to enhance/enjoy my passion and make a living of it as well. So I approached a few investors who would be interested in investing in my shop. W.Avy seemed impressed with the idea to offer the tourist with a Surf and Shake shop but he wanted some analysis to be done on the weather data especially for months of June and December to ensure that weather related risks are eliminated and the business can sustain all year round.

## Analysis Results
I analyzed the weather data provided by W.Avy using the Python, Pandas and SQLAlchemy tools to understand the weather trends for the months of June and December thus covering the summer and winter seasons. It will be a representation of how the business will fare in different seasons.
The temperatures in the month of June were favorable for a beach day with a min of 64 deg and max of 85 deg as it is the begining of the summer season. The hot temperatures ensure that the tourist would definitely flock the venue in good numbers. 

### Temperature Statistics(June)

count	1700.000000
mean	74.944118
std	3.257417
min	64.000000
25%	73.000000
50%	75.000000
75%	77.000000
max	85.000000

December being a winter month is off season and might see a decline in the tourist numbers but the data shows that 75% of the days are @ 74 deg which is kind of favorable for surfing at the beach. There might be a decline but the business can sustain with break even profit margins.

### Temperature Statistics(Dec)
count	1517.000000
mean	71.041529
std	3.745920
min	56.000000
25%	69.000000
50%	71.000000
75%	74.000000
max	83.000000

## Weather Analysis Summary

The investors were impressed when I presented the temperature analysis. As per the current analysis, the June and Dec months look favorable for the business to sustain all year round.
I recommended two more analysis queries for further consideration:
* Plotting a histogram using Pandas Matplotlib tool  to draw a clear picture of the data with June/Dec temperature and dates.
*I would use Flask to present my data in a webpage. It would be very user friendly for the investors to  just click on the URL and get all the data displayed.
