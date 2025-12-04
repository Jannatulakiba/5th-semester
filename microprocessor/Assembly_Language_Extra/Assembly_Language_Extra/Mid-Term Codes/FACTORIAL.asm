org 100h
.data
ans db ?
.code
main proc
    mov ax,@data
    mov ds,ax
    mov al,5
    mov cl,4
    mov bl,al
    sub bl,1
    l:
    mul bl
    sub bl,1
    loop l
    
    mov ans,al  
    mov ah,2
    mov dl,ans 
    int 21h 
    mov ah,4ch
    int 21h
    
    main endp
end main
    




