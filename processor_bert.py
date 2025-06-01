from sentence_transformers import SentenceTransformer
import joblib


#Load the sentence transformer model to compute embeddings
transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

import os

#Load the saved classifier
model_path = os.path.join(os.path.dirname(__file__), 'model', 'log_classifier.joblib')
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")
classifier = joblib.load(model_path)
    
def classify_with_bert(log_message):
    
    #compute the embedding for the log message
    embedding = transformer_model.encode(log_message, convert_to_tensor=True)   
    
    probabilities = classifier.predict_proba([embedding])[0]
    
    
    if probabilities.max() < 0.5:
        return "Unclassified"
    
    #Predict the label using the classifier
    label = classifier.predict([embedding])[0]  
    
    return label

if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "Hey bro, chill ya!",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)
    