org 100h

    mov dx, 1234     ; the decimal number you want to print
    call print_dec   ; print DX as decimal

    mov ah, 4Ch      ; exit to DOS
    int 21h

;-----------------------------------------------------
; print_dec: prints the 16-bit unsigned number in DX
;-----------------------------------------------------
print_dec:
    push ax
    push bx
    push cx
    push dx

    mov ax, dx       ; number to AX for division
    xor cx, cx       ; digit count = 0
    mov bx, 10       ; divisor for decimal

.next_digit:
    xor dx, dx       ; clear remainder
    div bx           ; AX ÷ 10 ? AX=quotient, DX=remainder
    push dx          ; store remainder (digit)
    inc cx
    test ax, ax
    jnz .next_digit  ; repeat until quotient = 0

.print_loop:
    pop dx           ; get a digit back
    add dl, '0'      ; convert to ASCII
    mov ah, 02h
    int 21h          ; print character
    loop .print_loop ; CX times

    pop dx
    pop cx
    pop bx
    pop ax
    ret