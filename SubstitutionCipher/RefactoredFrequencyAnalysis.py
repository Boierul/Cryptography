import operator
import sys

# Enum class to make the console text colorful
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

cipher = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt
  wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""


class Attack:
    # Constructor to intialize the values
    def __init__(self):
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.plain_char_left = "abcdefghijklmnopqrstuvwxyz"
        self.cipher_char_left = "abcdefghijklmnopqrstuvwxyz"
        self.freq = {}
        self.key = {}
        self.freq_eng ={'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}
        self.mappings = {}

    # Calculate frequencies in the cipher
    def calculate_freq(self, cipher):
        for c in self.alphabet:
            self.freq[c] = 0

        # Go through the cipher and verify the frequency of that letter in the text
        letterCount = 0
        for c in cipher:
            if c in self.freq:
                self.freq[c] += 1
                letterCount += 1

        # Checks the occurring frequency of a letter
        for c in self.freq:
            self.freq[c] = round(self.freq[c]/letterCount, 4)

    # Format the result
    def print_freq(self):
        newLineCount = 0
        for c in self.freq:
            print(c, ':', self.freq[c], ' ', end='')
            if newLineCount % 3 == 2:
                print()
            newLineCount += 1

    # Assign alphabet letters to the cipher to find the content of the message
    def calculate_matches(self):
        for cipher_char in self.alphabet:
            map = {}
            for plain_char in self.alphabet:
                map[plain_char] = round(abs(self.freq[cipher_char] - self.freq_eng[plain_char]), 4)
            self.mappings[cipher_char] = sorted(map.items(), key=operator.itemgetter(1))

    # Function responsible for mapping the used letters
    def set_key_mapping(self, cipher_char, plain_char):
        if cipher_char not in self.cipher_char_left or plain_char not in self.plain_char_left:
            print("ERROR: keymapping invalid", cipher_char, plain_char)
            sys.exit(-1)
        self.key[cipher_char] = plain_char
        self.plain_char_left = self.plain_char_left.replace(plain_char, '')
        self.cipher_char_left = self.cipher_char_left.replace(cipher_char, '')

    # Function is checking if the char is in the ciphertext
    #  if yes, it is replacing the char with the plain-char from the field
    def guess_key(self):
        for cipher_char in self.cipher_char_left:
            for plain_char, diff in self.mappings[cipher_char]:
                if plain_char in self.plain_char_left:
                    self.key[cipher_char] = plain_char
                    self.plain_char_left = self.plain_char_left.replace(plain_char, '')
                    break

    # Return the guess key
    def get_key(self):
        return self.key

def decrypt(key, cipher):
    message = ""
    for c in cipher:
        if c in key:
            message += key[c]
        else:
            message += c
    return message


# Main code
print()

attack = Attack()
attack.calculate_freq(cipher)
attack.print_freq()
attack.calculate_matches()
print()
print()

attack.set_key_mapping('r', 'e')
attack.set_key_mapping('v', 'c')
attack.set_key_mapping('m', 'a')
attack.set_key_mapping('p', 'h')
attack.set_key_mapping('w', 'i')
attack.set_key_mapping('s', 'p')
attack.set_key_mapping('u', 'r')
attack.set_key_mapping('x', 'f')
attack.set_key_mapping('e', 'v')
attack.set_key_mapping('q', 'k')
attack.set_key_mapping('t', 'y')
attack.set_key_mapping('d', 'd')
attack.set_key_mapping('c', 'w')
attack.set_key_mapping('a', 'x')
attack.set_key_mapping('f', 'q')

print("-------------------")
print()

attack.guess_key()
key = attack.get_key()

print(key)
print()
print("-------------------")
print()

message = decrypt(key, cipher)
message_lines = cipher.splitlines()
cipher_lines = message.splitlines()
for i in range(len(message_lines)):
    print(bcolors.WARNING + 'Plaintext:' + bcolors.ENDC, message_lines[i])
    print(bcolors.OKBLUE + 'Ciphertext' + bcolors.ENDC, cipher_lines[i])

print()
print("The full decrypted text is:")
for i in range(len(message_lines)):
    print(bcolors.OKBLUE + cipher_lines[i] + bcolors.ENDC)


# for c in attack.mappings:
#     print(c, attack.mappings[c])

# General frequency of letters in a english text
letter_freq = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}

