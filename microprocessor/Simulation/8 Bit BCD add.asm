.MODEL SMALL
.STACK 100H
.DATA
    A DB 25H     ; BCD 25
    B DB 37H     ; BCD 49
    SUM DB ?

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    MOV AL, A    ; AL = 25 (BCD)
    ADD AL, B    ; AL = AL + B
    DAA          ; Decimal Adjust after Addition (make it valid BCD)
    MOV SUM, AL  ; Save result

    ; Print result high nibble
    MOV AH, 2
    MOV DL, SUM
    SHR DL, 4         ; High nibble
    ADD DL, 30H       ; Convert to ASCII
    INT 21H

    ; Print result low nibble
    MOV DL, SUM
    AND DL, 0FH       ; Low nibble
    ADD DL, 30H
    INT 21H

    ; Exit
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
