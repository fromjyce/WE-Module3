# Assignment 4

The 1980s saw a shift from Natural Language Processing techniques aiming to codify the grammatical rules of natural language towards techniques aiming to use statistical models to generate text. One early idea which technically isn’t “AI” seeing as it is “memorizing” the training data and yet introduces us to the power contained in statistical techniques of text generation is the idea of Markov chains. Write a python function generate(filename: str, start_words: list[str], chain_length: int, num_generated: int) -> str which takes a filename, a chain length, a list of start words which has to be exactly as long as the chain_length (why?), and an integer num_generated and returns a sentence num_generated words long which sounds similar to the text contained in filename.


## Chat Conversations with ChatGPT

**User**: I'm interested in understanding Markov chains and how they can be used for text generation.

**ChatGPT**: Markov chains are mathematical systems used to model random processes where the next state depends only on the current state, with no consideration of the sequence of events that preceded it. In the context of text generation, Markov chains can be employed to generate new text based on a given input text.

Here's a simplified explanation of how Markov chains work for text generation:

1. **Building the Model**: 
   - Given a text corpus, the first step is to tokenize the text into words or characters, depending on the granularity desired for the model.
   - Then, the occurrences of each word or character and the probabilities of transitions between them are calculated. This is done by counting the frequency of each word or character and the occurrences of each pair of consecutive words or characters in the text.

2. **Constructing the Chain**:
   - Each word or character becomes a state in the Markov chain.
   - The probability of transitioning from one state to another is determined by the frequency of occurrence of those states in the input text.

3. **Generating New Text**:
   - To generate new text, you start with an initial state (a word or character).
   - Then, you randomly select the next state based on the probabilities of transition from the current state.
   - Repeat this process, selecting the next state based on the current state, until the desired length of text is generated or until a terminal state is reached.

Here's a simple example:

Let's say we have the following input text:
```
"the cat sat on the mat"
```

We tokenize it into words:
```
["the", "cat", "sat", "on", "the", "mat"]
```

Then, we construct a first-order Markov chain:
```
{
  "the": ["cat", "mat"],
  "cat": ["sat"],
  "sat": ["on"],
  "on": ["the"],
  "mat": [END]
}
```
Note: "END" represents the end of a sentence.

To generate new text:
- Start with the initial state "the".
- Randomly choose the next word based on the probabilities of transition from "the" (e.g., "cat").
- Repeat this process until reaching the terminal state or the desired length of text.

Markov chains are simple yet powerful tools for text generation, commonly used in applications like predictive typing, generating random text for testing, and even in more sophisticated natural language processing tasks. However, they have limitations, such as the inability to capture long-range dependencies in text or context.

**User**: Could you explain the concept of Markov chains and how they differ from traditional NLP techniques?

**ChatGPT**: Certainly! Markov chains are mathematical models used to represent stochastic processes where the next state of the system depends only on the current state, with no memory of previous states beyond the current one. They're used in various fields to model random processes such as weather patterns, stock prices, and text generation.

Here's a more detailed explanation of Markov chains:

1. **State**: A Markov chain consists of a set of states, each representing a possible condition or situation of the system being modeled.

2. **Transition Probabilities**: There are probabilities associated with transitioning from one state to another. These probabilities are typically represented in a transition matrix or graph, where each row corresponds to the current state, and each column corresponds to the possible next states along with their probabilities.

3. **Memorylessness**: The key characteristic of Markov chains is that they satisfy the Markov property, which states that the probability of transitioning to the next state depends only on the current state and not on the sequence of events that preceded it. In other words, the future behavior of the system is independent of its past behavior given its current state.

4. **Stationary Distribution**: Under certain conditions, Markov chains converge to a stationary distribution, where the probabilities of being in each state stabilize over time. This stationary distribution represents the long-term behavior of the system.

Now, let's discuss how Markov chains differ from traditional Natural Language Processing (NLP) techniques:

1. **Scope of Context**:
   - Markov chains typically consider only local dependencies between adjacent states. In the context of text generation, this means that the next word is chosen based solely on the current word, without considering any contextual information from previous words. Traditional NLP techniques, on the other hand, often consider broader context, including syntactic structure, semantics, and even discourse coherence.

2. **Complexity**:
   - Markov chains are relatively simple models compared to many traditional NLP techniques, which may involve complex algorithms, machine learning models, and large-scale data processing. While Markov chains are effective for certain tasks like basic text generation, they may struggle to capture more nuanced linguistic patterns and semantic relationships present in natural language.

3. **Long-range Dependencies**:
   - Markov chains have limitations in capturing long-range dependencies in sequences of data. They assume that the current state contains all the information needed to predict the next state, which may not always hold true, especially in language where distant words can influence each other's meanings and syntactic roles. Traditional NLP techniques often address this issue through techniques like recurrent neural networks (RNNs) or transformers, which are designed to capture long-range dependencies.

In summary, while Markov chains provide a simple and intuitive framework for modeling stochastic processes, including text generation, they have limitations in capturing complex linguistic patterns and long-range dependencies compared to traditional NLP techniques. However, they remain useful in various applications where simplicity and efficiency are prioritized.

**User**: Additionally, could you provide me with guidance on writing a Python function that generates text using Markov chains?

**ChatGPT**: Certainly! Below is a Python function that generates text using Markov chains. This function takes a text corpus as input and generates new text based on the learned probabilities of transitioning between words.

```python
import random

def generate_markov_text(corpus, order=1, length=50):
    """
    Generate text using Markov chains.
    
    Args:
    - corpus (str or list): The input text corpus.
    - order (int): The order of the Markov chain (default is 1).
    - length (int): The length of the generated text (default is 50).
    
    Returns:
    - str: The generated text.
    """
    # If the input corpus is a string, split it into a list of words
    if isinstance(corpus, str):
        corpus = corpus.split()
    
    # Initialize a dictionary to store transition probabilities
    markov_dict = {}
    
    # Construct the Markov chain
    for i in range(len(corpus) - order):
        current_state = tuple(corpus[i:i + order])
        next_state = corpus[i + order]
        if current_state not in markov_dict:
            markov_dict[current_state] = []
        markov_dict[current_state].append(next_state)
    
    # Generate text
    current_state = random.choice(list(markov_dict.keys()))
    generated_text = list(current_state)
    
    while len(generated_text) < length:
        if current_state in markov_dict:
            next_word = random.choice(markov_dict[current_state])
            generated_text.append(next_word)
            current_state = tuple(generated_text[-order:])
        else:
            break
    
    return ' '.join(generated_text)

# Example usage:
input_corpus = "the cat sat on the mat"
generated_text = generate_markov_text(input_corpus, order=1, length=20)
print("Generated Text:", generated_text)
```

In this function:

- `generate_markov_text` takes three arguments: `corpus` (the input text corpus), `order` (the order of the Markov chain, which specifies how many previous states are considered when predicting the next state), and `length` (the desired length of the generated text).
- The function first constructs a Markov chain based on the input text corpus by calculating transition probabilities between consecutive words or sequences of words (depending on the specified order).
- Then, it randomly generates new text by starting with a random initial state and iteratively selecting the next word based on the transition probabilities learned from the corpus.
- The function returns the generated text as a string.

You can adjust the `order` parameter to experiment with different levels of context for predicting the next word. Higher order values capture more context but may result in overfitting, especially for smaller corpora. Additionally, you can modify the `length` parameter to control the length of the generated text.
