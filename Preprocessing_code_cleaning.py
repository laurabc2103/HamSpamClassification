import os
import pandas as pd
import re  
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
english_stopwords = set(stopwords.words('english'))

base_folder = '/users/1217746/Downloads/LIMPIEZA'
ham_folder = os.path.join(base_folder, 'ham')
spam_folder = os.path.join(base_folder, 'spam')

data = []

def process_folder(folder_path, label):
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    body = ' '.join(line.strip() for line in file.readlines())
                    print(f"Processing {file_name}: {body[:100]}...") 
                    data.append((body, label))
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as file:
                    body = ' '.join(line.strip() for line in file.readlines())
                    print(f"Processing {file_name} (latin-1): {body[:100]}...")
                    data.append((body, label))

process_folder(ham_folder, 'ham')
process_folder(spam_folder, 'spam')

df = pd.DataFrame(data, columns=['body', 'label'])

print("Sample of DataFrame content:")
print(df.head())


df['body'] = df['body'].str.replace('\n', ' ', regex=True) 
df['body'] = df['body'].str.replace('"', "'", regex=True)  
df['body'] = df['body'].str.strip()  

df['body'] = df['body'].str.replace(r'[\/@-]', ' ', regex=True)  

df['body'] = df['body'].apply(
    lambda x: ' '.join(word.lower() for word in re.findall(r'\b\w+\b', x) if word.lower() not in english_stopwords)
)

print(df['body'].head())

with open('emails.arff', 'w', encoding='utf-8') as f:
    f.write('@RELATION email_classification\n\n')
    f.write('@ATTRIBUTE body STRING\n')
    f.write('@ATTRIBUTE class {\"spam\", \"ham\"}\n\n')
    f.write('@DATA\n')
    
    for index, row in df.iterrows():
        f.write(f'"{row.body}", "{row.label}"\n')

print("Conversion to ARFF completed.")
