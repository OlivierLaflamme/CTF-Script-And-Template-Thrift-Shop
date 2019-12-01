import  re 
f  =  open ( 'function.txt' , 'r' ) 
for  i  in  f : 
    function  =  re . findall ( r '/ readfile | if | time | local | sqrt | et | na | nt | strlen | info | path | rand | dec | bin | hex | oct | pi | exp | log / ' , i )  
    if  function  ==  []  and  not  ' _ '  in  i : 
        print ( i )
