# Assignment 2

- Use a genAI tool to learn what the game of Yahtzee is
- Engineer the genAI tool to play Yahtzee with you
- Ask the genAI tool how to approach writing code for a Yahtzee scorer yourself
DO NOT ask the genAI tool to write code yet.

## Chat Conversations with ChatGPT

**User**: Can you provide me with information about the game of Yahtzee? I'm interested in learning its rules, strategies, and any helpful tips for playing. 

**ChatGPT**: Absolutely! Yahtzee is a classic dice game that is easy to learn and can be enjoyed by people of all ages. Here's an overview of the rules, strategies, and some helpful tips for playing:

### Rules of Yahtzee:

1. **Objective**: The objective of Yahtzee is to score points by rolling five dice to make certain combinations. The game consists of 13 rounds, and the player with the highest total score at the end wins.

2. **Rolling the Dice**: Each player takes turns rolling five dice. They can roll the dice up to three times per turn, trying to get the best combination possible.

3. **Scoring Categories**: After each roll, the player must choose a scoring category for that round. The categories include ones, twos, threes, fours, fives, and sixes (where you aim to collect as many of that number as possible); three of a kind, four of a kind, full house, small straight, large straight, Yahtzee (five of a kind), and chance.

4. **Scoring**: The score for each category is determined by the specific rules for that category. For example, in the "threes" category, the player scores the total sum of all dice showing the number three.

5. **Yahtzee Bonus**: If a player rolls a Yahtzee and has already scored 50 points in the Yahtzee category, they get a 100-point bonus. Subsequent Yahtzees will also earn an additional 100-point bonus each.

6. **Upper Section Bonus**: If a player scores 63 or more points in the upper section of the scorecard (ones through sixes), they get a 35-point bonus.

7. **Final Round and Total Score**: After 13 rounds, players tally their scores, including any bonuses, and the player with the highest total score wins.

### Strategies and Tips:

1. **Focus on the Upper Section**: In the early rounds, prioritize filling out the ones through sixes categories to aim for the upper section bonus. This will provide a good base score for your game.

2. **Maximize Yahtzees**: Try to roll as many Yahtzees as possible, as they offer substantial points, especially if you can earn the Yahtzee bonus. Keep track of your Yahtzee count to strategize effectively.

3. **Be Flexible**: Be flexible with your strategy based on the rolls you get. Sometimes it's worth taking a lower score in one category to aim for a higher score in another category later in the game.

4. **Use the Chance Category Wisely**: If you have a particularly bad roll or can't fit your roll into any other category, use the chance category to score the total sum of all dice.

5. **Pay Attention to the Full House and Small/Large Straights**: These categories can be challenging to achieve, but they offer good points. Try to keep your options open for these combinations early in the game.

6. **Watch Your Opponents**: Keep an eye on what categories your opponents are scoring in to adjust your strategy accordingly. If they're close to completing a high-scoring category, you might want to prioritize it to prevent them from getting ahead.

Overall, Yahtzee is a game of both luck and strategy. By understanding the rules and employing smart tactics, you can increase your chances of winning while still enjoying the excitement of the dice rolls.

**User**: Once I have a good understanding, could you engineer yourself to play Yahtzee with me?

**ChatGPT**: As an AI developed by OpenAI, I don't have the capability to engage in real-time interactive games or simulations. However, I can certainly help you understand the rules, strategies, and offer advice for playing Yahtzee. If you have any questions or need further assistance with the game, feel free to ask!

**User**: Once I have a good understanding, could you guide me on how to engineer a tool that can play Yahtzee with me?

**ChatGPT**: Certainly! Creating a tool to play Yahtzee with you can be a fun project. Here's a high-level overview of how you can engineer such a tool:

1. **Choose a Programming Language**: Select a programming language that you're comfortable with and that is suitable for the task. Popular choices include Python, Java, and C++.

2. **Design the Game Logic**: Develop the logic for the Yahtzee game, including functions to roll dice, score combinations, and keep track of the game state. You'll need to implement the rules of Yahtzee, including scoring rules, bonuses, and end-game conditions.

