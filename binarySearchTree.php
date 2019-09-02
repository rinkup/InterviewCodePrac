<?php
function binarySearchTree($findElement, $input, $pointer){
	$size = count($input);
	$mid = floor($size/2);
	if($input[$mid] < $findElement){
		$input = array_splice($input, $mid, $size);
		return binarySearchTree($findElement, $input, ($pointer+$mid));
	}elseif($input[$mid] > $findElement){
		$input = array_splice($input, 0, $mid);
		return binarySearchTree($findElement, $input, $pointer);
	}else{
		return $pointer+$mid;
	}
}
$input = [4, 6, 27, 43, 54, 85, 105, 127, 153, 223];
$findElement = 153;
$findElementIndex = binarySearchTree($findElement, $input, 0);
echo $findElementIndex."\n";
?>
