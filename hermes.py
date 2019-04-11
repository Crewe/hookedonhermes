import getopt
import json
import random
import sys
from urllib import request, parse

# An office joke turned made a reality to add some holiday cheer!
# Sends a Hermes-ism to a channel, or a user with a custom message
# or a Pull Request details.
# Enjoy, @Crewe

DEFAULT_CHANNEL = '#general' # This can be a @user or #channel
WEBHOOK_URL = '' # The Slack webhook URL
ICON_URL = 'hermes.png'
THUMB_URL = ''
ADJECTIVES = ['Sweet', 'Great', 'Holy', 'Cursed']
RHYMES = [
    ['commit','Everest\'s summit'], 
    ['front-end', 'Switzerland'],
    ['back-end', 'Greenland'],
    ['middleware', 'I don\'t know where'],
    ['BAUD', 'Cape Cod'],
    ['IP','The Caribean Sea'],
    ['system call', 'St. Paul'],
    ['dot matrix printer', 'Lloydminster'],
    ['rubber ducky', 'Kentucky'],
    ['NULL', 'Portugal'],
    ['VB', 'Galilee'],
    ['typeface', 'outer space']
]

def main():
    x = random.randrange(0, len(ADJECTIVES))
    y = random.randrange(0, len(RHYMES))
    phrase = "{adj} {something} of {someplace}!".format(
        adj=ADJECTIVES[x],
        something=RHYMES[y][0],
        someplace=RHYMES[y][1])

    payload = {'text': phrase,
           'username': 'Hermes Conrad',
           'channel': DEFAULT_CHANNEL}
 
    # Setup a custom emoji in Slack or use a URL to an image.
    # You may only use one or the other.
    # payload['icon_emoji'] = ':hermes:'
    # payload['icon_url'] = ICON_URL

    try:
        opts, args = getopt.getopt(sys.argv[1:],
        "hc:u:t:p:s:",
        ["help","channel=","text=","pull-request=", "subject="])
    except getopt.GetoptError:
        print ('usage: hermes.py [-c <channel>] [-u <user>] [-t=<additional text>] [-p=<pull request URL> [-s=<subject>]]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('usage: hermes.py [-c <channel>] [-u <user>] [-t=<additional text>] [-p=<pull request URL> [-s=<subject>]]')
            sys.exit()
        elif opt in ("-c", "--channel"):
            payload['channel'] = "#" + arg
        elif opt in ("-u", "--user"):
            payload['channel'] = "@" + arg
        elif opt in ("-t", "--text"):
            payload['text'] = "{} {}".format(phrase, arg)
        elif opt in("-p", "--pull-request"):
            payload['attachments'] = [
                {'color': '#7FF7EC',
                'pretext': 'There\'s a new PR in the books mon.',
                'title': 'Pull Request',
                'footer': 'PR Express',
                'footer_icon': THUMB_URL,
                'text': arg}]
            for opt2, arg2 in opts:
                if opt2 in ("-s", "--subject"):
                    payload['attachments'][0]['title'] = arg2

    bin_data = json.dumps(payload,  separators=(',',':')).encode('ascii')
    req = request.Request(WEBHOOK_URL, method='POST', data=bin_data)
    req.add_header('Content-Type', 'application/json')
    resp = request.urlopen(req)


if __name__ == "__main__":
    main()