3. **User Interface (Optional)**: Decide whether you want a graphical user interface (GUI) for your Yahtzee game. If so, you can use libraries like Pygame (Python), JavaFX (Java), or Qt (C++) to create a visually appealing interface where players can interact with the game.

4. **Implement AI Player (Optional)**: If you want your tool to play against you, you'll need to develop an AI player. This AI should make decisions based on the current game state, evaluating possible moves and selecting the one that maximizes its expected score. Techniques like Monte Carlo simulations or heuristic search algorithms (e.g., minimax with alpha-beta pruning) can be used to develop the AI player.

5. **Testing and Debugging**: Test your tool thoroughly to ensure that it functions correctly and handles various scenarios and edge cases. Debug any issues that arise during testing.

6. **Refinement and Optimization (Optional)**: Once the basic functionality is implemented, you can refine and optimize your tool to improve its performance, user experience, and AI capabilities.

7. **Documentation and Deployment**: Document your code and provide clear instructions on how to use your Yahtzee tool. If you want to share it with others, consider packaging it for easy deployment, such as creating an executable file or a web application.

Here's a simple example in Python to get you started:

```python
import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(5)]

def score_dice(dice, category):
    # Implement scoring logic for different categories
    pass

def play_yahtzee():
    # Game loop
    while not game_over:
        # Player's turn
        roll = roll_dice()
        print("Your roll:", roll)
        # Ask player to choose a category and score the roll
        
        # AI's turn (if applicable)
        # Implement AI logic to select a category and score the roll
        
        # Update game state and check for end conditions

if __name__ == "__main__":
    play_yahtzee()
```

This is a basic outline, and you can expand and customize it based on your preferences and programming skills. Have fun engineering your Yahtzee tool!

**User**: I've learned about the game of Yahtzee and how to play it. Now, I'm looking to write a scorer function in Python. Could you provide me with insights on how to approach writing code for a Yahtzee scorer? What factors should I consider?

**ChatGPT**: Certainly! Writing a scorer function for Yahtzee involves implementing the logic to calculate scores based on the combinations rolled and chosen by the player. Here are some insights and factors to consider when approaching the task:

### 1. Understand the Scoring Categories:
   - Familiarize yourself with the scoring categories in Yahtzee, such as ones, twos, threes, fours, fives, sixes, three of a kind, four of a kind, full house, small straight, large straight, Yahtzee, and chance.
   - Each category has specific scoring rules, which you'll need to implement in your scorer function.

### 2. Design the Scorer Function:
   - Decide on the input parameters for your scorer function. Typically, the function should take the dice roll and the chosen scoring category as inputs.
   - Consider whether your function should handle edge cases, such as invalid inputs or incorrect category selections.

### 3. Implement Scoring Logic:
   - Write code to calculate the score for each scoring category based on the dice roll.
   - Ensure that your code accurately follows the rules for each category. For example, in the "three of a kind" category, the score is the sum of all dice if there are at least three dice with the same value.

### 4. Handle Special Cases and Bonuses:
   - Account for special cases, such as Yahtzee bonuses and the upper section bonus for scoring 63 or more points in the ones through sixes categories.
   - Implement logic to calculate bonuses accurately and add them to the total score.

### 5. Test Your Scorer Function:
   - Test your scorer function with various combinations of dice rolls and scoring categories to ensure that it produces the correct scores.
   - Consider writing unit tests to automate the testing process and verify the correctness of your implementation.

### Example Code Structure:
```python
def calculate_score(dice_roll, category):
    # Implement scoring logic for different categories
    if category == "ones":
        return dice_roll.count(1) * 1
    elif category == "twos":
        return dice_roll.count(2) * 2
    # Implement scoring logic for other categories
    else:
        return 0  # Handle invalid category

def yahtzee_score(dice_roll, category):
    score = calculate_score(dice_roll, category)
    # Implement bonus logic (e.g., Yahtzee bonus)
    return score

# Example usage
roll = [1, 2, 3, 4, 5]
chosen_category = "ones"
score = yahtzee_score(roll, chosen_category)
print("Score for", chosen_category, ":", score)
```

