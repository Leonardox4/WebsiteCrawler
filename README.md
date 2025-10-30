
The working principle is fairly simple, the code first downloads the html file of the site and then looks for 'anchor tags' and takes out the 'href'. Those href contains links which are then scrapped and
then checked recursively again and again.

use case:
python3 Static_Spider.py
#Note: This only works with static websites.
