(define (replicate x n)
    (if (= n 0) nil
        (cons x (replicate x (- n 1)))))


(define-macro (repeat-n expr n)
      (cons 'begin (replicate expr (eval n)))
)


(define-macro (or-macro expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1 ,expr2)))





;;; part 2

(define (has-even? s)
    (cond ((null? s) #f)
        ((even? (car s)) #t)
        (else (has-even? (cdr-stream s)))))

(define (naturals n)
    (cons-stream n (naturals (+ n 1))))

(define nat (naturals 0))

;;; 2.2

(define (range-stream start end)
    (if (eq? (- end start) 0)
        nil
        (cons-stream start (range-stream (+ 1 start) end)))
)

;;; 2.3

(define (slice s start end)
    (if (> start 0) (slice (cdr-stream s) (- start 1) (- end 1))
        (if (eq? end 0) nil
            (cons (car s) (slice (cdr-stream s) start (- end 1))))
    )
)

;;; 2.4

(define (combine-with f xs ys)
    (if (or (null? xs) (null? ys))
        nil
        (cons-stream
            (f (car xs) (car ys))
            (combine-with f (cdr-stream xs) (cdr-stream ys)))))

(define evens (combine-with + (naturals 0) (naturals 0)))

(define factorials 
    (cons-stream 1 (combine-with * factorials (naturals 1)))
)

(define fibs
    (cons-stream 0 
        (cons-stream 1 
            (combine-with + fibs (cdr-stream fibs))))
)


(define (exp x)
    (let ((terms (combine-with (lambda (a b) (/ (expt x a) b))
                    (cdr-stream (naturals 0))
                    (cdr-stream factorials))))
    (cons-stream 1 (combine-with + terms (exp x)))))
