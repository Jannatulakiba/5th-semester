.MODEL SMALL
.STACK 100h
.DATA
    A DW 1200h       ; packed BCD for 1234
    B DW 5600h       ; packed BCD for 5678
    SUM DW 0         ; result
    CF_TEMP DB 0     ; temporary carry storage

.CODE
MAIN PROC
    MOV AX,@DATA
    MOV DS,AX

    ; -------- LOW BYTE ADDITION --------
    MOV AL, BYTE PTR [A]    ; low byte of A
    ADD AL, BYTE PTR [B]    ; low byte addition
    DAA                     ; adjust to valid BCD
    MOV BYTE PTR [SUM], AL  ; store low byte result
    ; store carry from DAA
    JC SET_CF
    MOV CF_TEMP,0
    JMP LOW_DONE
SET_CF:
    MOV CF_TEMP,1
LOW_DONE:

    ; -------- HIGH BYTE ADDITION --------
    MOV AL, BYTE PTR [A+1]  ; high byte of A
    ADD AL, BYTE PTR [B+1]  ; high byte addition
    ADC AL, CF_TEMP          ; add carry from low byte
    DAA                      ; adjust to valid BCD
    MOV BYTE PTR [SUM+1], AL ; store high byte result

    ; -------- PRINT RESULT --------
    ; SUM = [SUM+1][SUM] = 6912 BCD

    ; thousands digit
    MOV AL, BYTE PTR [SUM+1]
    SHR AL,4
    ADD AL,'0'
    MOV DL,AL
    MOV AH,2
    INT 21h

    ; hundreds digit
    MOV AL, BYTE PTR [SUM+1]
    AND AL,0Fh
    ADD AL,'0'
    MOV DL,AL
    MOV AH,2
    INT 21h

    ; tens digit
    MOV AL, BYTE PTR [SUM]
    SHR AL,4
    ADD AL,'0'
    MOV DL,AL
    MOV AH,2
    INT 21h

    ; ones digit
    MOV AL, BYTE PTR [SUM]
    AND AL,0Fh
    ADD AL,'0'
    MOV DL,AL
    MOV AH,2
    INT 21h
