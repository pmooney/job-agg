import scrapy


class JobsPerlOrgSpider(scrapy.Spider):
    name = 'jobs-perl-org-single'
    allowed_domains = ['jobs.perl.org']
    start_urls = ['https://jobs.perl.org/job/21750']

    def parse(self, response):
        hash = {}

        for tr in response.xpath('/html/body/table[2]/tr'):
            td1 = tr.xpath('td[1]/text()')
            td2 = tr.xpath('td[2]/text()')
            # the parsing library seems to split the td into two as it has a <a/> inside it :/
            key = td1[1].get().strip()
            # the value part is just test in the <td> so it's cool
            value = ''.join(td2.getall()).strip()
            #print(f"td1 = {td1}")
            #print(f"td2 = {td2}")
            #print()
            hash[key] = value

        yield hash
