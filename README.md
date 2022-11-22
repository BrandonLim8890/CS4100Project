# CS4100Project

## Milestone Report 1

### Current progress

Scraper
- Implemented web scraper to get Amazon product review information from a given search keyword.
  - Implemented in Python with BeautifulSoup4 and requests libraries

NLP Sentiment Analysis Training
- Amazon review data set obtianed from Kaggle
- Understand workflows of how to preprocess text before Sentiment Analysis
- Researched into various NLP techniques used in Sentiment Analysis
  - Bag-of-words
  - TF-IDF
  - Word Embeddings
  - Word2Vec

### Reflection
- Our goal for milestone 1 was to implement a scraper for Amazon reviews and train a sentiment analysis model on that data.
- We succesfully acquired our data, but haven't implement it with a model yet.
- We didn't fully understand the process of using a sentiment analysis model when planning our milestones.
- Functionality (succesfully giving scores to text) was planned for milestone 2. Now it makes more sense that training a model on data comes hand in hand with functionality, so we will aim to do that for milestone 2.

### Next steps
- Having done enough research, we will need to choose a technique of our we will be qualifying our data. We will then need to actually implement the preprocessing, as well as feeding our AI applicaiton the data set from kaggle. 
- Combine the scraper to provide a data set to test our Sentiment Analysis algorithm on
- Create CLI for user to interact with

## Milestone Report 2

### Current progress
Improvements to product review scraper:
- Finalized I/O of scraper: takes in a search keyword (optional args: number of products to scrape, number of reviews to scrape), and returns a dictionary of product names (keys) to lists of reviews for that product (values).
- Randomness: in order to get a more accurate sampling of products, scraper now selects products and reviews at random instead of choosing just the top products.
- The scraper now collects more review text, allowing us to give our model more information and make more accurate predictions.
- Cleaned review text to exclude non-ASCII characters, unrelated words such as "read more". Cleaned output format.
- Slightly improved scraper performance, allowing for customizable number of products/reviews to scrape.
Progress on Sentiment-Analysis algorithm
- We decided on using a Convolutional Neural Net Model.
- The model can be used to give a rating of 1 or 0 to a chunk of text (an amazon review), which can be used to find an average rating score for a product.

### Reflection
- The scraper should now be fully ready to combine with the sentiment analysis algorithm. All we need to do is pass the outputs of the scraper to our model to perform sentiment analysis.
- The scraper is now a better reflection of the mission of our project: instead of comparing the top options recommended by Amazon, we randomly select products to compare (they are still products from the first page of results, so they should all have enough reviews to analyze). This allows us to somewhat avoid using Amazon's recommendation algorithm and give our model less biased inputs.
- We're currently creating a CNN model to perform natural language processing. Given a dataset, creating a table with our features is quite slow. We might consider other existing tools (such as Vader or Roberta) to improve efficiency. 
- Giving each comment a rating of either 1 or 0 is quite limited and requires looking at several comments per item for a more precise score. We are hoping to give individual comments more specific scores as well.


### Next steps
- Implement the web scraper with the sentiment analysis model.
- Integrating other models (such as Bag of words) for a more accurate and efficient solution.
- Create a simple command line interface that allows the user to type in what product to look up.
