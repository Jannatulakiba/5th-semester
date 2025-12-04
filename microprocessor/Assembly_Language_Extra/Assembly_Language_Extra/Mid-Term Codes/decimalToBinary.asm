.MODEL SMALL
.STACK 100H
.DATA
 msg db 'Enter the Decimal Number: $'
 msg1 db 'Binary Number is: $'

.CODE

    MAIN PROC 
        MOV AX, @DATA
        MOV DS, AX
        
        ;Message Displaying
         MOV AH, 09H
         LEA DX, MSG
         INT 21H
         
         ;NUMBER iNPUT
         MOV AH, 01H
         INT 21H
         ;INPUT WILL BE IN THE AL IN THE FORM OF ASCII CODE 
         SUB AL, 48
         MOV AH, 0
         MOV BX, 2
         MOV DX, 0
         MOV CX, 0 
      AGAIN:   
         DIV BX ; DIVISOR AX = DIVIDEND
         PUSH DX
         INC CX
         CMP AX, 0
         JNE AGAIN 
         
         MOV AH, 09H
         LEA DX, MSG1
         INT 21H 
      DISP:   
         POP DX
         ADD DX, 48
         MOV AH, 02H
         INT 21H 
         LOOP DISP
         
       
         
         
        
        MOV AH, 4CH
        INT 21H
    MAIN ENDP
END MAIN