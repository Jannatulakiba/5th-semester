.MODEL SMALL
.STACK 100H

.DATA

var1 DB 12

.CODE 
          
          
MAIN PROC 
    
    ;mov ebx, var1
    ;add eax, ebx
    ;But add can access one variable 
    
    mov AH,1
    add AH, var1  
    
    ;Printing 
    ;Primary Accumulator Register
    MOV AX , @DATA
    MOV DS , AX
    LEA DX, var1
    INT 21H 
    
    MOV AH, 4CH
    INT 21H   
    MAIN ENDP 
END MAIN