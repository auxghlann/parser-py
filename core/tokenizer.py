import re
from typing import List, Tuple, Optional

# =============================================================================
# Tokenizer Class
# =============================================================================
class Tokenizer:
    """
    The Tokenizer class is responsible for breaking down the input text into a
    stream of tokens. Each token represents a meaningful unit in the language,
    such as keywords, identifiers, operators, and literals.
    """
    def __init__(self, text: str):
        """
        Initializes the Tokenizer with the input text.

        Args:
            text (str): The text to be tokenized.
        """
        self.text = text
        self.cursor = 0
        self.tokens: List[Tuple[str, str]] = []  # List of (token_type, token_value)

    def get_next_token(self) -> Optional[Tuple[str, str]]:
        """
        Extracts the next token from the input text.

        This method uses regular expressions to identify different token types
        and their corresponding values.  It skips whitespace and raises an
        error if an unexpected character is encountered.

        Returns:
            Optional[Tuple[str, str]]: A tuple containing the token type and
            value, or None if the end of the input is reached.
        """
        if self.cursor >= len(self.text):
            return None  # End of input

        # Define token patterns using regular expressions.
        patterns = [
            ('KEYWORD', r'\b(if|else|while|for|int|float|string|void|return)\b'),
            ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            ('FLOAT', r'\b\d+\.\d+\b'),
            ('INTEGER', r'\b\d+\b'),
            ('OPERATOR', r'(\|\||&&|==|!=|<=|>=|[+\-*/=<>!;(){},\[\]])'),  
            ('WHITESPACE', r'\s+'),  
            ('STRING', r'"[^"]*"'),  
        ]

        # Iterate through the patterns to find a match at the current position.
        for token_type, pattern in patterns:
            regex = re.compile(pattern)
            match = regex.match(self.text, self.cursor)
            if match:
                value = match.group(0)  # Extract the matched text
                self.cursor = match.end()  # Advance the cursor
                if token_type != 'WHITESPACE':  # Discard whitespace
                    return (token_type, value)
                else:
                    return self.get_next_token() # continue to get next token
        # If no pattern matches, raise an error for an unexpected character.
            ## Include the current cursor position in the error message.
        raise ValueError(f"Unexpected character '{self.text[self.cursor]}' at position {self.cursor}")

    def tokenize(self) -> List[Tuple[str, str]]:
        """
        Tokenizes the entire input text.

        Repeatedly calls get_next_token() until the end of the input is reached,
        collecting all the tokens into a list.

        Returns:
            List[Tuple[str, str]]: A list of (token_type, token_value) tuples.
        """
        while True:
            token = self.get_next_token()
            if token is None:
                break  # Exit loop at end of input
            self.tokens.append(token)
        return self.tokens