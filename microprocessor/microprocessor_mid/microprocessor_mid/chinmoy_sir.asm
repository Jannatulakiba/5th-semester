MOV AX, 0Eh
MOV BX, 0EH

MUL BX            ; AX = X^2
MOV [2008], AX 

MOV BX, 3
MUL BX            ; AX = 3X^2
MOV [2002], AX

MOV AX, 0Eh
MOV BX, 2
MUL BX
MOV BX, AX
ADD BX, [2002]
SUB BX, 5         ; BX = 3X^2+2X-5

MOV AX, [2008]
MOV DX, 2
MUL DX            ; AX = 2X^2
SUB AX, 1
MOV DX, AX        ; DX = 2X^2-1
MOV AX, BX        ; AX = 3X^2+2X-5      

MOV BX, DX
XOR DX, DX
DIV BX