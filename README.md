# Email Classification: ham and spam

Introduction
This project aims to classify emails into two categories: spam and ham. The dataset comprises 5172 emails, with 1500 spam and 3672 ham examples. The objective is to develop a robust classification model using machine learning techniques, leveraging tools like Weka and employing effective text preprocessing methods.


Emails_arff_conversion.py. The code was implemented to make the email data suitable for Weka by converting it into the .arff format with a proper structure comprising a header and data.  This ensured the integration of the file into Weka, allowing for smooth training and evaluation of the model.

Preprocessing_code_cleaning.py. The code was designed to preprocess the email text to enhance classification accuracy. It performed tasks such as removing special characters, slashes, and hyphens, removing punctuation, and eliminating stopwords. These preprocessing steps ensured cleaner and more uniform input data, reducing noise and strengthening the classification process.
