<!DOCTYPE html><html><head><meta charset = "UTF-8"></head><body>
<?php
$x = NULL;
try{
    if (!isset($x)){
        throw new Exception('$x ist nicht set');
    }    
}
catch(Exception $e){
    echo $e->getMessage();
}
finally{
    echo "<br>finally";
}
?>
</body></html>