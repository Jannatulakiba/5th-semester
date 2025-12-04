include "emu8086.inc" 
.MODEL SMALL
.DATA
.CODE
MAIN PROC
 
    mov al, 7  ;m
    mov bl, 9   ;n
    mov cl, bl
    mov dl, 10
    print "."
    anik:
         mul dl
         div bl 
         mov ch , ah
         
        
         

         mov ah, 2
        mov dl, al
        add dl, 48
        int 21h  
        mov al , ch
        
    loop anik     
         
            
    
    


MAIN ENDP


END MAIN