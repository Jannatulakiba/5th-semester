
	.MODEL SMALL
	.STACK 100H
	.DATA
		d1 dw 1101
	.CODE
		MAIN PROC FAR
		MOV AX,@DATA
		MOV DS,AX

	mov ax,1000 
	
	mov BX,0AH
	MOV CX,00H
	MOV DX,00H 
	
	again:
    DIV BX;
    PUSH DX;
    INC CX;
    
    CMP AX,0;
    
    JNE again  
    
    
    
    L1:
    pop dx  
    MOV BX,2
    ADD DX,48 
    MOV AX,DX
    MUL BX
     
    
    
    ADD BX,2   
    
    ADD AX,AX
    
    MOV AH,02H  
    
    INT 21H
    
    LOOP L1
     
    
    MOV AH,4CH
    INT 21H
    
    MAIN ENDP
    
END MAIN	
	
	
	
	
	
	
	
	