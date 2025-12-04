.model small
.stack 100h
.data
 a dw ? 
.code
main proc 
    mov ax,@data
    mov ds,ax
    
    mov bx,01223h
    mov dx,01122h
    mov cx,0000
    
    add bx,dx
    
    jnc abc
    inc cx
    
    abc:
    mov a,cx
    main endp
end main
    