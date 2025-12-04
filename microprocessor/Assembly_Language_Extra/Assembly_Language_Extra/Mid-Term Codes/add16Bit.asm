.MODEL SMALL
.STACK 100H

.DATA 
 SUM DW ?
 
 
.CODE 
MAIN PROC 
    
    
    MOV AX, @DATA
    MOV DS, AX
    
    MOV AX, 0001H
    MOV BX, 0001H
    
    ADD AX, BX
    MOV SUM,AX
    
    MOV AH, 4CH
    INT 21H 
    MAIN ENDP 
END MAIN