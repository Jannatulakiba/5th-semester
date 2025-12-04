org 100h
    mov ax, 9h ; number to find square root of
    mov cx, 0h  ; result (square root)
    mov bx, 1h  ; current guess

next_guess:
    mov dx, 0h
    mov ax, 9h
    div bx       ; ax = number / guess

    add ax, bx   ; ax = guess + (number / guess)
    shr ax, 1    ; ax = (guess + (number / guess)) / 2
    cmp ax, cx   ; compare new guess with previous guess
    je done       ; if equal, we're done
    mov cx, ax   ; update result
    inc bx       ; increment guess
    jmp next_guess
done:
    mov ax, cx   ; move result to ax
ret