 .model small
.stack 100h
.data
           
   cr equ 0DH  ; cr represents carriage return
   lf equ 0AH  ; lf represents line feed        
           
   msg DB cr,lf,'ENTER AN ALGEBRIC EXPRESSION : ',cr,lf,'$'
   msg_correct DB  cr,lf,'EXPRESSION IS CORRECT.$'
   msg_left_bracket DB  cr,lf,'TOO MANY LEFT BRACKETS. BEGIN AGAIN!',cr,lf,'$'
   msg_right_bracket DB  cr,lf,'TOO MANY RIGHT BRACKETS. BEGIN AGAIN!',cr,lf,'$'
   msg_mismatch DB  cr,lf,'BRACKET MISMATCH. BEGIN AGAIN!',cr,lf,'$'
   msg_continue DB  cr,lf,'Type Y if you want to Continue : ',cr,lf,'$'
 
 
 
.code       
 
main proc
     
   mov ax,@data  ;get data segment  
   mov ds,ax     ;initialising
 
 
start:
   lea dx,msg   ;user prompt                 
   mov ah,9
   int 21h
 
 
   xor cx,cx      ;initializing cx             
   mov ah,1                
 
 
input:         ;this label for taking input   
 
    int 21h                
     
    cmp al,0Dh       ;checking if the enter is pressed or not            
           JE end_input                     
     
    ;if left bracket,then push on stack
    cmp al, "["              
           JE push_data         
    cmp al, "{"              
           JE push_data           
    cmp al, "("            
           JE push_data
     
     
    ;if right bracket,then pop stack
                   
    cmp al, ")"           
           JE parentheses       
    cmp al, "}"           
           JE curly_braces          
    cmp al, "]"            
           JE line_bracket     
    jmp input
 
 
 
push_data: 
    push ax                
    inc cx                  
    jmp input
        
     
     
                    
parentheses:                       
           dec cx             
           cmp cx,0           
           JL many_right        
            
           pop dx
           cmp dl, "("              
           JNE mismatch             
           JMP input          
              
              
curly_braces:                                           
        dec cx                  
        cmp cx,0                 
        JL many_right  
        pop dx       
        cmp dl, "{"           
        JNE mismatch            
        JMP input 
   
 
 
line_bracket:                 
        dec cx                
        cmp cx, 0                
        JL many_right
        pop dx           
        cmp dl, "["                
        JNE mismatch      
        JMP input 
      
                    
end_input: 
     cmp cx, 0                  
     JNE many_left           
      
     mov ah, 9               
     lea dx, msg_correct              
     int 21h                      
      
     lea dx, msg_continue             
     int 21h
                            
     mov ah,1                    
     int 21h                    
      
     cmp al, "Y"              
     JNE exit               
     JMP start                  
         
         
mismatch:  
     lea dx, msg_mismatch        
     mov ah,9                     
     int 21h
     JMP start                   
      
 
 
many_left: 
     lea dx, msg_left_bracket   
     mov ah,9
     int 21h
     JMP start               
            
            
many_right: 
     lea dx, msg_right_bracket     
     mov ah,9
     int 21h
     JMP start                   
 
 
 
exit: 
     mov ah,4ch               
     int 21h
 
 
MAIN ENDP
  END MAIN 