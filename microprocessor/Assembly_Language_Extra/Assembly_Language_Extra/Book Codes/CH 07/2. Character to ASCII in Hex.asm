 .MODEL SMALL
 .STACK 100H
 .DATA
 M1 DB 0AH, 0DH, "TYPE A CHARACTER:",'$'
 M2 DB 0AH, 0DH, "THE ASCII CODE OF"
 C1 DB ?, "IN HEXA IS", '$'
 
 .CODE
 MAIN PROC
 MOV AX, @DATA
 MOV DS, AX
 BEGIN:   MOV AH, 9
          LEA DX, M1
          INT 21H
          
          MOV AH, 1
          INT 21H
          
          CMP AL, 0DH
          JE OUT_  
          
          MOV CL, AL
          MOV BL, AL
          
          MOV AH, 9
          LEA DX, M2 
          INT 21H
          
          MOV CL, 4
          SHR C1, CL
          
          ADD C1, 30H
          MOV DL, C1
          JMP EXE1
          
 continue:  AND BL, 0FH
            CMP BL, 9
            JP ERROR_
            
            ADD BL, 30H
            MOV DL, BL
            JMP EXE2
            
EXE1:       MOV AH, 2 
            INT 21H
            JMP BEGIN
            
EXE2:       MOV AH, 2
            INT 21H
            JMP BEGIN
            
ERROR_:     ADD BL, 37H
            MOV DL, BL
            MOV AH, 2
            INT 21H
            JMP BEGIN
            
OUT_:       MOV AH, 4CH
            INT 21H
   MAIN ENDP 
 END MAIN
 
          