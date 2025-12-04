org 100h
    mov ax, 1234h ; first 16-bit number
    mov bx, 0020h ; second 16-bit number
    sub ax, bx    ; subtract bx from ax
    sbb ax, 0      ; subtract with borrow if needed
ret