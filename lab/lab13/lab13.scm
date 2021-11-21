; Q1
(define (compose-all funcs)
    (if (null? funcs)
    (lambda (x) x)
    (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
)
 
(define identity (compose-all (list)))
(define (halve x) (/ x 2))
(define (square x) (* x x))
(define halve-then-square (compose-all (list halve square)))
(define square-then-halve (compose-all (list square halve)))


; Q2
(define (tail-replicate x n)
    (define (helper x n current)
        (if (eq? n 0) current
            (helper x (- n 1) (cons x current))))

    (helper x n nil)
)