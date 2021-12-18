import time
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--char1", type=str)
    parser.add_argument("--char2", type=str)
    args = parser.parse_args()

    char1 = args.char1
    char2 = args.char2
    print(char1)
    file_question = open(char1, "r")
    text_question = file_question.readlines()
    with open(char2, 'r') as file_answer:
        text_answer = file_answer.readlines()
        time.sleep(1.5)

        for i in range(len(text_question)):
            print(text_question[i].strip())
            time.sleep(0.05*len(text_question[i].strip()))
            try:    
                print(text_answer[i].strip())
                time.sleep(0.05*len(text_answer[i].strip()))
            except IndexError:
                pass
        file_question.close()
if __name__ == '__main__':
    main()

