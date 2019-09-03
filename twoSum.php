<?php
/*
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.
	You may assume that each input would have exactly one solution, and you may not use the same element twice.
	
	Given nums = [2, 7, 11, 15], target = 9,
	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].

*/
function twoSum($inputArray, $targetNumber){
	$outputIndex = array();
	for($i=0; $i<count($inputArray); $i++){
		$firstElement=$inputArray[$i];
		$secondElement=$targetNumber - $firstElement;
		if(array_search($secondElement, $inputArray)){
			if(!array_search("$secondElement,$firstElement", $outputIndex)){
				array_push($outputIndex,"$firstElement,$secondElement");
			}
		}
	}
	return $outputIndex;
}
$inputArray = [1, 2, 4, 6,  7, 8, 11, 15];
$targetNumber = 9;
var_export(twoSum($inputArray, $targetNumber));
?>
