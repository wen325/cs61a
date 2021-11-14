(define (count-instance lst x)
    (cond ((null? lst) 0)
          ((equal? (car lst) x) (+ 1 (count-instance (cdr lst) x)))
    (else (count-instance (cdr lst) x)))
)



;;; part 1 q4
(define (count-tail lst x)
    (define (helper lst x count)
        (if (null? lst) count
            (if (equal? (car lst) x) (helper (cdr lst) x (+ 1 count))
            (helper (cdr lst) x count)))
    )
    (helper lst x 0)
    
)

;;; part 1 q5

(define (filter f lst)
    (define helper f lst new_lst)
        (if (null? lst) new_lst
            (if (f (car lst)) (helper f (cdr lst) (append new_lst (car lst)))
                (helper f (cdr lst) new_lst)) 
        )
    )
    (helper f lst nil)
)