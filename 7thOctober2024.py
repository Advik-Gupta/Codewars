def solution(number):
    multiples = []
    if (number < 0):
        return 0
    else:
        i = 0
        while i < number:
            if(i%3 == 0 or i%5 == 0):
                multiples.append(i)
            i = i + 1
    
    sumOfMultiples = sum(multiples)

    return(sumOfMultiples)

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


def spin_words(sentence):
    words = sentence.split(' ')
    newSentence = ''
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
        newSentence = newSentence + word + ' '
    print(newSentence.strip())
    
# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])