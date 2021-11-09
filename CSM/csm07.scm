(define (waldo lst)
    (if (null? lst) #f
        (if (eq? (car lst) 'waldo) #t
            (waldo (cdr lst))
        )
    )
)


(define (waldo-index lst)
    (if (null? lst) #f
        (if (eq? (car lst) 'waldo) 0
            (if (number? (waldo-index (cdr lst))) (+ 1 (waldo-index (cdr lst)))
                #f)
        )
    )
    
)


(define (quicksort lst)
    (if (null? lst) nil
        (if (number? (car (lst)) (car (lst)))
                
        
        )    
    )
)