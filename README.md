# Crypto1 Project


## First: Vernam-Cipher
### Introduction

Vernam Cipher is one of the Substitution techniques used for converting plain text into cipher text. It combines plaintext (the original message) with the random alphabetic characters (key) to give the ciphertext using an “exclusive or” (XOR) function. So, we should have a key to encrypt the plain text whose length must be equal to the length of the plain text.


### Vernam Cipher Steps

1. Assign a number to each character of the plain-text and the key according to alphabetical order.alphabetic-order-table

2. Convert each of these numbers to binary numbers (5-digits).

3. Bitwise XOR both the number (Corresponding plain-text character number and Key character number).
In mathematics, the XOR operation is known as modulo-2 addition. In our case, the individual bits of the plaintext are XOR-ed with the individual bits of the key. The resulting bit will only be '1' if the two input bits are different. If they are equal (both 1 or both 0), the result will be 0

4. If the result number of XOR operation was greater than or equal to 26, then subtract the number from 26, if it isn’t then leave it.

5. Now Convert the numbers to alphabetic to get the ciphertext.

6. To Decrypt the cipher-text, apply XOR operation on the cipher-text using the same key as the encryption steps.


### Security of Vernam Cipher

To encrypt your message as much as secure, you have to note that:
The characters in the key must be truly random.
There must be only two copies of the key (held by the sender and recipient) and the key must be secret to these parties.

Now, the vernam cipher is considered to be secure. This is also because each character is encrypted using its own key.
Most codebreakers exploit human weakness to crack ciphers. So, key exchange is a significant problem and could be exploited to get the key. That could happen when the sender and receiver live in completely different places, such as on opposite sides of the world.



## Second: Hill-Cipher (2x2 matrix)
### Introduction

Hill cipher is a polygraphic substitution cipher based on linear algebra. It used matrices and matrix multiplication to mix up the plaintext.
Each letter of plaintext is represented by a number modulo 26, like A = 0, B = 1, …, Z = 25.
To encrypt a message, each block of n letters (considered as an n-component vector) is multiplied by an invertible n × n matrix, against modulus 26. To decrypt the message, each block is multiplied by the inverse of the matrix used for encryption.
The matrix used for encryption is the cipher key, and it should be chosen randomly from the set of invertible n × n matrices (modulo 26).


### Hill Cipher Steps

See an example here : https://intellipaat.com/blog/what-is-hill-cipher/?US#no3


### Security of Hill Cipher

When dealing with 2×2 matrices, Hill Cipher is easily solvable. But when it comes to modern cryptography solutions that have 256 combinations of numbers, Hill Cipher has a proven vulnerability when it comes to dealing with known-plaintext attacks due to its linear dependency. Any system having linear ciphertext pairs can easily break the Hill Cipher matrices as it follows only the standard algebraic algorithms for solutions.

Unfortunately, a higher level of matrix multiplications doesn’t do anything to add more security to the system. It can, however, complement diffusion on mixing with non-linear operations. Modern advanced encryption methods like AES use different diffusion to add further security to their system.

Simple 2×2 Hill Cipher matrices are quite simple and decipherable, but as it expands in size, the calculations become a lot more complex, which requires an in-depth understanding of higher mathematics.
