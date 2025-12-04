org 100h
    mov al, 25h ; first BCD number
    mov bl, 12h ; second BCD number
    sub al, bl  ; subtract
    daa         ; adjust for BCD
ret