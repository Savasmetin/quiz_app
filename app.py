from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Oturum verilerini güvenli hale getirmek için rastgele bir anahtar kullanın

questions = [
    (1, 'Bir bilgisayar bir resmi tanıyabilir mi?', 'Evet', 'Evet', 'Hayır', 'Belki', 'Bilmiyorum', 10),
    (2, 'Yapay zeka robotlar nasıl konuşmayı öğrenir?', 'Veri ile', 'Oyun oynayarak', 'Kitap okuyarak', 'Veri ile', 'Uçarak', 10),
    (3, 'Bilgisayarlar neyi görür?', 'Piksel', 'Müzik', 'Koku', 'Tat', 'Piksel', 10),
    (4, 'Chatbot nedir?', 'Konuşan bilgisayar programı', 'Kedi türü', 'Uzay aracı', 'Konuşan bilgisayar programı', 'Çiçek türü', 10),
    (5, 'Bir yapay zeka nasıl şarkı söylemeyi öğrenir?', 'Veri ile', 'Rüyada', 'Arkadaşlarıyla', 'Veri ile', 'Dans ederek', 10),
    (6, 'NLP ne anlama gelir?', 'Doğal Dil İşleme', 'Yeni Dil Öğrenme', 'Notalı Lamba Projesi', 'Doğal Dil İşleme', 'Neşeli Limon Partisi', 10),
    (7, 'Gözlük takan bir robot hangi alanı kullanır?', 'Bilgisayar Görüşü', 'NLP', 'Matematik', 'Fizik', 'Bilgisayar Görüşü', 10),
    (8, 'Bir bilgisayar konuşmaları nasıl anlayabilir?', 'NLP', 'Bilgisayar Görüşü', 'Kimya', 'Astronomi', 'NLP', 10),
    (9, 'Bir yapay zeka nasıl çizim yapabilir?', 'Veri ve Algoritmalar ile', 'Sihirli Kalem', 'Bilgisayar Görüşü', 'NLP', 'Veri ve Algoritmalar ile', 10),
    (10, 'Bir yapay zeka hangi duyuları kullanabilir?', 'Görme ve Dinleme', 'Tat ve Koku', 'Tat ve Görme', 'Görme ve Dinleme', 'Koşma ve Zıplama', 10)
]

@app.route('/', methods=['GET', 'POST'])
def index():
    score = 0
    if request.method == 'POST':
        for question in questions:
            q_id = str(question[0])
            if request.form.get(q_id) == question[2]:
                score += question[7]
        
        if 'high_score' not in session or score > session['high_score']:
            session['high_score'] = score
    
    high_score = session.get('high_score', 0)
    return render_template('quiz.html', questions=questions, score=score, high_score=high_score)

if __name__ == '__main__':
    app.run(debug=True)
