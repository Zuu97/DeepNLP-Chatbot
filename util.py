import numpy as np
import re
from variables import*
from sklearn.utils import shuffle
import string

def load_data():
    id2line = {}
    for line in open(movie_lines_path, encoding='utf-8', errors='ignore'):
        line = line.split('\n')[0]
        line = line.split(' +++$+++ ')
        if len(line) == 5:
            line_id = line[0]
            line_text = line[-1]
            id2line[line_id] = line_text

    conversation_ids = []
    for line in open(movie_conversations_path, encoding='utf-8', errors='ignore'):
        line = line.split('\n')[0]
        line = line.split(' +++$+++ ')
        id_list = eval(line[-1])
        conversation_ids.append(id_list)

    return id2line, conversation_ids

def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "what is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
    return text

def get_Q_A():
    id2line, conversation_ids = load_data()
    questions = []
    answers = []
    for conversation_id in conversation_ids:
        for i in range(len(conversation_id)-1):
            question = clean_text(id2line[conversation_id[i]])
            answer = clean_text(id2line[conversation_id[i+1]])
            questions.append(question)
            answers.append(answer)
    return questions, answers

def get_data():
    questions, answers = get_Q_A()
    questions, answers = shuffle(questions, answers)
    questions, answers = np.array(questions), np.array(answers)
    ids = np.array([i for i in range(len(questions)) if (len(questions[i].split()) <= 8) and (len(answers[i].split()) <= 8)])
    idxs = np.random.choice(ids, num_samples, replace=False)
    questions, answers = questions[idxs], answers[idxs]

    inputs = []
    target_inputs = []
    targets = []

    for i in range(len(answers)):
        input_seq = questions[i]
        output_seq = answers[i]
        target_input_seq = '<sos> ' + output_seq
        target_seq = output_seq + ' <eos>'

        inputs.append(input_seq)
        target_inputs.append(target_input_seq)
        targets.append(target_seq)

    return inputs, target_inputs, targets