# job-agg
Scan jobs and aggregate them.

This is a learning project for me more than anything else.

I hopes to see jobs by different agents that are actually the same job by doing loose comparisons. That way if you see 7 adverts for a job you'll know they is _one_ job, not seven!

# Running a spider

My first working spider can be invoked like this to get a file of JSON lines:

* cd jobscraper/jobscraper
* scrapy crawl jobs-perl-org -o jobs.perl.org.jl

To view the json lines in a friendly way do:

* cat jobs.perl.org.jl | jq .

# History

I create a new project in gihub first so I could get the python .gitignore file created for me and did this:

* git clone https://github.com/pmooney/job-agg.git
* cd job-agg
* pipenv --python 3.9
* pipenv install scrapy

