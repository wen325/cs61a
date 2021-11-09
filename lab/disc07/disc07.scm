;;; # 4.1

(define (factorial x)
    (if (= x 1) 1
        (* x (factorial (- x 1))
        )
    )    
)


;;; # 4.2

(define (fib n)
    (if (or (= n 0) (= n 1))
        n
        (+ (fib (- n 1)) (fib (- n 2)))        
    )
)


(define (len a)
     (if (null? a)
     0
     (+1 (len (cdr a)))))

;;; # 5.1

(define (concat a b)
    (if (null? (cdr a)) (cons (car a) b)
        (cons (car a) (concat (cdr a) b)
        )    
    )
)

;;; # 5.2
(define (replicate x n)
    (if (= n 1) (list x)
        (cons x (replicate x (- n 1)))
    )
)

;;; # 5.3
(define (uncompress s)
    (if (null? s) nil
        (concat (replicate (car (car s)) (car (cdr (car s)))) (uncompress (cdr s)))
    )    
)

;;; # 5.4
(define (map fn lst)
    (if (null? lst) nil
        (cons (fn (car lst)) (map fn (cdr lst)))
    )
)


;;; # 5.5

(define (deep-map fn lst)
    (if (null? lst) nil
        (if (list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst)))
            (cons (fn (car lst)) (deep-map fn (cdr lst)))        
        )    
    )
)

;;; # 6.1

(define (make-tree label branches)
    (cons label branches)
)

(define (label tree)
    (if (null? tree) nil
        tree
    )
)

(define (branches tree))
    (if (null? branches) nil
        list tree
)

;;; # 6.2 unfinished

(define (tree-sum tree)



)


;;; # 6.3 unfinished