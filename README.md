# 🔐 Data Encryption and Decryption Tool

## Project Overview
The Data Encryption and Decryption Tool is a Python-based application designed to encrypt and decrypt text messages and files using modern cryptographic algorithms.

## Objectives
- Protect sensitive data using encryption.
- Implement AES and RSA cryptographic algorithms.
- Provide encryption and decryption functionality.
- Understand the security and performance differences between algorithms.

## Features
- Text encryption and decryption
- File encryption and decryption
- AES-256-GCM symmetric encryption
- RSA-2048 asymmetric encryption
- Password-based key derivation using PBKDF2
- Simple and user-friendly Streamlit interface

## Technologies Used
- Python
- Streamlit
- AES-256-GCM
- RSA-2048
- PBKDF2-HMAC-SHA256

## Project Structure
```text
DataEncryptionTool/
├── app.py
├── aes_crypto.py
├── rsa_crypto.py
├── file_crypto.py
├── requirements.txt
└── README.md
```

*Note: Update the file structure to match the actual files in your repository.*

## Installation and Usage

1. Clone the repository:
   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Open the project folder:
   ```bash
   cd DataEncryptionTool
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in your terminal.

## Learning Outcomes
- Understanding encryption and decryption.
- Learning symmetric and asymmetric cryptography.
- Understanding data confidentiality and integrity.
- Comparing encryption performance and key management.

## Disclaimer
This project is developed for educational purposes and cybersecurity learning.

## Author
Karthik

## License
This project is intended for educational use.
