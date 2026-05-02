import datetime

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

positive_words = [
    "good", "great", "excellent", "amazing", "love", "happy", "best",
    "wonderful", "fantastic", "awesome", "brilliant", "nice", "superb",
    "perfect", "joy", "excited", "beautiful", "glad", "enjoy", "positive",
    "fun", "laugh", "blessed", "grateful", "thankful", "proud", "succeed"
]

negative_words = [
    "bad", "sad", "hate", "terrible", "poor", "angry", "worst",
    "awful", "horrible", "disgusting", "boring", "ugly", "fail",
    "disappoint", "miserable", "dreadful", "annoying", "frustrating",
    "useless", "pathetic", "stupid", "painful", "regret", "fear", "cry"
]

RESULTS_FILE = "results.txt"

def save_result(sentence, pos_count, neg_count, result):
    """Save each analysis result to a text file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"Sentence : {sentence}\n")
        f.write(f"Positive : {pos_count}  |  Negative: {neg_count}\n")
        f.write(f"Result   : {result}\n")
        f.write("-" * 40 + "\n")

def analyze(text):
    """Return (positive_count, negative_count, result_label)."""
    text_lower = text.lower()
    pos_count = sum(1 for w in positive_words if w in text_lower)
    neg_count = sum(1 for w in negative_words if w in text_lower)

    if pos_count > neg_count:
        label = "Positive"
    elif neg_count > pos_count:
        label = "Negative"
    else:
        label = "Neutral"

    return pos_count, neg_count, label

def print_result(pos_count, neg_count, label):
    """Print the result with colors."""
    print(f"Positive words found: {GREEN}{pos_count}{RESET}")
    print(f"Negative words found: {RED}{neg_count}{RESET}")

    if label == "Positive":
        color = GREEN
    elif label == "Negative":
        color = RED
    else:
        color = YELLOW

    print(f"AI Result: {BOLD}{color}{label}{RESET}")


def main():
    print(f"\n{CYAN}{BOLD}{'='*45}")
    print("   AI Sentiment Analyzer — M.Training Academy")
    print(f"{'='*45}{RESET}")
    print(f"Type a sentence to analyze, or {BOLD}'exit'{RESET} to quit.\n")

    total = 0  # total sentences analyzed

    while True:
        user_text = input(f"{CYAN}Enter a sentence: {RESET}")

        # Exit condition
        if user_text.lower() == "exit":
            print(f"\n{YELLOW}Program stopped.{RESET}")
            print(f"Total sentences analyzed: {BOLD}{total}{RESET}\n")
            break

        # Empty input
        if user_text.strip() == "":
            print(f"{RED}Empty input is not allowed. Please try again.{RESET}\n")
            continue

        # Analyze
        total += 1
        pos, neg, label = analyze(user_text)

        print()
        print_result(pos, neg, label)
        save_result(user_text, pos, neg, label)
        print(f"{YELLOW}(Result saved to {RESULTS_FILE}){RESET}")
        print(f"Sentences analyzed so far: {BOLD}{total}{RESET}\n")

if __name__ == "__main__":
    main()