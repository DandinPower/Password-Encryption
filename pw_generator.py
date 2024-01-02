from argparse import ArgumentParser

def generate_password(length, special, number):
    """Generate a password of given length.

    Args:
        length (int): Length of password.
        special (bool): Include special characters.
        number (bool): Include numbers.

    Returns:
        str: Password.
    """
    import string
    from random import choice

    if special and number:
        chars = string.ascii_letters + string.digits + string.punctuation
    elif special:
        chars = string.ascii_letters + string.punctuation
    elif number:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters

    password = ""
    for _ in range(length):
        password += choice(chars)
        
    return password

def generate_password_by_vocabulary(vocab_nums: int, vocab_path: str, random_case: int) -> str:
    """Generate a password by selecting words from a vocabulary.
    
    Args:
        vocab_nums (int): Number of words to select.
        vocab_path (str): Path to vocabulary file.
        random_case (int): Randomly change the case of the words. 0: no change, 1: random, 2: all lower, 3: all upper.

    Returns:
        str: Password.
    """
    from random import choice, randint

    with open(vocab_path, "r") as f:
        vocab = f.read().splitlines()
    
    assert vocab_nums <= len(vocab), "Number of words to select must be less than or equal to the number of words in the vocabulary."

    password = ""
    for _ in range(vocab_nums):
        word = choice(vocab)
        vocab.remove(word)
        if random_case == 1:
            word = word.capitalize() if randint(0, 1) else word
        elif random_case == 2:
            word = word.lower()
        elif random_case == 3:
            word = word.upper()
        password += word

    return password


def main():
    parser = ArgumentParser(description="Generate a password")
    # parser.add_argument("--l", type=int, default=10, help="Length of password")
    # parser.add_argument("--s", type=int, default=1, help="Include special characters")
    # parser.add_argument("--n", type=int, default=1, help="Include numbers")
    parser.add_argument("--vocab_nums", type=int, help="Number of words to select")
    parser.add_argument("--vocab_path", type=str, help="Path to vocabulary file")
    parser.add_argument("--random_case", type=int, default=0, help="Randomly change the case of the words. 0: no change, 1: random, 2: all lower, 3: all upper")
    
    args = parser.parse_args()
    # password = generate_password(args.l, args.s, args.n)
    password = generate_password_by_vocabulary(args.vocab_nums, args.vocab_path, args.random_case)
    print(password)

if __name__ == "__main__":
    main()