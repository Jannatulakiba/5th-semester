.MODEL SMALL
.STACK 100H

.DATA 

array DB 1,2,3

.CODE

MAIN PROC 
    
    mov AL,array           ;        eax =1
    xchg BL,[array+4]      ; 1,1,3, eax =2
    xchg CL,[array+8]      ; 1,1,2, eax =3
    MOV array,AL         ; 3,1,2, eax =1 
    
    ;Primary Accumulator Register
    ;MOV AX , @DATA
    ;MOV DS , AX
     
    ;Printing String
        MOV AH, 9
        LEA DX, array
        INT 21H  
    
    MOV AH, 4CH
    INT 21H
    MAIN ENDP
END MAIN