(define (find s predicate)
  ;;;'YOUR-CODE-HERE   
   (if (null? s) #f
       (if (predicate (car s)) (car s)
           (find (force (cdr s)) predicate))
    )
)

(define (scale-stream s k)
  ;;;'YOUR-CODE-HERE
    (if (null? s) nil
        (cons-stream (* (car s) 2) (scale-stream (force (cdr s)) k)))
)

(define (has-cycle s)
  ;;;'YOUR-CODE-HERE
   (define (helper seen current)
        (cond ((null? current) #f)
              ((contains? seen current) #t)
              (else (helper (cons current seen) (cdr-stream current)))
        )
   )
  (helper nil s)
)

(define (contains? lst s)
        (cond ((null? lst) #f)
              ((eq? (car lst) s) #t)
              (else (contains? (cdr lst) s)))
)


(define (has-cycle-constant s)
  ;;;
      (define (helper slow fast)
              (cond ((or (null? fast) (null? (cdr-stream fast))) #f)
                    ((or (eq? fast slow) (eq? (cdr-stream fast) slow)) #t)
                    (else (helper (cdr-stream slow) (cdr-stream (cdr-stream fast))))
              )
      )
      (helper s (cdr-stream s))
)
