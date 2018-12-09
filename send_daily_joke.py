import os
from onesignal import OneSignal, SegmentNotification, Notification

with open('joke.txt', 'r') as f:
  joke = f.readline()

client = OneSignal(os.environ['ONESIGNAL_APP_ID'], os.environ['ONESIGNAL_API_KEY'])
notification_to_all_users = SegmentNotification(
  headings={
    "en": "Физтех-шутка"
  },
  contents={
    "en": joke
  },
  included_segments=SegmentNotification.ALL,
  url="https://vk.com/radiomipt/",
  delayed_option="timezone",
  send_after="18:06:00",
)

client.send(notification_to_all_users)
