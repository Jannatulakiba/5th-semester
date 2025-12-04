org 100h
    mov al, 25h ; first BCD number
    mov bl, 12h ; second BCD number
    add al, bl  ; add
    daa         ; adjust for BCD
ret