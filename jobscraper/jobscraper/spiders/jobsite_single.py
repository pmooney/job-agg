import scrapy
import json

# To test scraping a job try:
# scrapy shell \
#     --set USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' \
#     https://www.totaljobs.com/job/perl-developer/eligo-recruitment-limited-job91484407
#

class JobsPerlOrgSpider(scrapy.Spider):
    name = 'jobsite-single'
    allowed_domains = ['www.totaljobs.com']
    start_urls = ['https://www.totaljobs.com/job/perl-developer/eligo-recruitment-limited-job91484407?src=search&page=1&position=1&WT.mc_id=A_PT_CrossBrand_Jobsite&searchCriteria=Perl&searchLocation=&source=jobsite']

    # Jobsite will give access denied unless its a recognised user-agent
    # I did try an obey the robots.txt file but I could not make that work either (and they
    # list the bots they want to scrape their site)
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    def parse(self, response):
        hash = { 'url': response.url }

        script = response.xpath('//script[@id="jobPostingSchema"]/text()')
        text   = script.get().strip()
        parsed_json = (json.loads(text))

        for key in parsed_json:
            print("%s: %s" % (key, parsed_json[key]))
            hash[key] = parsed_json[key]

        yield hash
