#!/bin/bash

#Activate virtualenv

cd ~/Projects/ParserV2

source env/bin/activate

#Execute script rssparse

python3 rssparser.py -f https://app.vuejobs.com/feed/posts
python3 rssparser.py -f https://landing.jobs/feed?remote=true
python3 rssparser.py -f https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss
python3 rssparser.py -f https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss
python3 rssparser.py -f https://weworkremotely.com/categories/remote-front-end-programming-jobs.rss
python3 rssparser.py -f https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss
python3 rssparser.py -f https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss
python3 rssparser.py -f https://jsjobbs.com/rss
python3 rssparser.py -f https://www.djangoproject.com/rss/community/jobs/
python3 rssparser.py -f https://cryptojobslist.com/jobs.rss?jobLocation=Remote	
python3 rssparser.py -f https://www.golangprojects.com/rss.xml	
python3 rssparser.py -f https://jobspresso.co/feed/?post_type=job_listing	
python3 rssparser.py -f https://www.reddit.com/r/RemoteJobs/.rss	   
python3 rssparser.py -f https://www.reddit.com/r/remotejs/.rss	
python3 rssparser.py -f https://www.reddit.com/r/remotepython/.rss	
python3 rssparser.py -f https://vuejobs.com/feed


