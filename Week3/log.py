import re
from collections import Counter

# Path to mail log
log_file = "/var/log/mail.log"

# Counter Variables
total_logs = 0
sent_count = 0
bounced_count = 0
deferred_count = 0
ip_counter = Counter()
from_counter = Counter()
to_counter = Counter()

# Patterns to match in Logs
from_pattern = r'from=<([^>]*)>'
to_pattern = r'to=<([^>]*)>'
# Regex to extract IP inside []
ip_pattern = r'\[(\d+\.\d+\.\d+\.\d+)\]'

try:
    with open(log_file, "r") as file:
        for line in file:
            total_logs += 1

            # Check emails statuses
            if "status=sent" in line:
            
            elif "status=bounced" in line:
                
            elif "status=deferred" in line:
                

            # Extract IP addresses
            ip_match = re.search(ip_pattern, line)
            if ip_match:
                ip = ip_match.group(1)
                ip_counter[ip] += 1
            # Extract sender
            from_match = re.search(from_pattern, line)
            if from_match:
                sender = from_match.group(1)
                from_counter[sender] += 1

            # Extract receiver
            to_match = re.search(to_pattern, line)
            if to_match:
                receiver = to_match.group(1)
                to_counter[receiver] += 1

    # Get most frequent IP
    most_common_ip = ip_counter.most_common(1)

    # Report
    print("----- Mail Log Report -----")
    print(f"Total Logs: {total_logs}")
    print(f"Emails Sent: {sent_count}")
    print(f"Emails Bounced: {bounced_count}")
    print(f"Emails Deferred: {deferred_count}")

    #Now Collecting top sender and receivers using Counter();
    if from_counter:
        top_sender = from_counter.most_common(1)[0]
        print(f"Top Sender: {top_sender[0]} ({top_sender[1]} emails)")

    if to_counter:
        top_receiver = to_counter.most_common(1)[0]
        print(f"Top Receiver: {top_receiver[0]} ({top_receiver[1]} emails)")

    if most_common_ip:
        print(f"Top IP: {most_common_ip[0][0]} ({most_common_ip[0][1]} times)")

except FileNotFoundError:
    print("Log file not found. Check the path!")
except PermissionError:
    print("Permission denied. Try running with sudo.")
