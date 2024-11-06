import Scraper
import pickle

# Prompt the user for the URL of the documentation to scrape
base_url = input("Enter the URL of the documentation to scrape: ")

# Scrape the website and get all document objects
scraped_documents = Scraper.scrape_website(base_url)

# Print the first few scraped documents for a preview
for i, doc in enumerate(scraped_documents[:2], 1):  # Show the first 2 documents
    print(f"\nDocument {i}")
    print(f"URL: {doc.metadata.get('url', 'No URL found')}")
    print(f"Content Snippet: {doc.text[:200]}...\n")  # Show first 200 characters as snippet

# Build the index from the documents
index = Scraper.build_index_from_documents(scraped_documents)

# Save the index to a file for later use
with open("documentation_index.pkl", "wb") as file:
    pickle.dump(index, file)

print("\nIndexing complete. The index has been saved to 'documentation_index.pkl'.")
