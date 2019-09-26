pragma solidity >=0.5.0 <0.6.0;
contract HelloTON {
	uint32 deployTime;
  constructor() public {
		deployTime = uint32(now);
	}
	function sayHello() public view returns (uint32) {
		return deployTime;
	}
}
