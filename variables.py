import os
#model parameters
vocab_size = 10000
embedding_dim = 300
cutoff = 0.2
batch_size = 32
epochs = 50
d1 = 10
d2 = 1
dense_context = 100
seed = 1234
hidden_dim_encoder = 512
hidden_dim_decoder = 512
num_samples = 20000
padding_type = 'post'
truncating_type = 'post'

# data paths and model paths
data_dir = 'E:\My projects 2\DeepNLP chatbot\cornell movie-dialogs corpus'
movie_conversations_path = os.path.join(data_dir,"movie_conversations.txt")
movie_lines_path = os.path.join(data_dir,"movie_lines.txt")

chatbot_path = os.path.join(data_dir,"chatbot.json")
chatbot_weights = os.path.join(data_dir,"chatbot.h5")