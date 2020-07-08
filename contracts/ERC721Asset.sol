pragma solidity ^0.6.0;

import "./_lib/openzeppelin-contracts/contracts/presets/ERC721PresetMinterPauserAutoId.sol";
import "./_lib/openzeppelin-contracts/contracts/utils/Counters.sol";

contract ERC721Asset is ERC721PresetMinterPauserAutoId
{
	using Counters for Counters.Counter;

	struct Diamond
	{
		string cut;
		string clarity;
		string color;
		string carat;
		string system;
	}

	constructor(string memory name, string memory symbol, string memory baseURI) public ERC721PresetMinterPauserAutoId(name, symbol, baseURI)
	{

	}

	function mint
		(address to, string calldata cut,
			string calldata clarity, string calldata color,
			string calldata carat, string calldata system,
			string calldata tokenURI
		) external
	{
		uint tokenId = totalSupply();
		diamonds[tokenId].cut     = cut;
		diamonds[tokenId].clarity = clarity;
		diamonds[tokenId].color   = color;
		diamonds[tokenId].carat   = carat;
		diamonds[tokenId].system  = system;

		_setTokenURI(tokenId, tokenURI);

		this.mint(to);
	}

	function getDiamondInfoByTokenId(uint tokenId) public returns
		(string memory cut, string memory clarity,
			string memory carat, string memory system,
			string memory color)
	{
		diamonds[tokenId].cut     = cut;
		diamonds[tokenId].clarity = clarity;
		diamonds[tokenId].carat   = carat;
		diamonds[tokenId].system  = system;
		diamonds[tokenId].color   = color;
	}

	mapping (uint => Diamond) public diamonds;
}