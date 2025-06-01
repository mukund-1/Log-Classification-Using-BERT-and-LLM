import re 
def classify_with_regex(log_message):
    regex_pattern = {
        r"User User\d+ logged (in|out)": "User Action",
        r"Backup (started|ended) at .*" : "System Notifications",
        r"Backup completed successfully": "System Notifications",
        r"System updated to version .*" : "System Notifications",
        r"File .* uploaded successfully by user .*" : "System Notifications",
        r"Disk cleanup completed successfully. ": "System Notifications",
        r"System reboot initiated by user .*": "System Notifications",
        r"Account with ID .* created by .*": "User Action"
    }
    
    for pattern, label in regex_pattern.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    
    return None

if __name__ == "__main__":
    test_messages = [
        "User User123 logged in",
        "Backup started at 2023-10-01 12:00:00",
        "Backup completed successfully",
        "System updated to version 1.2.3",
        "File report.pdf uploaded successfully by user User456",
        "Disk cleanup completed successfully.",
        "System reboot initiated by user User789",
        "Account with ID 101 created by admin"
    ]
    
    for message in test_messages:
        print(f"Message: {message} -> {classify_with_regex(message)}")