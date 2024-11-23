# Email Classification: ham and spam

Introduction
The aim of this project is to classify emails into two categories: spam and ham. The dataset consists of 5,172 emails, of which 1,500 are spam and 3,672 are ham. The aim is to develop a robust classification model using machine learning techniques, employing efficient text preprocessing methods on our dataset and using the Weka tool and the k-NN algorithm.


Emails_arff_conversion.py. The code was implemented to make the email data suitable for Weka by converting it into the .arff format with a proper structure comprising a header and data.  This ensured the integration of the file into Weka, allowing for smooth training and evaluation of the model.

Preprocessing_code_cleaning.py. The code was designed to preprocess the email text to enhance classification accuracy. It performed tasks such as removing special characters, slashes, and hyphens, removing punctuation, and eliminating stopwords. These preprocessing steps ensured cleaner and more uniform input data, reducing noise and strengthening the classification process.
