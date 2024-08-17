class GeneratorClass:
    @staticmethod
    def Generate_Key_Function():
        open_alphabet =   'abcdefghijklmnopqrstuvwxyz'
        cipher_alphabet = 'zyoinasgrdfucmlwthpbvkqjxe'
        key_mapping = dict(zip(open_alphabet, cipher_alphabet))
        return key_mapping

class ALiceEncrypterClass:
    @staticmethod
    def Encrypter_Function(_Emessage, _Ekey):
        Encrypted_message = ''
        for char in _Emessage:
            if char.isalpha():
                char = char.lower()
                if char in _Ekey:
                    Encrypted_message += _Ekey[char]
                else:
                    Encrypted_message += char
            else:
                Encrypted_message += char
        return Encrypted_message

class BobDecrypterClass:
    @staticmethod
    def Decrypter_Function(_Dciphertext, _Dkey):
        Decrypted_message = ''
        for char in _Dciphertext:
            if char.isalpha():
                char = char.lower()
                if char in _Dkey.values():
                    Decrypted_message += next(k for k, v in _Dkey.items() if v == char)
                else:
                    Decrypted_message += char
            else:
                Decrypted_message += char
        return Decrypted_message

class Hacker_OscarClass:
    @staticmethod
    def receive_message(encrypted_message):

        print("------ Oscar received the encrypted message from Alice via unsecured network ------:\n", encrypted_message.upper())
        print()
        print("----------Attempting to hack the message using letter frequency analysis...---------")
        print()

        sorted_letters = [('z', 63), ('m', 55),('r', 53), ('b', 48), ('n', 48), ('l', 40), ('p', 38), ('u', 31),
                          ('i', 30),('s', 25), ('h', 24), ('v', 21), ('g', 18), ('c', 18), ('o', 16), ('q', 11),
                          ('w', 10), ('a', 9), ('y', 8), ('k', 6), ('x', 5), ('f', 4), ('j', 1), ('e', 0),
                          ('t', 0), ('d', 0)]

        sorted_bigrams = [('es', 4), ('et', 3), ('at', 3), ('mı', 2), ('ng', 2), ('as', 2), ('ao', 2), ('mv', 1),
                          ('on', 1), ('sn', 1), ('ql', 1)]

        sorted_trigrams = [('nhi', 7), ('etd', 7), ('ell', 1), ('top', 1), ('pey', 1), ('ton', 1), ('bun', 1),
                           ('cvi', 1)]

        english_frequencies = ['e', 't', 'a', 'n', 'i', 'o', 's', 'l', 'd', 'g', 'r', 'u', 'h', 'm', 'c', 'w', 'p',
                               'f', 'b', 'v', 'y', 'k', 'x', 'q', 'j', 'z']

        hacked_key1 = {}
        for i in range(min(len(sorted_letters), len(english_frequencies))):
            encrypted_letter = sorted_letters[i][0]
            hacked_key1[encrypted_letter] = english_frequencies[i]

        hacked_message1 = ''.join(hacked_key1.get(char.lower(), char) for char in encrypted_message)

        hacked_bigrams = {
            'es': 'as', 'et': 'an', 'at': 'in', 'mı': 'me',
            'ng': 'of', 'as': 'is', 'ao': 'it', 'mv': 'my',
            'on': 'to', 'sn': 'so', 'ql': 'on',
        }
        hacked_message2 = hacked_message1
        for key, value in hacked_bigrams.items():
            hacked_message2 = hacked_message2.replace(key, value)

        hacked_message2 = ''.join(hacked_bigrams.get(char.lower(), char) for char in hacked_message1)

        hacked_trigrams = {
            'nhi': 'the','etd': 'and','ell': 'all',
            'top': 'now','pey': 'way','ton': 'not',
            'bun': 'but','cvi': 'mud'
        }

        hacked_message3 = hacked_message2
        for key, value in hacked_trigrams.items():
            hacked_message3 = hacked_message3.replace(key, value)

        print("----------------------- Final Hacked message ------------------------------\n:", hacked_message3.upper())
        print()

def main():

    key = GeneratorClass.Generate_Key_Function()

    alice_textEnglish = (
        "I remember as a child, and as a young budding naturalist, spending all my time \n observing and testing "
        "the world around me moving pieces, altering the flow of things, and documenting \n ways the world responded"
        " to me. Now, as an adult and a professional naturalist, I’ve approached language \n in the same way, "
        "not from an academic point of view but as a curious child still building little \n mud dams in creeks "
        "and chasing after frogs. So this book is an odd thing: it is a naturalist’s walk \n through the "
        "language-making landscape of the English language, and following in the naturalist’s \n tradition it "
        "combines observation, experimentation, speculation, and documentation \n activities we don’t normally"
        " associate with language.")
    ciphertext_english = ALiceEncrypterClass.Encrypter_Function(alice_textEnglish, key)
    print("----------------- Alice send English encrypted text  -----------------------:\n", ciphertext_english.upper())
    print()
    decrypted_text_english = BobDecrypterClass.Decrypter_Function(ciphertext_english, key)
    print("------------------- Bob got English text and decrypted it   --------------------\n:", decrypted_text_english)
    print()
    Hacker_OscarClass.receive_message(ciphertext_english)

if __name__ == "__main__":
    main()
