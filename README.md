# Semantic.py

## Overview: Semantic Demonstration Python Script
The "semantic.py" script is a Python application that demonstrates the use of spaCy, a popular natural language processing library. Specifically, it showcases how to calculate the similarity between words using spaCy's pre-trained English core model (en_core_web_md). This script can help you understand how spaCy's word vectors work and how they can be used to measure the semantic similarity between words.

## Usage
To run the "semantic.py" script, you can use Docker to set up a consistent environment. Here are the steps to run the script with Docker:

### Prerequisites
- Make sure you have Docker installed on your system.

### Step 1: Clone the Repository
```bash
git clone https://github.com/BrandenSysoutHelloWorld/semantic-similarity.git
cd .../semantic-similarity
```

### Step 2: Build the Docker Image
Run the following command to build a Docker image named "my-python-app" from the provided Dockerfile:

```bash
docker build -t semantic-similarity .
```

### Step 3: Run the Docker Container
Once the image is built, you can run a Docker container based on it:

```bash
docker run semantic-similarity
```

This command will execute the "semantic.py" script inside the container, and you'll see the results of word similarity calculations.

## Script Explanation
The "semantic.py" script does the following:

1. Imports the spaCy module and loads the en_core_web_md English core model.

2. Casts words ("cat," "monkey," "banana") to the model.

3. Calculates and prints the similarities between words based on the model.

4. Provides explanatory notes about the calculated similarities.

5. Demonstrates how to compare similarities between a set of custom words ("moderator," "admin," "user," "guest").

## Notes
The script's notes explain interesting observations about word similarities based on the spaCy model. It highlights how the model considers general facts and stereotypes when calculating similarity scores.

## Author
- Branden van Staden

Feel free to modify and experiment with the script to explore word similarities further or use it as a starting point for your own natural language processing tasks.