from core.parser import Parser
from core.tokenizer import Tokenizer
# =============================================================================
# Main Function
# =============================================================================

def parse_code(code: str):
    tokenizer = Tokenizer(code)
    tokens = tokenizer.tokenize()
    # print("Tokens:")
    # # for token in tokens:
    # #     print(token)

    parser = Parser(tokens)
    ast_root = parser.parse()
    print("\nAbstract Syntax Tree (AST):")
    ast_root.pretty_print()
    
def main():
    """
    Main function to run the parser.
    """

    declare_code = """
    int nums = 5;
    string hello = "hello, world!";
    float fl = 3.14;
    """

    for_code = """
    for (int i = 0; i < 10; i = i + 1) {
        for (int j = 0; j < 10; j = j + 1) {
            int x = i + j * 2;
        }
    }

    """

    if_code = """
    int x = 10;
    int y;
    if (x > 5) {
        y = x + 5;
    } else {
        y = x - 5;
    }
    """

    arithmetic_code = """

    int x = 10;
    int y= 10;

    int sum = x + y;
    int diff = x - y;
    int prod = x * y;
    int quot = x / y; 
    """

    while_code = """
    int x = 5;
    int y = 0;
    while (x > 0) {
        y = y + 1;
    }
    """

    parse_code(declare_code)
    parse_code(arithmetic_code)
    parse_code(if_code)
    parse_code(for_code)
    parse_code(while_code)

if __name__ == "__main__":
    main()



