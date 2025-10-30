# Calculator - Mathematical Expression Evaluator

A Python-based calculator that evaluates arithmetic expressions with support for operator precedence and parentheses.

## Features

- ✅ **Basic arithmetic operations**: `+`, `-`, `*`, `/`
- ✅ **Parentheses support**: Use `()` to control operation order
- ✅ **Operator precedence**: Follows standard mathematical rules (PEMDAS)
- ✅ **Interactive mode**: Continuous input/output loop
- ✅ **Error handling**: Comprehensive exception handling for invalid expressions
- ✅ **Custom implementation**: Built from scratch without using `eval()` or external libraries

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download the `calculator.py` file
2. Ensure you have Python 3 installed on your system

```bash
python --version  # Should show Python 3.x
```

## Usage

### Running the Calculator

```bash
python calculator.py
```

### Interactive Mode

Once started, the calculator enters an interactive loop where you can type expressions:

```
> 2 + 3
5.0
> 10 * (5 + 3)
80.0
> 2 + 3 * 4
14.0
> (2 + 3) * 4
20.0
> 100 / (20 - 10)
10.0
> quit
```

Type `quit` to exit the program.

### Using in Your Code

You can also import and use the Calculator class in your own Python code:

```python
from calculator import Calculator, CalculatorException

calc = Calculator()

try:
    result = calc.eval("2 + 3 * 4")
    print(result)  # Output: 14.0
except CalculatorException as e:
    print(f"Error: {e}")
```

## Supported Operations

| Operator | Description | Example | Result |
|----------|-------------|---------|--------|
| `+` | Addition | `5 + 3` | `8.0` |
| `-` | Subtraction | `10 - 4` | `6.0` |
| `*` | Multiplication | `6 * 7` | `42.0` |
| `/` | Division | `20 / 4` | `5.0` |
| `()` | Parentheses | `(2 + 3) * 4` | `20.0` |

## Operator Precedence

The calculator follows standard mathematical operator precedence:

1. **Parentheses** `()` - highest priority
2. **Multiplication and Division** `*`, `/` - evaluated left to right
3. **Addition and Subtraction** `+`, `-` - evaluated left to right

### Examples

```
2 + 3 * 4       → 2 + (3 * 4) = 14
(2 + 3) * 4     → (5) * 4 = 20
10 / 2 + 3      → (10 / 2) + 3 = 8
10 / (2 + 3)    → 10 / (5) = 2
```

## Error Handling

The calculator throws `CalculatorException` for invalid expressions:

### Common Errors

| Error | Example | Description |
|-------|---------|-------------|
| Empty expression | ` ` | No input provided |
| Invalid character | `2 + @` | Unsupported character in expression |
| Mismatched parentheses | `(2 + 3` | Opening parenthesis without closing |
| Division by zero | `10 / 0` | Attempting to divide by zero |
| Invalid expression | `+ + 2` | Malformed expression |

### Error Example

```
> 2 + (3 * 4
Eroare: Paranteze nepotrivite în expresie

> 10 / 0
Eroare: Împărțire la zero

> 2 @ 3
Eroare: Caracter invalid în expresie: '@'
```

## Implementation Details

### Algorithm

The calculator uses a two-step process to evaluate expressions:

1. **Shunting Yard Algorithm**: Converts infix notation (standard mathematical notation) to Reverse Polish Notation (RPN)
2. **Stack-based Evaluation**: Evaluates the RPN expression using a stack

### Example Evaluation Process

For the expression `2 + 3 * 4`:

```
Step 1: Tokenization
Input: "2 + 3 * 4"
Tokens: ['2', '+', '3', '*', '4']

Step 2: Convert to RPN
Infix: 2 + 3 * 4
RPN: 2 3 4 * +

Step 3: Evaluate RPN
2     → Stack: [2]
3     → Stack: [2, 3]
4     → Stack: [2, 3, 4]
*     → Pop 4, 3; Push 3*4=12 → Stack: [2, 12]
+     → Pop 12, 2; Push 2+12=14 → Stack: [14]

Result: 14.0
```

## Class Structure

### `CalculatorException`
Custom exception class for calculator errors.

### `Calculator`
Main calculator class with the following methods:

- **`__init__()`**: Initializes the calculator with operator definitions
- **`read()`**: Reads input from stdin
- **`eval(string)`**: Evaluates an arithmetic expression and returns the result
- **`loop()`**: Interactive loop for continuous expression evaluation
- **`_tokenizeaza(expresie)`**: Private method to tokenize expressions
- **`_conversie_rpn(tokens)`**: Private method to convert to RPN
- **`_evalueaza_rpn(rpn)`**: Private method to evaluate RPN expressions

## Testing

You can test the calculator with various expressions:

```python
test_expressions = [
    "2 + 3",                    # Simple addition
    "10 - 5",                   # Subtraction
    "4 * 5",                    # Multiplication
    "20 / 4",                   # Division
    "2 + 3 * 4",                # Precedence test
    "(2 + 3) * 4",              # Parentheses test
    "10 / (2 + 3)",             # Complex parentheses
    "((2 + 3) * 4 - 5) / 3",    # Nested operations
    "-5 + 3",                   # Negative numbers
]
```

## Limitations

- Only supports basic arithmetic operations (`+`, `-`, `*`, `/`)
- No support for exponentiation, modulo, or other advanced operations
- No support for variables or functions
- Whitespace is allowed but not required between tokens

## License

This project is provided as-is for educational purposes.

## Author

Created as an assignment implementation for expression evaluation without using built-in `eval()` functions.

## Contributing

Feel free to extend the calculator with additional features such as:
- More operators (exponentiation, modulo, etc.)
- Scientific functions (sin, cos, sqrt, etc.)
- Variable support
- Memory functions
- Expression history
