# Password Manager

This is a password manager program that allows you to encrypt and decrypt your passwords using the AES encryption algorithm.

## Requirements

- Python 3.6 or higher
- Python packages: `pycryptodomex`, `pycryptodomex`, `python-dotenv`

## Installation

1. Clone the repository:

```shell
git clone https://github.com/DandinPower/Password-Encryption.git
```

2. Install the required Python packages:

```shell
pip install -r requirements.txt
```

## Usage

To run the program, execute the following command:

```shell
python main.py <operation> <password> <input_file> <output_file>
```

- `<operation>`: Specify the operation to perform. Use `-e` to encrypt a CSV file or `-d` to decrypt a binary file. Use `get_salt` to generate a new salt.
- `<password>`: The password to use for encryption or decryption.
- `<input_file>`: The path to the input file (CSV file for encryption or binary file for decryption).
- `<output_file>`: The path to the output file (binary file for encryption or CSV file for decryption).

For example, to encrypt a CSV file:

```shell
python main.py -e mypassword input.csv encrypted.bin
```

To decrypt a binary file:

```shell
python main.py -d mypassword encrypted.bin output.csv
```

To generate a new salt and add it to the .env file:

```shell
python main.py get_salt
```

**Note**: After generating a new salt, add it to the .env file as the value for the `SALT` variable. Please make sure to replace `<new_salt_value>` with the actual generated salt value obtained from running `python main.py get_salt`.

## .env Configuration

To use the program, create a `.env` file in the project directory and add the following configuration:

```
SALT=<new_salt_value>
```

Replace `<new_salt_value>` with the generated salt value obtained from running `python main.py get_salt`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions, feel free to open an issue or submit a pull request.

## Acknowledgements

This project was inspired by the need for a secure password management solution.

## Contact

For any questions or inquiries, please contact [tomhot246@gmail.com](mailto:tomhot246@gmail.com).