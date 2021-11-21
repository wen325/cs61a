; Q4
(define (rle s)
  ;'YOUR-CODE-HERE
  (define (helper s prev count)
      (if (null? s) (cons-stream (list prev count) nil)
          (if (= prev (car s))
              (helper (cdr-stream s) prev (+ count 1))
              (cons-stream (list prev count) (helper (cdr-stream s) (car s) 1))
          )
      )
    
  )
  
  (if (null? s) nil
    (helper (cdr-stream s) (car s) 1)
  )
)

(define s (cons-stream 1 (cons-stream 1 (cons-stream 2 nil))))

; Q4 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q5
(define (insert n s)
  ;'YOUR-CODE-HERE
  (define (helper n prev last)
        (if (null? last) (append prev (list n))
          (if (< n (car last)) (append prev (list n) last)
            (helper n (append prev (list (car last))) (cdr last))
          )        
        )
  )
  (if (< n (car s)) (append (list n) s)
      (helper n (list (car s)) (cdr s)))
)

(define (tail-list n so-far)
   (if (= n 0)
       so-far
       (tail-list (- n 1) (cons 1 so-far))))

(define big-list (tail-list 500 '()))

(define result (insert 4 big-list)) ; Test for tail recursion


; Q6
(define (deep-map fn s)
  ;'YOUR-CODE-HERE
    (define (helper fn s lst)

  (if (null? s)
      lst
      (if (list? (car s)) (helper fn (cdr s) (append lst (list (deep-map fn (car s)))))
          (helper fn (cdr s) (append lst (list (fn (car s)))))))
  )    

  (if (null? s) nil
      (helper fn s nil))
)


; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  ;'YOUR-CODE-HERE
  (define (helper unique_name last_name s)
      (if (null? s) unique_name
        (if (among unique_name (car s)) (helper unique_name last_name (cdr s))
            (helper (append unique_name (list (car s))) (car s) (cdr s))
        )
      )
  )      

  (define (among unique_name new_name)
      (if (null? unique_name) #f
          (if (eq? (car unique_name) new_name) #t
              (among (cdr unique_name) new_name))
      )
  )

  (if (null? s) nil
      (helper (list (car s)) (car s) (cdr s)))
)

(define (count name s)
  ;'YOUR-CODE-HERE
  (if (null? s) 0
      (if (eq? name (car s))
          (+ 1 (count name (cdr s)))
          (+ 0 (count name (cdr s)))
      )
  )
)

(define (tally names)
  ;'YOUR-CODE-HERE

  (define (helper unique_name names lst)
        (if (null? unique_name) lst
            (helper (cdr unique_name) names 
            (append lst (list (cons (car unique_name) (count (car unique_name) names))))
            )))
  (if (null? names) nil
      (helper (unique names) names nil)
  )
)


(define a '(james jen jemin john))
(define b '(billy billy bob billy bob billy bob))