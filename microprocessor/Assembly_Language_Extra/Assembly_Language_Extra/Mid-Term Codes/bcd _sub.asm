.model small
.stack 100h
.data 
r1 dw ?
r2 dw ?
.code
main proc
    mov ax,@data
    mov ds,ax
    
    mov cx,00h
    
    mov ax,85h
    mov bx,74h
    sub ax,bx 
    das
    jnc abc 
    inc cx
    abc:
    mov r1,ax 
    mov r2,cx
    
    main endp
end main




