org 100h
    mov ax, 0234h ; first 16-bit number
    mov bx, 0020h ; second 16-bit number
    mul bx        ; multiply ax by bx, result in dx:ax
ret