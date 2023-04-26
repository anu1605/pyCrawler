

<?php
$url =  $_POST['url'];
$content = file_get_contents($url);
$im = imagecreatefromstring($content);
$imagepath = dirname(__FILE__, 2) . "/" . "images/" . date('Y:m:d h:ia') . ".png";
$imagepng = imagepng($im, $imagepath, 0);
?>