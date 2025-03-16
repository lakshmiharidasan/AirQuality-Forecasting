import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset
AIR_QUALITY_RESPONSES = [
    {"user": "how do agricultural practices affect air quality?",
     "bot": "Agricultural practices release pollutants like methane from livestock, ammonia from fertilizers, and dust from crops, all of which contribute to air pollution."},
    {"user": "how do volatile organic compounds (VOCs) impact air quality?",
     "bot": "VOCs are chemicals emitted by vehicles, industrial processes, and household products that contribute to the formation of ground-level ozone and smog."},
    {"user": "how does air pollution affect the productivity of plants?",
     "bot": "Air pollution can damage plant leaves, stunt growth, and reduce agricultural yields by blocking sunlight, causing damage to plant tissues, and impairing photosynthesis."},
    {"user": "how can air quality be improved through urban planning?",
     "bot": "Urban planning can improve air quality by integrating green spaces, creating pedestrian-friendly areas, promoting public transportation, and encouraging sustainable building practices."},
    {"user": "how do air pollution and human health intersect?",
     "bot": "Air pollution directly impacts human health by causing respiratory and cardiovascular diseases, increasing cancer risk, and contributing to premature deaths."},
    {"user": "how can a decrease in air pollution improve urban living?",
     "bot": "A decrease in air pollution can lead to better health outcomes, cleaner environments, reduced healthcare costs, and a higher quality of life for urban residents."},
    {"user": "how do landfills contribute to air pollution?",
     "bot": "Landfills release methane and other gases into the atmosphere, contributing to air pollution and global warming."},
    {"user": "what are the effects of air pollution on children's health?",
     "bot": "Children are particularly vulnerable to air pollution, as it can impair lung development, increase the risk of asthma, and cause cognitive and behavioral issues."},
    {"user": "how can individuals reduce their exposure to air pollution?",
     "bot": "Individuals can reduce exposure to air pollution by staying indoors on high pollution days, using air purifiers, avoiding heavy traffic areas, and wearing masks when necessary."},
]

# Extract the user queries and bot responses
user_queries = [entry["user"] for entry in AIR_QUALITY_RESPONSES]
bot_responses = [entry["bot"] for entry in AIR_QUALITY_RESPONSES]

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on both user queries and bot responses
corpus = user_queries + bot_responses
vectorizer.fit(corpus)


# Function to get the best response
def get_best_response(user_input):
    # Convert the user's input to the same vector space
    user_vector = vectorizer.transform([user_input])

    # Get the cosine similarity between the user input and all bot responses
    similarity_scores = cosine_similarity(user_vector, vectorizer.transform(bot_responses))

    # Get the index of the most similar response
    best_match_index = np.argmax(similarity_scores)

    # Return the best matching bot response
    return bot_responses[best_match_index]



