;;; part 1
;;; 1

(define (non-contiguous subseq lst)
    (cond ((null? subseq) #t)
          ((null? lst) #f)
          ((eq? (car subseq) (car lst)) (non-contiguous (cdr subseq) (cdr lst)))            
          (else (non-contiguous subseq (cdr lst)))))


(define (assert-equals expected expression)
    (if (eq? (eval expression) expected)
        'OK
        (cons 'expected (cons expected (cons 'but (cons 'got (cons (eval expression) nil)))))))


;;;(define expected #t)
;;;(define expression '(non-contiguous '(1 3 6) '(1 2 3 4 5 6)))

;;; 2

(define (directions n sym)
    (define (search s exp)
    ; Search an expression s for n and return an expression based on exp.
    (cond ((number? s) (if (= s n) exp nil))
        ((null? s) nil)
        (else (search-list s exp))))

    (define (search-list s exp)
    ; Search a nested list s for n and return an expression based on exp.
        (let ((first (search (car s) (list 'car exp)))
              (rest  (search (cdr s) (list 'cdr exp))))
                (if (null? first) rest first)))
    (search (eval sym) sym))

;;; 3

(define (if-when day left)
    (if (= (- day left) 0) (print 'im-free)
        (print 'jk-final)))

;;; part 2

; Repeat n Cycle

(define (cycle lst n)
    (define s (cons-stream (car lst)) (helper (cdr lst) n)))
    (define (helper buffer num)
        (cond ((= n 0) s)
              ((null? buffer) (helper lst (- n 1)))
              (else (cons-stream (car buffer) (helper (cdr buffer) n)))))
    s
)

; Stream first n

(define (stream-first-n n lst)
    (define (stream-helper i curr-lst)
        (if (null? curr-lst) nil
            (if (= i 0) curr-lst
                (cons-stream (car curr-lst) (stream-helper (- i 1) (cdr curr-lst))))
    ))
(stream-helper n lst))


;; official solution?
(define (stream-first-n n lst)
    (define (stream-helper i curr-lst)
        (if (or (zero? i) (null? curr-lst))
        (stream-first-n n lst)
        (cons-stream (car curr-lst) (stream-helper (- i 1) (cdr curr-lst)))
    ))
    (stream-helper n lst)
)
