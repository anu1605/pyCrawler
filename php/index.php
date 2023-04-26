<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
</head>

<body>
    <div class="container">

        <?php

        $link = file_get_contents(dirname(__FILE__, 2) . "/" . "imageLink.txt");

        $content = file_get_contents($link);


        $im = imagecreatefromstring($content);
        $imagepath = dirname(__FILE__, 2) . "/" . "images/" . date('Y:m:d h:ia') . ".png";

        $imagepng = imagepng($im, $imagepath, 0);

        // require 'image.compare.class.php';
        // $class = new compareImages;
        // echo $class->compare('1st.png', '3.png');

        // $url1 = dirname(__FILE__, 2) . '/images/1st.png';
        // $url2 = dirname(__FILE__, 2) . '/images/classified.jpeg';

        ?>


    </div>

</body>
<script src="/js/index.js"></script>

</html>