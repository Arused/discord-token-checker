import colorama
from time import sleep
import requests

class DiscordTokenChecker:
    @staticmethod
    def check_token(token):
        headers = {
            'Authorization': token,
            'Content-Type': 'application/json'
        }
        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        return response.status_code == 200

    @staticmethod
    def collect_tokens():
        with open('tokens.txt', 'r') as file:
            tokens = file.read().splitlines()
        return tokens

    @staticmethod
    def save_worked_tokens(worked_tokens):
        with open('tokens_worked.txt', 'w') as file:
            for token in worked_tokens:
                file.write(token + '\n')

    @staticmethod
    def show_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end='\r'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(length * iteration // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
        if iteration == total:
            print()

    @staticmethod
    def run():
        print("\033[38;2;0;128;255mWDiscord Token Checker\033[0m")
        sleep(1)
        print("Initializing...")
        sleep(1)
        print("Reading tokens from file...")
        sleep(1)
        tokens = DiscordTokenChecker.collect_tokens()
        total_tokens = len(tokens)
        print(f"Found {total_tokens} tokens.")
        sleep(1)
        print("Checking token validity...")
        sleep(1)
        worked_tokens = []
        for i, token in enumerate(tokens, start=1):
            DiscordTokenChecker.show_progress_bar(i, total_tokens, prefix='\033[38;2;128;0;255mProgress:', suffix='Complete', length=50)
            sleep(0.1)
            if DiscordTokenChecker.check_token(token):
                worked_tokens.append(token)
        print("Token check completed!")
        sleep(1)
        print(f"Found {len(worked_tokens)} working tokens.")
        sleep(1)
        if len(worked_tokens) > 0:
            print("Saving worked tokens to file...")
            sleep(1)
            DiscordTokenChecker.save_worked_tokens(worked_tokens)
            print("Worked tokens saved successfully!")
            sleep(1)
            print('\033[38;2;0;255;0mYou can find the working tokens in "tokens_worked.txt".\033[0m')
        else:
            print("\033[38;2;255;0;0mNo working tokens found. Check your tokens or try again later.\033[0m")
        sleep(1)
        print("\033[38;2;0;128;255mThank you for using Discord Token Checker!\033[0m")

class TokenGenerator:
    @staticmethod
    def generate_tokens(num_tokens):
        tokens = []
        for _ in range(num_tokens):
            token = 'YOUR_RANDOM_TOKEN_GENERATION_LOGIC'  # Replace with your token generation logic
            tokens.append(token)
        return tokens

    @staticmethod
    def save_tokens(tokens):
        with open('tokens.txt', 'w') as file:
            for token in tokens:
                file.write(token + '\n')

    @staticmethod
    def run():
        print("\033[38;2;0;128;255mWelcome to Token Generator!\033[0m")
        sleep(1)
        num_tokens = int(input("Enter the number of tokens to generate: "))
        sleep(1)
        print("Generating tokens...")
        sleep(1)
        tokens = TokenGenerator.generate_tokens(num_tokens)
        TokenGenerator.save_tokens(tokens)
        print("Tokens saved successfully!")
        sleep(1)
        print('\033[38;2;0;255;0mYou can find the generated tokens in "tokens.txt".\033[0m')
        sleep(1)
        print("\033[38;2;0;128;255mThank you for using Token Generator!\033[0m")

def print_banner():
    banner = ['8', '.d8b.', '_.d8888888b._', '.88888888888888b.', 'd88888888888888888b', '8888888888888888888',
              'Y88888888888888888P', "'Y8888888888888P'", "_..._ 'Y88888P' _..._", '.d88888b. Y888P .d88888b.',
              'd888888888b 888 d88888888b', "888P  `Y8888888888P'  Y888", 'b8b    Y88888888P    d8Y',
              '`"\'  #############  \'"`', 'dP d8b Yb', 'Ob=dP d888b Yb=dO', '`"` O88888O `"`', "'Y8P'", "'"]

    color = "\033[38;2;225;-;255m"
    new_banner = ""
    counter = 0
    for line in banner:
        new_banner += color.replace('-', str(counter * int(255 / len(banner)))) + ' ' * int((80 - len(line)) / 2) + line + "\033[38;2;255;255;255m\n"
        counter += 1

    print(new_banner)

if __name__ == '__main__':
    colorama.init(autoreset=True)
    print_banner()
    sleep(2)
    print("\n\033[38;2;0;128;255mg Fastest Token Checker\033[0m\n")
    sleep(1)
    print("Please select an option:")
    print("[1] Discord Token Checker")
    print("[2] Token Generator")

    selected_option = input("Enter your choice: ")

    if selected_option == '1':
        DiscordTokenChecker.run()
    elif selected_option == '2':
        TokenGenerator.run()
    else:
        print("\033[38;2;255;0;0mInvalid option. Exiting...\033[0m")
