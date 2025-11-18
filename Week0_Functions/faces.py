
def convert(sentence):
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")
    return sentence

def main():
    sentence = input("Please enter your sentence: ")
    sentence = convert(sentence)
    print(sentence)

main()