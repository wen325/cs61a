;;; 3.2
(define (fib n)
    (define (fib-sofar fib1 fib2 n)
        (if (= 2 n) (+ fib1 fib2)            
            (fib-sofar fib2 (+ fib1 fib2) (- n 1)))
    )

    (if (= 0 n) 0 
        (if (= 1 n) 1
            (fib-sofar 0 1 n)))
)

;;; 3.3
(define (sum lst)
    (define (tail-sum current lst)
        (if (null? (cdr lst)) (+ current (car lst))
            (tail-sum (+ current (car lst)) (cdr lst)))
        )
        
    (if (null? (cdr lst)) (car lst)
        (tail-sum (car lst) (cdr lst)))
)


;;; 3.4 not understand the problem, it seems reverse is unnecessary

(define (reverse lst)
    (define (reverse-sofar lst lst-sofar)
        (if (null? (cdr lst)) (cons (car lst) lst-sofar)
            (reverse-sofar (cdr lst) (cons (car lst) lst-sofar)))
        )
    
    (if (null? list) nil
        (reverse-sofar (cdr lst) (cons (car lst) nil)))
)

(define (append a b)

    (if (null? (cdr a)) (list (car a) (car b))
        (list (car a) (car (append (cdr a) b)))
    )
)


        
