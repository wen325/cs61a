;;;# 1
(define (double-naturals)
    (double-naturals-helper 1 #f)
)

(define (double-naturals-helper first go-next)
    (cons-stream first (cons-stream first (double-naturals-helper (+ first 1) (+ first 1))))
)


(define (naturals1 n)
    (cons-stream n (naturals1 (+ n 1))))

(define (naturals2 n)
    (cons-stream (* n 2) (naturals2 (+ n 1))))

;;;# 2

(define stream1 (naturals1 0))
(define stream2 (naturals2 0))

(define (interleave stream1 stream2)
    (cons-stream (car stream1) (interleave (cdr-stream stream2) (cdr-stream stream1)))
)

