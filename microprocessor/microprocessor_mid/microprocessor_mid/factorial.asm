org 100h
    mov ax, 1h
    mov cx, 5h ; number to do factorial
    
count:
    mul cx
    loop count     
ret