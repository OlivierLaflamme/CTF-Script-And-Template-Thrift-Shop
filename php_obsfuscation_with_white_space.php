<?
function encode ($ code)
{
    $ c_len = strlen ($ code);
    for ($ i = 0; $ i <$ c_len; $ i ++) {
        $ t_bin = decbin (ord ($ code [$ i]));
        $ t_len = strlen ($ t_bin);
        if ($ t_len <= 6) {
            for ($ j = $ t_len; $ j <7; $ j ++) {
                $ t_bin = '0'. $ t_bin;
            }
        }
        $ bin. = $ t_bin;
    }
    $ ret = str_replace ("1", "\ t", $ bin);
    $ ret = str_replace ("0", "", $ ret);
    return $ ret;
}
function decode ($ code)
{
    $ code = str_replace ("\ t", "1", $ code);
    $ code = str_replace ("", "0", $ code);
    $ c_len = strlen ($ code);
    for ($ i = 0; $ i <$ c_len; $ i + = 7) {
        $ ret. = chr (bindec (substr ($ code, $ i, 7)));
    }
    return $ ret;
}
?>
