import os
from twilio.rest import Client
import feedparser
from dotenv import load_dotenv

load_dotenv()

print("Script started...")

# Twilio setup
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
user_phone = os.getenv("USER_PHONE")

# Load feeds from .env
feeds_env = os.getenv("FEEDS", "")
feeds = [f.strip() for f in feeds_env.split(",") if f.strip()]

print(" Loaded environment variables")
print("Feeds:", feeds)

# Fetch headlines
headlines = []
for url in feeds:
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:2]:  
            headlines.append(entry.title)
    except Exception as e:
        print(f" Error parsing {url}: {e}")

if not headlines:
    headlines = ["No news available"]

message_body = "Top News:\n" + "\n".join([f"- {h}" for h in headlines])

# Trim to 3 segments max (~210 Telugu characters)
MAX_SEGMENTS = 2
MAX_CHARS = 70 * MAX_SEGMENTS  # Telugu = ~70 chars per segment

def trim_sms(text):
    if len(text) > MAX_CHARS:
        return text[:MAX_CHARS - 3] + "..."  # add ellipsis if trimmed
    return text

message_body = trim_sms(message_body)

print(" Headlines selected:")
for h in headlines:
    print("   •", h)

# Send SMS
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=message_body,
    from_=twilio_phone,
    to=user_phone
)

print(f"SMS sent! SID: {message.sid}")
