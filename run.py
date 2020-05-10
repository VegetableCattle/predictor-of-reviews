from flask import Flask, redirect, url_for, request, render_template
import re
import numpy as np

app = Flask(__name__)
rating_num = [19158, 40146, 406379, 531411, 1534845]
word_num = [351866, 812238, 7844287, 10053347, 29664372]
stopSet = set({'i', 'im', 'me', 'my', 'myself', 'we', 'our', 'ours', 'us', 'ourselves', 'you', 'your', 'yours',
               'yourself', "youve", 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
               'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
               'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
               'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
               'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
               'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',
               'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out',
               'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
               'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some',
               'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
               'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain',
               'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn',
               'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn',
               "havent", "wont", 'mustnt', "neednt", 'couldnt', 'doesnt', "shouldnt", "wasnt", 'wouldnt', "shes",
               "shouldve", "werent", "isnt", "dont", "arent", "thatll", "hasnt", "didnt", "mightnt", "hadnt", 'youre',
               'theyre', })


def read_file():
    f = open('./static/dict_file.txt', 'r')
    a = f.read()
    train = eval(a)
    f.close()
    return train


train_dict = read_file()


@app.route('/predicted', methods=['POST', 'GET'])
def predicted():
    if request.method == 'POST':
        sentence = request.form['sentence']

    else:
        sentence = request.args.get('sentence')
    rating = ' '
    probability = ''
    if sentence:
        rating, probability = rating_prediction(sentence)
    else:
        sentence = ''

    print(sentence)
    return render_template('flask.html', rating=rating, sentence=sentence, probability=probability)


def rating_prediction(sentence):
    rating, probability = predict(sentence)
    pro = ''
    for i in range(0,len(probability)):
        pro += str(i + 1) + "pts: " + str(round(probability[i] / probability[rating], 4))
        if i != len(probability) - 1:
            pro += ','
    rating += 1
    return rating, pro


def getConditionalProbabilityUsingSmoothing(word):
    lambda_value = 0.0005
    conditional_probability = list()
    for i in range(0, len(rating_num)):
        if word not in train_dict:
            pro = lambda_value / (len(train_dict) * lambda_value + word_num[i])
        else:
            pro = (lambda_value + train_dict[word][i]) / (len(train_dict) * lambda_value + word_num[i])
        conditional_probability.append(pro)
    return conditional_probability


def SegmentLineToWordsSet(sentense):
    sentense = re.sub("[%s]+" % ('"|#|$|%|&|\|(|)|\[|\]|*|+|\-|/|<|=|>|@|^|`|{|}|~|,|.|?|!|:|;'), ' ', sentense)
    sentense = re.sub("[%s]+" % ('\''), '', sentense)
    return set([x.lower() for x in re.split(r'[\s]\s*', sentense.strip()) if x])


def predict(review):
    words = set()
    words = words.union(SegmentLineToWordsSet(review))
    probability = np.array(rating_num).astype(float)
    pattern = re.compile('[0-9]+')
    for word in words:
        if pattern.findall(word):
            continue
        if word not in stopSet and len(word) > 1:
            probability *= getConditionalProbabilityUsingSmoothing(word)
    probability = list(probability)
    return probability.index(max(probability)), probability


if __name__ == '__main__':
    app.run()
