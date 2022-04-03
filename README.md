Symmetric Encryption Algorithm.

# This program reads the content of a file (e.g. txt), encrypts its content using a user chosen key (range 0 to 10000)

# How the encryption
# 1. Plain text is spread in a matrix with 7 columns.
# 2. Rows with incomplete columns are padded with $$
# 3. Unicode value of each character is added to the secret key to generate a resulting value.
# 4. Each result in a row is added to the total size of rows of the matrix
# 5. The value is used to find the associating unicode value from the Unicode table (cipher text)

# How the decrytion works
# 1. The cipher text is spread in the same matrix as used in the encryption
# 2. The size of the matrix rows is subtracted from the unicode value of each cipher character in the row
# 3. The symmetric key is subtracted from resulting value from 2.
# 4. The output of column is used to find the values from th unicode table, which is the plaintext.

# Pitfalls of this symmetric encryption
# The unicode version 14.0 table has a size of 144, 697 characters. Finding an associate character over the 144, 697th
# character may result in an unknown or unprintable characters. An alternative to solving this issue will be to initiate a
# wrap around the last character to prevent an overflow.


