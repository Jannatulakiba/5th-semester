org 100h
    mov ax, 4h ; number to find square root of
    mov bx, 1h  ; current guess

next_guess:
    mov ax, 4h
    div bx       ; ax = number / guess     
    cmp ax, bx
    je done
    
    add bx, 1
    jmp next_guess
done:
    mov ax, bx   ; move result to ax

ret