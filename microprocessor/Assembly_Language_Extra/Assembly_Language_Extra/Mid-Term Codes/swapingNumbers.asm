.MODEL SMALL
.STACK 100H

.DATA 
 A_X DW ?
 B_X DW ?
.CODE 

MAIN PROC 
    
    
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, '1'
    MOV BX, '2'
    MOV DX, AX
    MOV AX, BX
    MOV BX, DX   
    MOV A_X, AX
    MOV B_X, BX
    
    MOV AH, 4CH
    INT 21H 
    MAIN ENDP 
END MAIN