class ColeCipher:

    def __init__(self, content, secretkey = 200) -> None:
        self.content = content
        self.secretkey = secretkey
        self.con = 3
        self.row_cols = 7

    def process(self, plaintext):
        processed_plaintext = []

        for start in range(0, len(plaintext), self.row_cols):
            row = plaintext[start: start + self.row_cols]
            if len(row) < self.row_cols:
                row = row.ljust(self.row_cols, '$')

            val = [ord(code) for code in row]
            processed_plaintext.append(val)

        return processed_plaintext

    def encrypt(self):
        processed_values = self.process(self.content)
        cipher = ""
        # row encrypt using key
        for index, values in enumerate(processed_values):
            processed_values[index] =  [(value + self.secretkey) for value in values]

        # column encrypt using row length
        row_size = len(processed_values)
        for row in processed_values:
            cipher +=  "".join([str(chr(row[column_index] + row_size)) for column_index in range(len(row))])

        return cipher

    def decrypt(self, ciphertext):
        processed_vals = self.process(ciphertext)
        plain_text = ""

        # Column decrypt
        row_size = len(processed_vals)
        for i, c in enumerate(processed_vals):
            processed_vals[i] = [(c[i] - row_size) for i in range(len(c))]
            
        # Row decrypt
        for j in processed_vals:
            plain_text += "".join([str(chr(q - self.secretkey)) for q in j])

        return plain_text