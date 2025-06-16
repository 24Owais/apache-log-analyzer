import re
from collections import Counter

# Open the Apache log file
with open("access.log", "r") as log:
    logs = log.readlines()

# Regex pattern to match log entries
pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*?\] "(?:GET|POST) (?P<url>\S+).*?" (?P<status>\d{3})'
)

# Data collectors
ips = []
urls = []
statuses = []

# Extract relevant info
for line in logs:
    match = pattern.search(line)
    if match:
        ips.append(match.group("ip"))
        urls.append(match.group("url"))
        statuses.append(match.group("status"))

# Print analysis
print("\n🔸 Top 5 Most Common IPs:")
for ip, count in Counter(ips).most_common(5):
    print(f"{ip} — {count} requests")

print("\n🔸 Top 5 Requested URLs:")
for url, count in Counter(urls).most_common(5):
    print(f"{url} — {count} hits")

print("\n🔸 HTTP Status Codes:")
for status, count in Counter(statuses).items():
    print(f"{status} — {count} times")
