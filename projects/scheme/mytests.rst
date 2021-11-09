This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

    >>> from scheme_reader import *

    Case Example
        >>> scheme_read(Buffer(tokenize_lines(['nil'])))
        

        >>> from scheme_reader import *
        >>> tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
        >>> src = Buffer(tokens)
        
        >>> src.current()
        '('
        >>> src.remove_front()
        '('
        >>> src.current()
        '+'
        >>> src.remove_front()
        '+'
        >>> src.remove_front()
        1
        >>> scheme_read(src)  # Returns and removes the next complete expression in src 
        