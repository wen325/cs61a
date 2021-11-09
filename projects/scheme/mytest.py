from scheme_reader import *
tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
src = Buffer(tokens)
src.current()
src.remove_front()
src.current()
src.remove_front()
# src.remove_front()
# scheme_read(src)  # Returns and removes the next complete expression in src 
