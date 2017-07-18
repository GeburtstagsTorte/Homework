<!DOCTYPE html><html><head><meta charset = "UTF-8"></head>
<body>
<form action = "allinone1.php" method = "post">
<?php
if (isset($_POST['gesendet'])){
    
    function checkInput(){
        $pdo2 = new PDO('mysql:host=localhost;dbname=testdatenbank', 'root', '');
        $sql = "SELECT code FROM session WHERE id = 0";
        $correct_code = $pdo2->query($sql)->fetch();
        $eingabe = doubleval($_POST["eingabe"]);
        
        if ($eingabe != $correct_code['code']){
            return 0;
        }
        if ($eingabe == $correct_code['code']){
            return 1;
        }
    }
    $tf2 = checkInput();
    // echo $tf2. '$tf2'; --> übermittelt 1, wie es vorgesehen ist
    return $tf2;
}


function randomizeColors($c0=50,$c1=50,$c2=50){
    $c=[$c0, $c1, $c2];
    $i = rand(0, 2);
    $c[$i]=255;
    return $c;
}

function createImage($cl_r, $cl_g, $cl_b, $code, $x=250, $y=75){
    $image = imagecreate($x, $y);
    $farbe = imagecolorallocate($image, $cl_r, $cl_g, $cl_b);
    imagefill($image, $x, $y, $farbe);
    
    $fontFarbe = imagecolorallocate($image, $cl_b, $cl_r, $cl_g);
    $schriftart = "C:\Windows\Fonts\impact.ttf";
    $ri = rand(25, -25);
    $ri2 = rand(2, 4);
    
    imagettftext($image, rand(15, 25), $ri, $x/$ri2-$ri/4, $y/2+$ri/4, $fontFarbe, $schriftart, $code);
    
    imagejpeg($image, "current_image1.jpeg");
    imagedestroy($image);
}

session_start();
$sessionid = session_id();
$code = rand(1000, 9999);
    
$pdo = new PDO('mysql:host=localhost;dbname=testdatenbank', 'root', '');
$statement = $pdo->prepare('UPDATE session SET sessionid = :sessionid, code = :code WHERE id = 0');
$statement->execute(array('sessionid'=>$sessionid, 'code'=>$code));
    
$c = randomizeColors();
createImage($c[0], $c[1], $c[2], $code);
?>
<p><img src="current_image1.jpeg"></p>
<p><input name="eingabe" maxlength="4"> CAPTCHA Eingabe</p>
<p><input type="submit" name="gesendet"> <input type="reset"></p>
</form>
</body></html>