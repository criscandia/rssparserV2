# -*- coding: utf-8 -*

import configparser
import io
import os
import re
import smtplib
import sys
import urllib
import time
from datetime import datetime, timedelta   
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from optparse import OptionParser
from email.mime.text import MIMEText
import csv
import feedparser
import pygsheets
import pandas as pd
import time

jobs = []
links = []
dates = []

#Parse the Rss.

def parse(url_feed):
    posts = feedparser.parse(url_feed)
    content = ""
    tags = ['angular', 'node', 'nodejs', 'python', 'django', 'frontend', 'backend', 'back end', 'remote', 'remoto', 'fullstack', 'js', '.net', 'sap', 'azure', 'abap', 'react', 'reactnative', 'graphql', 'typescript', 'javascript', 'golang', 'vue', 'data']
    locations = ['United States', 'Canada', 'Spain', 'UK', 'Europe', 'Latin America', 'Argentina']
    sevendays_ago = datetime.now() - timedelta(days=7)
    current = time.time()
    #I want to get the data from a week ago
    for post in list(filter(lambda post: any(location.lower() in post.summary.lower() for location in locations), posts.entries)):
        if any(tag in post.title.lower() for tag in tags) and datetime.fromtimestamp(time.mktime(post.published_parsed)) > sevendays_ago:
            jobs.append(post.title)
            links.append(post.link)
            dates.append(datetime.now().strftime('%d %b %Y %X'))
            content += f"{post.title}: {post.link}\n"
    return content

#Write the spreadsheet

def sheet():
    gc = pygsheets.authorize(service_file="./gs_credentials.json")
    df = pd.DataFrame()
    df["Date"] = dates
    df["Jobs"] = jobs
    df["Links"] = links
    sheet_name = str(datetime.now().year) + str(datetime.now().month)
    try:
          wks = gc.open("ListadoDeProyectos").worksheet_by_title(sheet_name)
    except Exception as err:
        file = gc.open("ListadoDeProyectos")
        file.add_worksheet(sheet_name)
        wks = file.worksheet_by_title(sheet_name)
    values = df.values.tolist()
    wks.append_table(values, start='A1', end=None, dimension='ROWS', overwrite=None)

if __name__=="__main__":
    feed_option = "url_feed"
    parser = OptionParser()
    parser.add_option("-f", "--feed", dest=feed_option,
                  help="write report to FILE", metavar="FILE")

    (options, args) = parser.parse_args()
    if options.url_feed:
    #url_feed = 'http://python.org.ar/trabajo/rss'
        content = parse(options.url_feed)
        print(jobs)
        sheet()
    else:
        print ("Usage rssparser.py -f URL")