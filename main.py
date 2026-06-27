import random as r

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalize = [True, False] 
numbers = ['0','1','2','3','4','5','6','7','8','9'] 
symbols = ['!','#','$','%','&','(',')','*','+']

def run():
    global letters
    global capitalize
    global numbers
    global symbols

    length = 0
    num_letters = 0
    num_numbers = 0
    num_symbols = 0
    password = ""

    response1 = input("Do you want to completely randomize this password? It will choose the length and density of characters for you. (Y/N) ").strip().lower()
    randomize = True if response1 == 'y' else False

    if randomize:
        length = r.randint(18,30)
        while(length > 0):
            length -= 1
            cap = r.choice(capitalize)
            char_choice = r.choice([letters,numbers,symbols])
            choice_type = char_choice
            char_choice = char_choice[r.randint(0,len(char_choice)-1)]
            if choice_type == letters and cap:
                char_choice = char_choice.capitalize()
            password += char_choice
                            
    else:
        num_letters = int(input("How many letters do you want to include? "))
        num_numbers = int(input("How many numbers do you want to include? "))
        num_symbols = int(input("How many symbols do you want to include? "))
        while num_letters + num_numbers + num_symbols > 0:
            cap = r.choice(capitalize)
            choices = []
            if num_letters > 0:
                choices.append(letters)
            if num_numbers > 0:
                choices.append(numbers)
            if num_symbols > 0:
                choices.append(symbols)
            
            cap = r.choice(capitalize)
            char_choice = r.choice(choices)
            choice_type = char_choice
            char_choice = char_choice[r.randint(0,len(char_choice)-1)]
            
            if choice_type is letters:
                num_letters -= 1
                if cap:
                   char_choice = char_choice.capitalize()
            elif choice_type is numbers:
                num_numbers -=1 
            elif choice_type is symbols:
                num_symbols -=1

            password += char_choice

    print(f"New Password: {password}")

run()  
