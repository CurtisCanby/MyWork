import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Sample data: questions and answers
questions = ["Hello", "How are you?", "What is your name?", "Goodbye"]
answers = ["Hi there!", "I'm fine, thank you!", "I'm a chatbot.", "Goodbye!"]

# Convert questions and answers to numerical data
def encode_data(data, vocab_size=100):
    encoded_data = []
    for sentence in data:
        encoded_sentence = [ord(char) for char in sentence]
        encoded_data.append(encoded_sentence)
    return tf.keras.preprocessing.sequence.pad_sequences(encoded_data, maxlen=vocab_size)

encoded_questions = encode_data(questions)

# Create integer labels for answers
answer_labels = [0, 1, 2, 3]  # Assign an integer to each answer

# Build the model
model = Sequential([
    Dense(128, input_shape=(100,), activation='relu'),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dense(4, activation='softmax')  # Output layer with 4 units (one for each class)
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(encoded_questions, np.array(answer_labels), epochs=10)

# Function to get chatbot response
def get_response(question):
    encoded_question = encode_data([question])
    prediction = model.predict(encoded_question)
    response_index = np.argmax(prediction)
    return answers[response_index]

# Test the chatbot
print(get_response("Hello"))
print(get_response("How are you?"))
print(get_response("What is your name?"))
print(get_response("Goodbye"))