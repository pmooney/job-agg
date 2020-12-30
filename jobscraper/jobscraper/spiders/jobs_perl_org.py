import scrapy


class JobsPerlOrgSpider(scrapy.Spider):
    name = 'jobs-perl-org'
    allowed_domains = ['jobs.perl.org']
    start_urls = ['http://jobs.perl.org/']

    # The XPath given by Safari does not work here. I dunno why.
    # By experimenting the below XPath pulls out the pairs of job links,
    # the first is a link to the full job description, the second is who it is.
    # We only need the link to the full job descriptioin
    def parse(self, response):
        for uri_selector in response.xpath('/html/body/table/tr/td/table/tr/td/a/@href'):
            print(f"    uri = {uri_selector.get()}")
            if 'https://jobs.perl.org/job' in uri_selector.get():
                print(f"yielding to scrap {uri_selector.get}")
                yield response.follow(uri_selector.get(), self.parse_job_page)

    def parse_job_page(self, response):
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
