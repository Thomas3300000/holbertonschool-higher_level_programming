#!/usr/bin/python3
import requests
import json
import csv


def fetch_and_print_posts():
    """Function to fetch and print posts"""
    request = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status code: {}".format(request.status_code))
    
    if request.status_code == 200:
        posts = request.json()
        for post in posts:
            print(post['title'])
def fetch_and_save_posts():
    """Function to fetch and save posts"""
    request = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if request.status_code == 200:
        posts = request.json()
        with open('posts.csv', 'w') as csv_file:
            data = ["id", "title", "body"]
            writer = csv.DictWriter(csv_file, fieldnames=data)
            writer.writeheader()
            for post in posts:
                writer.writerow({"id": post["id"], 
                                "title": post["title"], "body": post["body"]})

