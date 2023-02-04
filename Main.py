from Functions import word_count_text, word_count_file
import pyfiglet

printer = """
1. Count Words From Input
2. Count Words From File
"""

print("")
print(pyfiglet.figlet_format("Words Counting App",justify="center",width=110))
print(pyfiglet.figlet_format("Created By Shinjan",justify="center",width=110))

while True:
    try:
        print(printer)
        choose_input = int(input("Enter Your Choice From The Above Lines In Numbers: "))

    except ValueError:
        print("")
        print("Kindly Enter An Integer Value!")
        continue

    if choose_input == 1:
        print("")
        user_input1 = input("Enter The Text: ")
        print("")
        result_1 = word_count_text(user_input1)
        print(f"The Total Words In Your Text Was {result_1}!")

    else:

        try:
            print("")
            filepath1 = input("Enter The Filepath (Data.txt): ")
            print("")
            result_2 = word_count_file(filepath1)
            print(f"The Total Words In Your File Was {result_2}!")

        except FileNotFoundError or ValueError:
            print("Sorry, No Such File Found In That Filepath!")
            continue
