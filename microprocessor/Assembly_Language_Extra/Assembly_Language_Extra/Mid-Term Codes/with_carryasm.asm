.model small
.stack 100h
.data 
a dw ?
.code
main proc 
    mov ax,@data
    mov ds,ax
    
    mov bx,0124h
    mov dx,0A122h
    mov cx,0000H
    
    SUB bx,dx
    
    jnc abc
    inc cx
    
    abc:
    mov a,cx
    main endp
end main
    



