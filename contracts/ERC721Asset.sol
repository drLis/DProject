pragma solidity ^0.6.0;

import "./_lib/openzeppelin-contracts/contracts/presets/ERC721PresetMinterPauserAutoId.sol";

contract ERC721Asset is ERC721PresetMinterPauserAutoId
{
	constructor(string memory name, string memory symbol, string memory baseURI) public ERC721PresetMinterPauserAutoId(name, symbol, baseURI)
	{

	}
}