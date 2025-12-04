.MODEL SMALL
.STACK 100H
.DATA
 VAR DW ?

.CODE

    MAIN PROC 
        ;MOV AX, @DATA
        ;MOV DS, AX
        
        MOV DL, 082
        MOV AH, 2
        INT 21H
        
        MOV DL, 079
        MOV AH, 2
        INT 21H
        
        MOV DL, 078
        MOV AH, 2
        INT 21H
        
        MOV DL, 089
        MOV AH, 2
        INT 21H
        
        
        ;RETURN 0
        MOV AH, 4CH
        INT 21H
    MAIN ENDP
END MAIN