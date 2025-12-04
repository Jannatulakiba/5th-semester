include 'emu8086.inc' 
.model small
.stack 100h
.DATA

.CODE
   MAIN PROC
     mov al, 0
     mov bl, 255

     start:
     
     cmp al, bl
     inc al 
     
     mov ah, 2
     mov dl, al
     int 21h 
     
     jnz start          

     MOV AH, 4CH               
     INT 21H
   MAIN ENDP
END MAIN