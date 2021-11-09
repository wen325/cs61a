
;;; # 1

(define (factorial n)
(if (= n 0)
1
(* n (factorial (- n 1)) )))


;;; # 2
(define (hailstone seed n)
    (if (= n 0) seed
        (if (= (remainder (remainder seed 2) 2) 0) (hailstone (/ seed 2) (- n 1))
            (hailstone (+ (* seed 3) 1) (- n 1))
        )
        )
)

;;; # 3 (cdr (cdr a))

;;; # 4   unfinished

(define (well-formed lst)
    (if (null? lst) #t
    (if (null? (cdr lst)) #t
        (well-formed (cdr lst))        
         )
    )
)

;;; 

;;; # 5

(define (is-prefix p lst)
    (if (null? p) #t
        (if (null? lst) #f
            (if (eq? (car p) (car lst)) (is-prefix (cdr p) (cdr lst))  
                (if (null? (cdr lst)) #f
                #f)
            )        
        )
    )
)
