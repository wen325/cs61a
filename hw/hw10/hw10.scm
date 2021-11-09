(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (term n) (accumulate combiner start (- n 1) term))

  )
)

(define (accumulate-tail combiner start n term)
  (define (helper combiner start n term current)
      (if (= n 0) current
      (helper combiner start (- n 1) term (combiner (term n) current)))
  )
  (if (= n 0)
    start
    (helper combiner start n term start)
  )  
)

(define-macro (list-of expr for var in seq if filter-fn)
    `(map (lambda(, var), expr) (filter (lambda(,var), filter-fn),seq))
)
