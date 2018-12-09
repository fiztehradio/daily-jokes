import os
from onesignal import OneSignal, SegmentNotification

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
  delivery_time_of_day="6:10PM"
)

client.send(notification_to_all_users)
