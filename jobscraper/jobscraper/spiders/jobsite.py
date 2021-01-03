import scrapy
import json

class JobsPerlOrgSpider(scrapy.Spider):
    name = 'jobsite-co-uk'
    allowed_domains = ['jobsite.co.uk']
    start_urls = ['https://www.jobsite.co.uk/jobs/perl']

    # Jobsite will give access denied unless given a recognised user-agent
    # I did try an obey the robots.txt file but I could not make that work either (and they
    # list the bots they want to scrape their site)
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    def parse(self, response):
        a_elements = response.xpath('//div[@class="job-title"]/a')
        hrefs      = [a_element.attrib['href'] for a_element in a_elements]

        for href in hrefs:
            print(f"href = {href}")
            yield response.follow(href, self.parse_job_page)


    def parse_job_page(self, response):
        hash = { 'url': response.url }

        script = response.xpath('//script[@id="jobPostingSchema"]/text()')
        text   = script.get().strip()
        parsed_json = (json.loads(text))

        for key in parsed_json:
            print("%s: %s" % (key, parsed_json[key]))
            hash[key] = parsed_json[key]

        yield hash
