<?php
Class Node{
	public $data;
	public $next;
	function __construct($data){
		$this->data = $data;
		$this->next = NULL;
	}
	function getNode(){
		return $this->data;
	}
}

Class LinkedList{
	public $headNode;
	public $tailNode;
	public $total;
	function __construct(){
		$this->headNode = NULL;
		$this->tailNode = NULL;
		$this->total = 0;
	}
	// PUSH and POP as Stack FILO
	public function push($data){
		$link = new Node($data);
		$link->next = $this->tailNode;
		$this->tailNode = $link;
		// If HEAD is null then assign node and exit
		if($this->headNode == NULL){
			$this->headNode = $link;
		}
		$this->total++;
	}
	public function pop(){
		$current = $this->tailNode;
		$this->tailNode = $current->next;
		$current->next = NULL;
	}
	public function display(){
		$listData = [];
		$current = $this->tailNode;
		while($current != NULL){
			array_push($listData,$current->getNode());
			$current = $current->next;
		}
		var_export($listData);
	}
}
$linkedList = new LinkedList();
$linkedList->push(3);
$linkedList->push("Second");
$linkedList->push("Third");
$linkedList->push("5");
$linkedList->pop();
$linkedList->display();

?>
