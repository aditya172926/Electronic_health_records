// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract File {
    mapping(string => files) hashToFile; //filehash to file info

    struct files {
        string file_name;
        string file_type;
        string file_hash;
    }
    mapping(address => files[]) internal patientFiles;

    // check if the file exists or not
    modifier checkFile(string memory fileHashId) {
        bytes memory tempString = bytes(hashToFile[fileHashId].file_name);
        require(tempString.length > 0); //check if file exist
        _;
    }
    function getFileInfo(string memory fileHashId)
        public
        view
        checkFile(fileHashId)
        returns (files memory)
    {
        return hashToFile[fileHashId];
    }
}