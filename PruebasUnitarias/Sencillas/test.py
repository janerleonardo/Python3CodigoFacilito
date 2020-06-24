from algoritmo import fibonacci,palindromo,factorial

def test_fibonacci():
    assert fibonacci(5) == 5

def test_palindromo():
    assert palindromo("ana")

def test_factorial():
    assert factorial(5) == 120
