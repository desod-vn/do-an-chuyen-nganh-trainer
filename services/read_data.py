from pyvi import ViTokenizer, ViPosTagger # thư viện NLP tiếng Việt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
import time
import pickle
from tqdm import tqdm
import numpy as np
import gensim # thư viện NLP
# xử dụng stop word loại bỏ từ không có ý nghĩa trong việc phân loại
f = open("assets\Stopword\stopword.txt",encoding = 'utf-8')
stopword=f.read()
def remove_stopwords(line):
    words = []
    for word in line.strip().split():
        if word not in stopword:
            words.append(word)
    return ' '.join(words)
def processing_data(data):
    data = gensim.utils.simple_preprocess(data)
    data = ' '.join(data)
    data = ViTokenizer.tokenize(data)

    data=remove_stopwords(data)
    return data

xxx=[]
str=' Hơn 16.000 khách đến vịnh Nha Trang Theo trực ban bộ đội biên phòng tại cảng du lịch Cầu Đá (Vĩnh Nguyên), trong những ngày lễ vừa qua có hơn 16.000 người đến tham quan vịnh Nha Trang, trong đó có 734 du khách nước ngoài.Đông nhất là vào ngày 30-4, vịnh Nha Trang đã đón tới 7.019 du khách. Những địa chỉ trong vịnh Nha Trang thu hút được số lượng du khách đến tham quan, nghỉ ngơi, vui chơi nhiều nhất vẫn là các đảo Hòn Tằm và Hòn Mun. '

xxx.append(processing_data(str))

tfidf_vect_ngram = pickle.load(open(r'module\tfidf_vect_ngram_fit.pkl', 'rb'))
xxx_tfidf_ngram =  tfidf_vect_ngram.transform(xxx)

svd_ngram = pickle.load(open(r'module\svd_ngram_fit.pkl', 'rb'))

xxx_tfidf_ngram_svd = svd_ngram.transform(xxx_tfidf_ngram)

from sklearn.naive_bayes import BernoulliNB

model = pickle.load(open(r'module\AI.pkl', 'rb'))

score = model.predict_proba(xxx_tfidf_ngram_svd)
score1 = model.predict(xxx_tfidf_ngram_svd)
print(score)
print(score1)


#ok r đợi thôi xong chạy file featureEngineering, file này lâu nhất
# xong chạy file trainModule r chạy read_data là đc
# ok