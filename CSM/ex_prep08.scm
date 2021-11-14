(define (caddaadr x)
    (car (cdr (cdr (car (car (cdr x))))))
)

;;; hard, unfinished
(define (deeval num k)
    (cond
        (eq? k 1) 1)
        (eq? k 0) 0)
        (else
            (+
                (if (eq? (modulo num k) 0
                    0
            )
            (deeval (- num k) (- k 1))
            )
        )
    )
)





(define (deep-reverse lst)
    (cond ((null? lst) nil)
          ((list? (car lst))
            (append (deep-reverse (cdr lst))
                    (list (deep-reverse (car lst)))))
          (else
            (append (deep-reverse (cdr lst)) (list (car lst))))
    )
)
