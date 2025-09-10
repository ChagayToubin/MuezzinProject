import base64


class Decryption:
    @staticmethod
    def Decryption_msg(m):
        encoded_string = m

        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')

        return decoded_string.split(',')
