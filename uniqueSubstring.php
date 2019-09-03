<?php

// Problem Statement -  find the length of the longest substring without repeating characters

//	Given "abcabcbb", the answer is "abc", which the length is 3.

function uniqueSubstring($inputString){
	$subString = '';
	$longestString = '';
	$inputStringA = str_split($inputString);
	for($i=0; $i<count($inputStringA); $i++){
		$index = strpos($subString, $inputStringA[$i]); // Return false if NO character found
		if( ($index === false) || (strlen($subString) == 1) ){
			$subString = $subString.$inputStringA[$i];
		}else{
			if(strlen($subString) > strlen($longestString)){
				$longestString = $subString;
			}
			$subString = $inputStringA[$i];
		}
	}	
	return $longestString.strlen($longestString);	
}

var_export(uniqueSubstring('abcdajkesplmnzxbcabcdeabcdbcdefsre'));
?>
