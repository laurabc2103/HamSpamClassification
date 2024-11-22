import os
import pandas as pd
import re  # Import regular expression module

# Define the base path for ham and spam folders
base_folder = 'C:/Users/Usuario/OneDrive/Escritorio/UNIVERSIDAD PAIS VASCO/2_INTR_MACHINE_LEARNING/ASSIGNMENT/arff_emails_alltogeteher'
ham_folder = os.path.join(base_folder, 'ham')
spam_folder = os.path.join(base_folder, 'spam')

# Initialize a list to hold email data
data = []

# Function to process emails in a folder
def process_folder(folder_path, label):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Assume the whole file is the body, with no subject line
                    body = ' '.join(line.strip() for line in file.readlines())
                    # Debug print to verify email content
                    print(f"Processing {file_name}: {body[:100]}...")  # Print the first 100 characters of each email
                    data.append((body, label))
            except UnicodeDecodeError:
                # Fallback to a different encoding if UTF-8 fails
                with open(file_path, 'r', encoding='latin-1') as file:
                    body = ' '.join(line.strip() for line in file.readlines())
                    # Debug print to verify email content
                    print(f"Processing {file_name} (latin-1): {body[:100]}...")
                    data.append((body, label))

# Process both folders
process_folder(ham_folder, 'ham')
process_folder(spam_folder, 'spam')

# Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=['body', 'label'])

# Debug print to verify DataFrame content
print("Sample of DataFrame content:")
print(df.head())

# Clean up the body column:
# 1. Remove line breaks and extra whitespace
# 2. Remove all special characters (e.g., !, ?, @, #)
df['body'] = df['body'].str.replace('\n', ' ', regex=True)  # Remove line breaks
df['body'] = df['body'].str.replace('"', "'", regex=True)  # Replace double quotes with single quotes
df['body'] = df['body'].str.strip()  # Remove leading and trailing spaces

# Remove special characters using regular expressions
df['body'] = df['body'].apply(lambda x: re.sub(r'[^\w\s]', '', x))  # Remove all non-alphanumeric characters (except spaces)

# Save to ARFF format
with open('emails.arff', 'w', encoding='utf-8') as f:
    # Write ARFF header
    f.write('@RELATION email_classification\n\n')
    f.write('@ATTRIBUTE body STRING\n')
    f.write('@ATTRIBUTE class {\"spam\", \"ham\"}\n\n')
    f.write('@DATA\n')
    
    # Write data
    for index, row in df.iterrows():
        f.write(f'"{row.body}", "{row.label}"\n')

print("Conversion to ARFF completed.")
