# Semantic movie search engine

This project is a simple movie search engine built with Flask, Pinecone, and Sentence Transformers. It uses a semantic search model to find movies based on the user's query.

## Features

- Semantic search: The search engine understands the context of the user's query and returns relevant results.
- Movie details: Each search result includes the movie's title, release year, and a brief overview.

## Setup

1. Clone this repository.
2. Install the required Python packages:
   `pip3 install flask pinecone-io sentence-transformers python-dotenv`
3. Copy the .env.example file to .env and fill in your Pinecone API key and TMDB API key.
4. Run the Flask app: `python3 query.py`

## Usage

1. Open your web browser and navigate to <http://localhost:5000>.
2. Enter your movie query in the search field and click "Search".
3. The search results will be displayed on the page.

License
This project is licensed under the terms of the MIT license.
