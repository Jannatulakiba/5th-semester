include "emu8086.inc"
.MODEL SMALL
.CODE
MAIN PROC

    mov al, 80h
    mov bl, 0ffh
    mov cl, 0
    
    anik:
    cmp bl, al
    je end_anik
    
    
    mov ah, 2
    mov dl, al
    int 21h 
     
    inc al 
    
    print " "
    inc cl
    cmp cl, 10
    jg new
    
    jmp anik
    
    new:
    printn
    mov cl, 0
    jmp anik
     
    end_anik:

END MAIN

