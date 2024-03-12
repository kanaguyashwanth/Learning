import os
import datetime
import win32com.client

# Path where you want to save the email files
output_folder = "C:/Users/RC982BE/Downloads/TEST/today_emails/"

# List of store numbers
stores = ['7146', '7262', '1855', '2213', '3847', '4020', '4742', '6377']

# Subject to match
subject_to_match = "ECaaS Server Migration has Completed Successfully"

# Get today's date
today = datetime.date.today()

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

# Ensure that the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Keep track of the number of emails saved
total_emails_saved = 0

# Iterate over emails in the Inbox
for message in inbox.Items:
    # Check if the email subject is not an auto-reply or contains 'EXTERNAL Automatic reply'
    if "Out of Office" not in message.Subject and "Auto Reply" not in message.Subject and 'EXTERNAL Automatic reply' not in message.Subject:
        # Check if the email subject contains any of the store numbers
        for store_number in stores:
            if store_number in message.Subject:
                # Check if the email subject contains the specified subject
                if subject_to_match in message.Subject:
                    # Generate a unique filename using subject and timestamp
                    subject = ''.join(char for char in message.Subject if char.isalnum() or char in (' ', '.', '-'))
                    timestamp = message.SentOn.strftime("%Y%m%d_%H%M%S")
                    filename = f"{subject}_{timestamp}.msg"
                    try:
                        message.SaveAs(os.path.join(output_folder, filename))
                        print(f"Email with subject '{message.Subject}' saved as '{filename}'.")
                        total_emails_saved += 1
                    except Exception as e:
                        print(f"Error occurred while saving email '{message.Subject}': {str(e)}")
                    break  # Stop checking further store numbers if a match is found

print(f"Total emails saved: {total_emails_saved}")