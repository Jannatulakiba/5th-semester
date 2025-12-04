include 'emu8086.inc'
.model small
.stack 100h
.data
 
   a dw ?
   
.code
    main proc
        
     mov ax, 0008h
     mov bx, 0003h 
     
     mov a, ax  
     
     loop1:
     cmp a,0008h
     je loop2
     jne end1
       
     loop2:
     cmp bx,0003h
     je loop3
     jne end1  
     
     
     
     
     loop4:
     cmp a,00ffh
     je loop5
     jne end3
       
     loop5:
     cmp bx,1000h
     je loop3
     jne end3
     
     loop3:
     mul bx 
     jmp end2
     
     
     end1:
     cmp a, 00ffh
     je loop4
     printn " Multiplication is not possibe "
     jmp end2 
     
     end3:
     printn " Multiplication is not possibe "
      
     end2:
              
     
     main endp   
    
endp main