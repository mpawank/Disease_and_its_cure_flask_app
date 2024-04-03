from flask import Flask, render_template

app = Flask(__name__)

# Sample article data
articles = [
    {
        'title': 'Flu',
        'content': 'Influenza, commonly known as the flu, is a viral infection that attacks your respiratory system — your nose, throat and lungs. Influenza is commonly called the flu, but it\'s not the same as stomach "flu" viruses that cause diarrhea and vomiting. For most people, the flu resolves on its own. But sometimes, influenza and its complications can be deadly. People at higher risk of developing flu complications include:',
        'timestamp': '2024-04-03 10:00:00',
        'image': 'flu.jpg',
        'disease': 'flu'
    },
    {
        'title': 'Common Cold',
        'content': 'The common cold is a viral infection of your nose and throat (upper respiratory tract). It\'s usually harmless, although it might not feel that way. Many types of viruses can cause a common cold. Children younger than 6 are at greatest risk of colds, but healthy adults can also expect to have two or three colds annually. Most people recover from a common cold in about a week or 10 days. Symptoms might last longer in people who smoke.',
        'timestamp': '2024-04-02 09:00:00',
        'image': 'common_cold.jpg',
        'disease': 'common_cold'
    }
]

@app.route('/')
def home():
    return render_template('index.html', articles=articles)

@app.route('/filter/<disease>')
def filter_by_disease(disease):
    filtered_articles = [article for article in articles if article['disease'] == disease]
    return render_template('index.html', articles=filtered_articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
