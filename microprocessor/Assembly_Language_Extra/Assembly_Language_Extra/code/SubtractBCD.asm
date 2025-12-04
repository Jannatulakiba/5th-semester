MOV  DL,34H
MOV  BL,99H    

MOV AL,DL
SUB AL,BL

DAS
  
JNC jump  

INC CH

jump:

MOV CL,AL




 HLT