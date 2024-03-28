from typing import List
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from themoviedb import TMDb, schemas
import dotenv
import os

dotenv.load_dotenv()

tmdb = TMDb(key=os.getenv("TMDB_API_KEY"), language="en-US", region="US")

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")


pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("movies")


movies_list: List[schemas.PartialMovie] = []

for i in range(1, 10):
    for m in tmdb.movies().top_rated(page=i).results:
        movies_list.append(m)

movie_titles = [movie.title for movie in movies_list]


embeddings = model.encode(movie_titles)


index.upsert(
    vectors=[
        {
            "id": str(movie.id),
            "values": embedding,
            "metadata": {
                "title": movie.title,
                "cover": movie.poster_url(),
                "overview": movie.overview,
                "release_year": movie.year,
            },
        }
        for movie, embedding in zip(movies_list, embeddings)
    ],
    namespace="ns1",
)
