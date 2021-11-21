;;; 5.1
(define (merge s1 s2)
    (if (null? s1) s2 
        (if (null? s2) s1
            (if (< (car s1) (car s2)) (cons-stream (car s1) (merge (cdr-stream s1) s2))
                (cons-stream (car s2) (merge s1 (cdr-stream s2))))
            )
        )
)

;;; 5.2

(define (cycle start)
    (cons-stream (modulo start 5) (cycle (+ 2 start)))
)
