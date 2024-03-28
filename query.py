from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from themoviedb import TMDb
from flask import Flask, request, jsonify, render_template
import os
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")


pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("movies")


@app.route("/search")
def search():
    user_query = request.args.get("q")

    if not user_query:
        return jsonify(error="Query parameter 'q' is required"), 400

    query = [user_query]

    embeddings = model.encode(
        query,
    )

    model_encode_list = [float(x) for x in embeddings[0]]

    results = index.query(
        namespace="ns1",
        vector=model_encode_list,
        top_k=5,
        include_values=False,
        include_metadata=True,
    )

    if results["matches"] is None:
        return jsonify(results=[])

    return jsonify(results=results.to_dict())


@app.route("/")
def home():
    return render_template("search.html")


if __name__ == "__main__":
    app.run(debug=True)
