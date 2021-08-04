#!/usr/bin/env python

import datetime
import sys
import json
import requests

# see README for directions on how to fill these variables
LEADERBOARD_ID = "YOUR_ID_HERE"
SESSION_ID = "YOUR_SESSION_COOKIE_HERE"
SLACK_WEBHOOK = "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_HERE"

# You should not need to change this URL
LEADERBOARD_URL = "https://adventofcode.com/{}/leaderboard/private/view/{}".format(
        datetime.datetime.today().year, LEADERBOARD_ID)

def formatLeaderMessage(members):
    """
    Format the message to conform to Slack's API
    """
    message = "Below are the current Top 15 of our leaderboard (orderd by stars). Give a :thumbsup: when you've completed today's challenge! Remember, you all have until *Monday 4th January* to get as many stars as possible and top of leaderboard wins a prize :gift: (or if a tie, I'll select at random). Well done to all of you with " + str(members[0][2]) + " :star:s so far!\n\n"

    # add each member to message
    for username, score, stars, last_star_ts in members:
        message += "*{}* {} :star:\n".format(username, stars)

    message += "\n<{}|View Online Leaderboard>".format(LEADERBOARD_URL)

    return message

def parseMembers(members_json):
    """
    Handle member lists from AoC leaderboard
    """
    # get member name, score and stars
    members = [(m["name"], m["local_score"], m["stars"], m["last_star_ts"]) for m in members_json.values()]

    # sort members by score, decending
    members.sort(key=lambda s: (-s[2], -(-1*int(s[3]))))

    return members[:15]

def postMessage(message):
    """
    Post the message to to Slack's API in the proper channel
    """
    payload = json.dumps({
       # "icon_emoji": ":christmas_tree:",
       # "username": "Advent Of Code Leaderboard",
        "text": message
    })

    requests.post(
        SLACK_WEBHOOK,
        data=payload,
        headers={"Content-Type": "application/json"}
    )

def main():
    """
    Main program loop
    """
    # make sure all variables are filled
    if LEADERBOARD_ID == "YOUR_ID_HERE" or SESSION_ID == "YOUR_SESSION_COOKIE_HERE" or SLACK_WEBHOOK == "https://hooks.slack.com/services/YOUR_SLACK_WEBHOOK_HERE":
        print("Please update script variables before running script.\n\
                See README for details.")
        sys.exit(1)

    # retrieve leaderboard
    r = requests.get(
        "{}.json".format(LEADERBOARD_URL),
        cookies={"session": SESSION_ID}
    )
    if r.status_code != requests.codes.ok: #pylint: disable=no-member
        print("Error retrieving leaderboard")
        sys.exit(1)

    # get members from json
    members = parseMembers(r.json()["members"])

    # generate message to send to slack
    message = formatLeaderMessage(members)

    # send message to slack
    postMessage(message)

if __name__ == "__main__":
    main()
