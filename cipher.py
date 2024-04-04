##############################################################################
# COMPONENT:
#    CIPHER01
# Author:
#    Br. Helfrich, Kyle Mueller, <your name here if you made a change>
# Summary:
#    Implement your cipher here. You can view 'example.py' to see the
#    completed Caesar Cipher example.
##############################################################################


##############################################################################
# CIPHER
##############################################################################
class Cipher:
    def __init__(self):
        # TODO: Insert anything you need for your cipher here
        pass

    def get_author(self):
        # TODO: Return your name
        return "Kaleb Bradford"

    def get_cipher_name(self):
        # TODO: Return the cipher name
        return "AutoKey Cipher"

    ##########################################################################
    # GET CIPHER CITATION
    # Returns the citation from which we learned about the cipher
    ##########################################################################
    def get_cipher_citation(self):
        # TODO: This function should return your citation(s)
        return "citation: http://practicalcryptography.com/ciphers/classical-era/autokey/"

    ##########################################################################
    # GET PSEUDOCODE
    # Returns the pseudocode as a string to be used by the caller
    ##########################################################################
    def get_pseudocode(self):
        # TODO: This function should return your psuedocode, neatly formatted

        # The encrypt pseudocode
        pc = "encrypt(plainText, password)\n" \
             "   FOR character in plainText\n" \
             "      cipher_ASCII = plain_ASCII + Pass_ASCII\n" \
             "      Cipherchar = get_char(cipher_ASCII)\n" \
             "      cipherText += Cipherchar\n" \
             "   RETURN cipherText\n\n"

        # The decrypt pseudocode
        pc += "decrypt(cipherText, password)\n" \
             "   FOR character in cipherText\n" \
             "      plain_ASCII = ASCII_total + cipher_ASCII - Pass_ASCII\n" \
             "      PlainChar = get_char(plain_ASCII)\n" \
             "      plainText += Cipherchar\n" \
             "   RETURN plainText\n\n"

        return pc

    ##########################################################################
    # ENCRYPT
    # TODO: ADD description
    ##########################################################################
    def encrypt(self, plaintext, password):
        for character in plaintext:
            if character > password.length():
                pa
        plaintext
        # TODO - Add your code here
        ciphertext = str
        return ciphertext

    ##########################################################################
    # DECRYPT
    # TODO: ADD description
    ##########################################################################
    def decrypt(self, ciphertext, password):
        plaintext = ciphertext
        # TODO - Add your code here
        return plaintext