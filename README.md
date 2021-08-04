# Advent of Code Leaderboard Slack Bot

This is a small adaptation of the wonderful work done by tomswartz07, see the original repo and their code [here](https://github.com/tomswartz07/AdventOfCodeLeaderboard).

## Slightly Updated Original README

This repository contains the code for a script that will post a Private Advent of Code Leaderboard to a custom Slack Channel.

Useful for your friendly competitions in and around the workplace.

**What It Does:** Post the contents of a Private Advent of Code Leaderboard to your Slack Channel

## Setup
**Prerequisites**:
- Python 3
- Working Internet Connection
- Admin access to a Slack Workspace or the ability to persuade someone who does (I hear Christmas Cookies are nice this time of year).

**Process**:

1. Create a new [Incoming Slack Webhook](https://my.slack.com/services/new/incoming-webhook/)
    - Read more about incoming webhooks [here](https://api.slack.com/incoming-webhooks)
    - Feel free to customize it as you wish.
    - If you don't have access to add an incoming webhook, see the [Recommended Settings](#recommended-settings) section for more details.
2. Log in to Advent of Code and obtain two things: the Private Leaderboard ID Number and a Session Cookie.
See [Session Cookie](#getting-a-session-cookie) section for details.
3. Dump that info into the copy of the script.
  - Webhook URL goes in the `SLACK_WEBHOOK` variable
  - Session goes in the `SESSION_ID` variable
  - Leaderboard ID goes in the `LEADERBOARD_ID` variable.
    - The ID is the last part of the leaderboard url (https://adventofcode.com/2018/leaderboard/private/view/LEADERBOARD_ID)
4. Run that shit. Schedule a cron job or something. I don't know. You're doing Advent of Code, figure it out. [Just make sure that you don't hit the servers too often.](https://www.reddit.com/r/adventofcode/comments/7gy2y3/remember_please_limit_automated_http_requests/)

## Recommended Settings
When creating the custom webhook for the Slack channel, there are a few options to customise.

It's also possible that you don't have access to add an incoming webhook to your team due to permissions. In that case, you would need to know what to send to the admin to get it set up.

Here are the recommended settings when setting up the Hook:
- **Post to Channel:** Your `#advent_of_code` channel, or whatever name
- **Descriptive Label:** Whatever you want. This isn't really necessary.
- **Customize Name:** "Advent of Code Leaderboard"
- **Customize Icon:** Pick an emoji, the [Advent of Code logo](./advent_of_code.png) in this repo or a Christmas Tree perhaps.

Copy the Webhook URL or have the Admin send that URL to you, you'll need to include it at the top of the script.

## Getting a Session Cookie
You'll need a session cookie from the Advent of Code website.

Go to the [Advent of Code Private Leaderboard](https://adventofcode.com/2018/leaderboard/private) page. Make sure you're logged in.

### In Chrome:
- Open the Developer Tools by pressing `CTRL` + `Shift` + `I`
    - Mac: Open the Developer Tools by pressing `Cmd` + `Opt` + `I`
- Select "Application" from the tool tabs
- Click the dropdown arrow beside cookies in treeview on the left
- Select *https://adventofcode.com*
- Double click the value of the *session* cookie to highlight it
- Right click and copy the value
- Add this value to the top of the script as the `SESSION_COOKIE =` constant as a string.

### In Firefox:
- Open the Developer Tools by pressing `F12`
- Click on the small gear on the top right of the Developer Options pane
- Scroll down and make sure that "Storage" is checked under the Default Firefox Developer Options section
- Click on the Storage tab
- Open the Cookies section and copy the "Value" for "session"
- Add this value to the top of the script as the `SESSION_COOKIE =` constant as a string.
