# -------------------------------------------------------------------------
# AUTHOR: Aaliyah Divinagracia
# FILENAME: cleaned_documents.csv
# SPECIFICATION: find and output the two most similar
# documents from the cleaned_documents.csv dataset based on their cosine similarity
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 3hrs
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
        documents.append(row[1])
        print(row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
#--> add your Python code here
unique_words = set()
for doc in documents:
    words = doc.split()
    unique_words.update(words)

unique_words = sorted(list(unique_words))
word_index = {word: i for i, word in enumerate(unique_words)}

docTermMatrix = []
for doc in documents:
    words = doc.split()
    vector = [1 if unique_words[i] in words else 0 for i in range(len(unique_words))]
    docTermMatrix.append(vector)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here
max_similarity = -1
most_similar_docs = (-1, -1)

for i in range(len(docTermMatrix)):
    for j in range(i + 1, len(docTermMatrix)):  # Compare each pair only once
        similarity = cosine_similarity([docTermMatrix[i]], [docTermMatrix[j]])[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_docs = (i + 1, j + 1)  # Adjust index to match document IDs


# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here
print(f"The most similar documents are document {most_similar_docs[0]} and document {most_similar_docs[1]} with cosine similarity = {max_similarity:.4f}")
