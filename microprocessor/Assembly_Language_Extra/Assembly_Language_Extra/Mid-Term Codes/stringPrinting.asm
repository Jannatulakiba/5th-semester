.MODEL SMALL
.STACK 100H

.DATA

MSG DB "...d$"

.CODE 

MAIN PROC 
   
    ;Primary Accumulator Register
    MOV AX , @DATA
    MOV DS , AX  
     
    ;Printing String
        MOV AH, 9
        LEA DX, MSG
        INT 21H   
    
    MOV AH, 4CH
    INT 21H   
    MAIN ENDP 
END MAIN