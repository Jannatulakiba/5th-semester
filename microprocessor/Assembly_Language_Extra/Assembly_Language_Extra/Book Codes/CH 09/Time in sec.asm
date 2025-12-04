 .model small
 .stack 100h
 .data
 msg1 db 'Enter time in seconds:$'
 msg2 db 10,13,'Time in Hour Miniute And Second Is:$'
 .cod
 emain proc
    mov ax,@data
    mov ds,ax
    lea dx,msg1
    mov ah,9int 21h
    
    call indec
    push ax 
    
    xor cx,cx
    mov cl,3
    pop ax
l1:xor dx,dx
    mov bx,60d
    div bx 
    push dx 
   loop l1   
      
 
 mov ah,9
 lea dx,msg2
 int 21h
 
 mov cl,3
 
 time:
    pop ax
    call outdec 
    mov ah,2
    mov dl,':'
    int 21h
   loop time
   
   mov ah, 4ch
   int 21h
   main endp
 
 include outdec.asm 
 include indec.asm
 end main