# hookedonhermes
A Hermes webhook for Slack

An office joke turned made a reality to add some holiday cheer!
Sends a Hermes-ism to a channel or a user with a custom message
or Pull Request details.

Enjoy.

## Setup
### Basic
Create a custom emoji in slack named `hermes` then uncomment `payload['icon_emoji'] = ':hermes:'`.
Or if you'd prefer to use a hosted image add the URL to the image in `ICON_URL` and uncomment
`payload['icon_url'] = ICON_URL`.

### Extra
If you want to use Pull Request fuction and add a little flare add a thumbnail image
for the PR message to `THUMB_URL`.
