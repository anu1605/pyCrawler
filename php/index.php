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
    <div class="container"></div>
</body>
<script>
    var url;
    $('document').ready(
        setTimeout(function() {
            url = $('.container > img').attr('data-src');
            $.ajax({
                url: "getImage.php",
                type: 'post',
                data: {
                    action: 'getImage',
                    url: url
                }

            })

        }, 1000))
    $('.container').load('/imageLink.txt')
</script>

</html>