from core.parser import Parser
from core.tokenizer import Tokenizer
# =============================================================================
# Main Function
# =============================================================================
def main():
    """
    Main function to run the parser.
    """
    # Example C-like code
    code = """
    int main() {
        int x = 10;
        float y = 20.5;
        x = x + 1;
        y = y * 2.0;
        if (x > 5) {
            return x;
        } else {
            return y;
        }
        while (x < 15) {
            x = x + 1;
        }
        return 0;
    }
    """

    code_1 = """
    int nums = 5;
    string hello = "hello, world!";
    
    """

    # Tokenize the code
    tokenizer = Tokenizer(code_1)
    tokens = tokenizer.tokenize()
    print("Tokens:")
    for token in tokens:
        print(token)

    # Parse the tokens into an AST
    parser = Parser(tokens)
    ast_root = parser.parse()
    print("\nAbstract Syntax Tree (AST):")
    print(ast_root)  # Print the AST

if __name__ == "__main__":
    main()
    