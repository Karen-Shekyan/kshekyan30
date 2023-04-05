;Team Phantom Tollbooth :: Karen Shekyan
;SoftDev pd8
;K27 -- Basic functions in JavaScript
;2023-04-04

;Scheme Antecedents for JS work

;factorial:
(define fact (lambda (x)
	(if (< x 2)
		1
		(* x (fact(- x 1)))
	)
))

(fact 1) ;"...should be  1"
(fact 2) ;"...should be  2"
(fact 3) ;"...should be  6"
(fact 4) ;"...should be  24"
(fact 5) ;"...should be  120"


;fib:
(define fib (lambda (x)
	(if (< x 2)
		x
		(+ (fib(- x 1)) (fib(- x 2)))
	)
))

(fib 0) ;"...should be  0"
(fib 1) ;"...should be  1"
(fib 2) ;"...should be  1"
(fib 3) ;"...should be  2"
(fib 4) ;"...should be  3"
;=================================================================

