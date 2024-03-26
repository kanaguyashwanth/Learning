import os
import datetime
import win32com.client

# Base directory where you want to save the email files
base_output_folder = "C:/SANITY_CHECKS"

# Create a folder named 'Emails' with the current date
current_date = datetime.date.today().strftime("%Y-%m-%d")
emails_folder_name = f"{current_date}-emails"
output_folder = os.path.join(base_output_folder, emails_folder_name)

# Connect to Outlook
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

# Ensure that the APPS_FINAL folder exists
os.makedirs(output_folder, exist_ok=True)

# Prompt the user to enter stores
stores_input = input("Enter Stores: ").split()  # Get store numbers as space-separated input

# Extract only the numeric parts from the input stores
stores = [store.strip("ST") for store in stores_input]

# Subject to match
subject_to_match = "ECaaS Server Migration has Completed Successfully"

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
