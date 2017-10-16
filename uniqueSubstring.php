<?php

// Problem Statement -  find the length of the longest substring without repeating characters

//	Given "abcabcbb", the answer is "abc", which the length is 3.

function uniqueSubstring($inputString){
	$inputStringA = str_split($inputString);
	$subString = '';
	$out = [];
	for($i=0; $i<count($inputStringA); $i++){
		$index = strpos($subString, $inputStringA[$i]); // Return false if NO character found
		if( ($index === false) || (strlen($subString) == 1) ){
			$subString = $subString.$inputStringA[$i];
			echo $subString ."    ".$inputStringA[$i]."\n";
		}else{
			array_push($out,$subString);
			$subString = $inputStringA[$i];
		}
//	echo $inputStringA[$i];
	}	
	array_push($out,$subString);
	return $out;	
}

var_export(uniqueSubstring('abcabcbb'));
?>
