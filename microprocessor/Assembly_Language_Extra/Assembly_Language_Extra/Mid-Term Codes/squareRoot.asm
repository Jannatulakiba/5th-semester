.MODEL SMALL
.STACK 100H
.DATA
 VAR DW ?

.CODE

    MAIN PROC 
        MOV AX, @DATA
        MOV DS, AX
        
        MOV AX, 00019H
        MOV CX, 00000H
        MOV BX, 0FFFFH
	
L1:
   ADD BX, 0002H	
   INC CX
   SUB AX, BX	
			
  JNZ L1
  MOV VAR, CX	
  
        ;RETURN 0
        MOV AH, 4CH
        INT 21H
    MAIN ENDP
END MAIN