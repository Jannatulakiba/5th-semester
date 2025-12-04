ORG 100h

; first number = 42
MOV CH, 4    ; tens digit
MOV CL, 2    ; ones digit

; second number = 19
MOV DH, 1    ; tens digit
MOV DL, 9    ; ones digit

; ---- subtract ones ----
SUB CL, DL
JNC NO_BORROW
ADD CL, 10   ; borrow adjust
DEC CH       ; take borrow from tens
NO_BORROW:

; ---- subtract tens ----
SUB CH, DH

; ---- print result ----
; print tens
MOV AH, 2
MOV DL, CH
ADD DL, '0'
INT 21h

; print ones
MOV DL, CL
ADD DL, '0'
INT 21h

HLT
