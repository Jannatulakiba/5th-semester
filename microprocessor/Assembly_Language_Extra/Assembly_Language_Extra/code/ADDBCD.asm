MOV  DL,34H
MOV  BL,99H    

MOV AL,DL
ADD AL,BL

DAA
  
JNC jump  

INC CH

jump:

MOV CL,AL




 HLT