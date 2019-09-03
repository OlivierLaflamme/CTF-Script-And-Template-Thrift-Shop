<?php
$protocol=$_SERVER['HTTPS']?"https":"http";
$retransmit_target_host = "172.16.15.1";
$retransmit_target_port = "80";
$headers="";
foreach (getallheaders() as $name => $value) {
    $headers=$headers."$name: $value\n";
}
$data = file_get_contents("php://input");
$opts = array (
    'http' => array (
        'method' => $_SERVER['REQUEST_METHOD'],
        'header'=> $headers,
        'content' => $data
    )
);
$log_path =  "/tmp/wtr_log.txt";
$log_content = date("Y-m-d h:i:sa", $d)." ".$_SERVER['REMOTE_ADDR']." ".$_SERVER['REQUEST_URI']." ".$data;
file_put_contents($log_path,$log_content,FILE_APPEND);
$context = stream_context_create($opts);
$html = file_get_contents($protocol."://".$retransmit_target_host.":".$retransmit_target_port.$_SERVER['REQUEST_URI'], false, $context);
echo $html;
