# PSSC: Polyalphabetic Substitution Stream Cipher with Payload Obfuscation

PSSC is a custom, from-scratch implementation of a symmetric stream cipher built in Python. The project demonstrates core engineering concepts in data serialization, modular arithmetic cryptography, and transport payload obfuscation without relying on third-party cryptographic libraries.

## 🚀 Architectural Overview

PSSC applies a dynamic, variable-shift substitution mechanism over an 82-character alphanumeric and symbol space. 

Unlike traditional static ciphers, **Version 2** implements a pseudo-One-Time Pad (OTP) architecture where every character in the plaintext string is shifted by an independent, randomly generated key digit, neutralizing standard monoalphabetic frequency analysis attacks.

### Mathematical Mechanism
For each character index $i$ in the payload, the ciphertext index $C_i$ is computed using modular arithmetic:

$$C_i = (P_i + K_i) \pmod M$$

Where:
* $P_i$ = Index of the plaintext character within the target alphabet array.
* $K_i$ = The single-digit integer key value corresponding to the $i$-th index of the dynamically generated Initialization Vector (IV).
* $M$ = Total length of the character space array ($M = 82$).

---

## 🛠️ Codebase Architecture

The repository contains two iterations of the cipher, showcasing architectural evolution:

### 1. Version 1: Dynamic Key-Space Expansion
* **Mechanism:** Generates a high-entropy integer as an Initialization Vector (IV) and expands the underlying key space by concatenating the base alphabet array proportionally to the size of the IV.
* **Payload Packaging:** The configuration metadata needed for decryption—including the randomized position index (`pos`), the scale multiplier (`rand`), and the raw `IV`—are procedurally sliced and injected directly into the final ciphertext string.

### 2. Version 2: Polyalphabetic Digits Shift (Stream Hybrid)
* **Mechanism:** Eliminates key-space duplication in favor of a direct character-to-digit shift array. It scales an IV integer precisely to the length of the string, ensuring every plaintext character gets a unique shift vector based on a Vigenère-style matrix model.
* **Key Protection:** Obfuscates the transmitted IV value within the payload by applying a pre-shared 4-digit PIN offset before string concatenation.

---

## 🔒 Cryptanalysis & Security Assessment (Self-Evaluation)

While PSSC effectively demonstrates symmetric stream cipher logic, it is an educational proof-of-concept and possesses specific structural vulnerabilities that make it unsuitable for production environments:

1. **Entropy Constraints on Shifting:** Because the IV array in Version 2 uses base-10 digits ($0-9$) to shift characters within an 82-character space, the maximum shift window is confined to $\approx 11\%$ of the total character space per mutation loop.
2. **Key Transmission inside Payload:** Both versions package the key material (or a direct derivative of it) within the ciphertext string itself via predictable string-slicing markers. An attacker who uncovers the slicing boundaries can easily extract the IV.
3. **PIN Brute-Forcing:** The 4-digit symmetric PIN tracking mechanism in Version 2 provides a narrow search space ($10^4$ combinations), making it trivially vulnerable to computational brute-force exhaustion.

---

## 💻 How To Run

Ensure you have Python 3.x installed. Clone the repository and execute either version directly:

```bash
# Run Version 2 Stream Hybrid
python version2.py
