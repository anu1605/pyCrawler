

<?php
$link = file_get_contents(dirname(__FILE__, 2) . "/" . "imageLink.txt");

$content = file_get_contents($link);


$im = imagecreatefromstring($content);
$imagepath = dirname(__FILE__, 2) . "/" . "images/" . date('Y:m:d h:ia') . ".png";

$imagepng = imagepng($im, $imagepath, 0);


?>