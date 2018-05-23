#!/usr/bin/env python3

def display_welcome():
    print("**************************************")
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    score_total = 0
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
                score_total += score
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    average = sum(scores) / len(scores)
    median = 0
    if(len(scores)%2==0):
        n1 = scores[int(len(scores)/2-1)]
        n2 = scores[int(len(scores)/2)]
        median = round((n1 + n2)/2,2)
    else:
        median = scores[int(len(scores)/2)]
    # times
                
    # format and display the result
    print()
    print("Total:\t\t\t", sum(scores))
    print("Number of Scores:\t", len(scores))
    print("Average Score:\t\t", average)
    print("Low Score:\t\t",min(scores))
    print("High Score:\t\t", max(scores))
    print("Median Score:\t\t",median)

def main():
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


