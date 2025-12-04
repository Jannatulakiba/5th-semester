.MODEL SMALL
.DATA
.CODE
MAIN PROC
 
    mov al, 18
    mov bl, 9
    
    
    zzz:
         div bl
         cmp ah, 0
         je zzz_end
         mov al, bl
         mov bl, ah
         mov ah, 0
         
    jmp zzz     
         
            
    zzz_end:
    mov ah, 2
    mov dl, bl
    add dl, 48
    int 21h
    


MAIN ENDP


END MAIN




