# A Parser Framework Using Python
By: Allan Khester Mesa BSCS 3_A10

## Programming Language Grammar

This documentation outlines the grammar rules supported by the parser framework. Each rule defines the structure of valid programs, statements, and expressions in the language.

---

### 1. Program
```txt
program : statement*
```
- **Description**: A program consists of zero or more statements.

### 2. Statements
```txt
statement : expression_statement
          | if_statement
          | while_statement
          | return_statement
          | declaration_statement
          | compound_statement
          | for_statement
```
- **Description**: A statement can be one of several types, including expressions, control flow constructs, or declarations.

#### 2.1 Expression Statement
```txt
expression_statement : expression ';'
```
- **Description**: An expression followed by a semicolon.
- **Example**:
  ```c
  x = x + 1;
  ```

#### 2.2 If Statement
```txt
if_statement : 'if' '(' expression ')' statement
             | 'if' '(' expression ')' statement 'else' statement
```
- **Description**: A conditional statement that executes a block of code if the condition evaluates to true. Optionally, an `else` block can be provided.
- **Example**:
  ```c
  if (x > 5) {
      int y = x + 5;
  } else {
      int y = x - 5;
  }
  ```

#### 2.3 While Statement
```txt
while_statement : 'while' '(' expression ')' statement
```
- **Description**: A loop that executes a block of code as long as the condition evaluates to true.
- **Example**:
  ```c
  while (x < 10) {
      x = x + 1;
  }
  ```

#### 2.4 For Statement
```txt
for_statement : 'for' '(' declaration_statement ';' expression ';' counter ')' statement
```
- **Description**: A loop that includes initialization, a condition, and an increment/decrement operation.
- **Example**:
  ```c
  for (int i = 0; i < 10; i = i + 1) {
      int x = i * 2;
  }
  ```

#### 2.5 Return Statement
```txt
return_statement : 'return' expression? ';'
```
- **Description**: A statement that exits a function and optionally returns a value.
- **Example**:
  ```c
  return x + y;
  ```

#### 2.6 Declaration Statement
```txt
declaration_statement : type_specifier IDENTIFIER (',' IDENTIFIER)* ( '=' expression )? ';'
```
- **Description**: Declares one or more variables of a specific type. Optionally, variables can be initialized with a value.
- **Example**:
  ```c
  int x = 10, y = 20;
  string message = "Hello, World!";
  ```

#### 2.7 Compound Statement
```txt
compound_statement : '{' statement* '}'
```
- **Description**: A block of code enclosed in curly braces. It can contain zero or more statements.
- **Example**:
  ```c
  {
      int x = 10;
      int y = x + 5;
  }
  ```

---

### 3. Type Specifier
```txt
type_specifier : 'int' | 'float' | 'void' | 'string'
```
- **Description**: Specifies the type of a variable or function.
- **Example**:
  ```c
  int x;
  float pi = 3.14;
  string name = "Alice";
  ```

---

### 4. Expressions
```txt
expression : logical_or_expression
```
- **Description**: An expression is a combination of variables, literals, and operators that evaluates to a value.

#### 4.1 Logical OR Expression
```txt
logical_or_expression : logical_and_expression ( '||' logical_and_expression )*
```
- **Description**: Evaluates to true if at least one of the operands is true.
- **Example**:
  ```c
  x > 5 || y < 10
  ```

#### 4.2 Logical AND Expression
```txt
logical_and_expression : equality_expression ( '&&' equality_expression )*
```
- **Description**: Evaluates to true if both operands are true.
- **Example**:
  ```c
  x > 5 && y < 10
  ```

#### 4.3 Equality Expression
```txt
equality_expression : relational_expression ( ('==' | '!=') relational_expression )*
```
- **Description**: Compares two values for equality or inequality.
- **Example**:
  ```c
  x == y
  x != y
  ```

#### 4.4 Relational Expression
```txt
relational_expression : additive_expression ( ('<' | '>' | '<=' | '>=') additive_expression )*
```
- **Description**: Compares two values using relational operators.
- **Example**:
  ```c
  x < y
  x >= 10
  ```

#### 4.5 Additive Expression
```txt
additive_expression : multiplicative_expression ( ('+' | '-') multiplicative_expression )*
```
- **Description**: Performs addition or subtraction.
- **Example**:
  ```c
  x + y
  x - 5
  ```

#### 4.6 Multiplicative Expression
```txt
multiplicative_expression : primary_expression ( ('*' | '/') primary_expression )*
```
- **Description**: Performs multiplication or division.
- **Example**:
  ```c
  x * y
  x / 2
  ```

#### 4.7 Primary Expression
```txt
primary_expression : IDENTIFIER | INTEGER | FLOAT | STRING | '(' expression ')' | '!' primary_expression
```
- **Description**: The most basic unit of an expression. It can be a variable, literal, or a grouped expression.
- **Example**:
  ```c
  x
  42
  "Hello"
  (x + y)
  !x
  ```

---

### Notes
- **Operator Precedence**: The grammar ensures that operators are parsed in the correct order of precedence (e.g., `*` and `/` have higher precedence than `+` and `-`).
- **Type Checking**: The parser performs type checking to ensure that operations are valid for the given types (e.g., you cannot add a string to an integer).
