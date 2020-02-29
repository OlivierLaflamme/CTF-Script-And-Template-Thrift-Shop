Import re


Def  filter_tags ( htmlstr ):
    # First filter CDATA
    re_cdata = the re.compile ( ' // <! \ [CDATA \ [[^>] * // \] \]> ' , re.I)   # match CDATA
    Re_script = re.compile( ' <\s*script[^>]*>[^<]*<\s*/\s*script\s*> ' , re.I)   # Script
    Re_style = re.compile( ' <\s*style[^>]*>[^<]*<\s*/\s*style\s*> ' , re.I)   # style
    re_br = the re.compile ( ' <br \ S *? /?> ' )   # processing newline
    Re_h = re.compile( ' </?\w+[^>]*> ' )   # HTML tags
    Re_comment = re.compile( ' <!--[^>]*--> ' )   # HTML Notes
    s = re_cdata.sub( ' ' , htmlstr)   # Remove CDATA
    s = re_script.sub( ' ' , s)   # Remove SCRIPT
    s = re_style.sub( ' ' , s)   # remove style
    s = re_br.sub( ' \n ' , s)   # convert br to newline
    s = re_h.sub( ' ' , s)   # Remove HTML tags
    s = re_comment.sub( ' ' , s)   # Remove HTML comments
    # Remove the extra blank lines
    Blank_line = re.compile( ' \n + ' )
    s = blank_line.sub( ' \n ' , s)
    S = replaceCharEntity (S)   # replaced entity
    Return s


Def  replaceCharEntity ( htmlstr ):
    CHAR_ENTITIES  = { ' nbsp ' : '  ' , ' 160 ' : '  ' ,
                     ' lt ' : ' < ' , ' 60 ' : ' < ' ,
                     ' gt ' : ' > ' , ' 62 ' : ' > ' ,
                     ' amp ' : ' & ' , ' 38 ' : ' & ' ,
                     ' quot ' : ' " ' , ' 34 ' : ' " ' , }

    re_charEntity = re.compile( r '  ? ( ?P<name> \w + ) ; ' )
    Sz = re_charEntity.search(htmlstr)
    While sz:
        Entity = sz.group()   # entity full name, such as >
    Key = sz.group( ' name ' )   # remove &; after entity, such as > for gt
    Try :
        Htmlr = re_charEntity.sub( CHAR_ENTITIES [key], htmlstr, 1 )
        Sz = re_charEntity.search(htmlstr)
    the except  KeyError :
        Htmlstr = re_charEntity.sub( ' ' , htmlstr, 1 )
        Sz = re_charEntity.search(htmlstr)
    Return htmlstr


If  __name__  ==  ' __main__ ' :
    s =  file ( ' index.html ' ).read()
    News = filter_tags(s)
    Print news
