# This program will provide statistics for 
# grades in a class.

def receive_scores():
    scores = []
    
    while True:
        score = float(input("Enter a score: \n"))
        if score < 0:
            if len(scores) == 0:
                print("You must enter one value.")
            else:
                break
        else:
            scores.append(score)
            
    return scores

def calculate_average(scores):
    total = 0.0
    for i in range(len(scores)):
        total += scores[i]
    
    return total / len(scores)

def calculate_minimum(scores):
    minimum = scores[0]
    for i in range(1, len(scores)):
        if minimum > scores[i]:
            minimum = scores[i]
    
    return minimum

def calculate_maximum(scores):
    maximum = scores[0]
    for i in range(1, len(scores)):
        if maximum < scores[i]:
            maximum = scores[i]
    
    return maximum

def results(maximum, minimum, average):
    print(f"""Results: \n
          Maximum: {maximum} \n
          Minimum: {minimum} \n
          Average: {average}
          """)

def main():
    scores = receive_scores()
    maximum = calculate_maximum(scores)
    minimum = calculate_minimum(scores)
    average = calculate_average(scores)
    
main()   
