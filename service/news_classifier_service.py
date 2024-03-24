import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
import nltk
import re
from nltk.corpus import stopwords

class NewsClassifierService:
    def __init__(self):
        nltk.download('stopwords')
        self.model = load_model('fake_news_classifier_model_75percent_acc.h5')
        self.voc_size = 5000

    def preprocess_content(self, content):
        processed_content = []
        for text in content:
            text = re.sub('[^a-zA-Z]', ' ', text)
            text = text.lower()
            text = text.split()
            text = [word for word in text if not word in stopwords.words('english')]
            text = ' '.join(text)
            processed_content.append(text)
        return processed_content

    def classify_news(self, df):
        # df = pd.read_csv(file_path)
        content = df['text'].values
        processed_content = self.preprocess_content(content)
        onehot_repr = [one_hot(words, self.voc_size) for words in processed_content]
        embedded_docs = pad_sequences(onehot_repr, padding='pre', maxlen=20)
        predictions = self.model.predict(embedded_docs)
        predicted_classes = ['Fake' if prediction > 0.5 else 'Real' for prediction in predictions]
        return predicted_classes