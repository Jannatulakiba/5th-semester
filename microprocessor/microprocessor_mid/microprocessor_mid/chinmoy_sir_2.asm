org 100h

MOV AX, 0Eh        ; X = 14
MOV BX, 0Eh
MUL BX             ; AX = X^2
MOV [2008], AX     ; save X^2 = 196

MOV BX, 3
MUL BX             ; AX = 3X^2 = 588
MOV [2002], AX

MOV AX, 0Eh
MOV BX, 2
MUL BX             ; AX = 2*X = 28
MOV BX, AX
ADD BX, [2002]     ; BX = 588 + 28 = 616
SUB BX, 5          ; BX = 611 ? (3X^2 + 2X - 5)

MOV AX, [2008]     ; AX = 196
MOV DX, 2
MUL DX             ; AX = 392
SUB AX, 1          ; AX = 391 ? (2X^2 - 1)
MOV DX, AX         ; DX = 391
MOV AX, BX         ; AX = 611
MOV BX, DX         ; BX = 391
XOR DX, DX         ; DX = 0 (clear high word before DIV)

DIV BX             ; AX = Quotient, DX = Remainder

MOV [2010], AX     ; Store Quotient (word)
MOV [2012], DX     ; Store Remainder (word)

RET