### Additional Considerations:
- Keep your code modular and easy to understand by breaking it into smaller functions if necessary.
- Consider adding error handling to handle unexpected inputs or edge cases gracefully.
- Document your code effectively, including function signatures, parameters, and return values, to make it easier for others (and yourself) to understand and use your scorer function.

By following these insights and considering the factors mentioned above, you'll be well-equipped to write an effective scorer function for Yahtzee in Python.

## Chat Conversations with ChatGPt (Additional):

**User**: Very well. Write a function def score(dice: list[int]) -> dict[str, int] which returns a dictionary containing what the yahtzee hand represented by the list dice would score in each Yahtzee category.

**ChatGPT**: Sure, here's a Python function `score` that takes a list of integers representing the dice rolls and returns a dictionary containing the score for each Yahtzee category:

```python
from collections import Counter

def score(dice):
    result = {}
    counts = Counter(dice)
    
    # Ones through Sixes categories
    for i in range(1, 7):
        result[f"{i}s"] = counts[i] * i
    
    # Three of a Kind, Four of a Kind, Chance categories
    result['Three of a Kind'] = sum(dice) if any(count >= 3 for count in counts.values()) else 0
    result['Four of a Kind'] = sum(dice) if any(count >= 4 for count in counts.values()) else 0
    result['Chance'] = sum(dice)
    
    # Full House
    if 2 in counts.values() and 3 in counts.values():
        result['Full House'] = 25
    else:
        result['Full House'] = 0
    
    # Small Straight
    if any(all(i in dice for i in range(start, start+4)) for start in range(1, 4)):
        result['Small Straight'] = 30
    else:
        result['Small Straight'] = 0
    
    # Large Straight
    if all(i in dice for i in range(1, 6)) or all(i in dice for i in range(2, 7)):
        result['Large Straight'] = 40
    else:
        result['Large Straight'] = 0
    
    # Yahtzee
    result['Yahtzee'] = 50 if any(count == 5 for count in counts.values()) else 0
    
    return result

# Example usage:
dice = [1, 2, 3, 4, 5]  # Example dice rolls
print(score(dice))
```

This function calculates the score for each category based on the given dice rolls and returns a dictionary where the keys are the names of the categories and the values are the corresponding scores.

**User**: Ok can you redefine what exactly is the function trying to do.

**ChatGPT**: Certainly! The `score` function is designed to calculate the score for each Yahtzee category based on a given set of dice rolls. Here's a breakdown of what the function does:

1. **Input**: The function takes a list of integers representing the dice rolls as its input parameter.

2. **Dice Counts**: It calculates the count of each number rolled using the `Counter` class from the `collections` module.

3. **Scoring Categories**: For each Yahtzee category, the function determines the score based on the rules of the game:

   - **Ones through Sixes**: Scores the sum of all dice showing the corresponding number (e.g., the sum of all ones, twos, etc.).
   - **Three of a Kind**: Scores the sum of all dice if at least three dice have the same number.
   - **Four of a Kind**: Scores the sum of all dice if at least four dice have the same number.
   - **Full House**: Scores 25 if there are two dice with one number and three dice with another number.
   - **Small Straight**: Scores 30 if there is a sequence of four consecutive numbers in the dice roll.
   - **Large Straight**: Scores 40 if there is a sequence of five consecutive numbers in the dice roll.
   - **Yahtzee**: Scores 50 if all five dice have the same number.
   - **Chance**: Scores the sum of all dice, regardless of the combination.

4. **Output**: The function returns a dictionary where the keys are the names of the Yahtzee categories and the values are the corresponding scores for those categories based on the input dice rolls.

Overall, the `score` function provides a convenient way to determine the score for each Yahtzee category, allowing players to easily track their progress during the game.
