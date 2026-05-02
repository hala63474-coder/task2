A Python CLI-based AI program that analyzes the sentiment of user input and predicts whether it is Positive, Negative, or Neutral.

- Detects positive and negative keywords in any sentence
- Classifies sentiment as Positive / Negative / Neutral
- Colored terminal output for better readability
- Saves all results with timestamps to results.txt
- Shows total number of sentences analyzed per session
- Handles empty and invalid input gracefully
- Runs continuously until the user types exit


How It Works:
User enters a sentence
The program converts it to lowercase
It counts matches from the positive and negative word lists
If positive count > negative → Positive
If negative count > positive → Negative
If equal → Neutral
