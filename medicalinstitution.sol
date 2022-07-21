// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract MedicalInstitution {

    mapping(address => Med_Institution) internal institutions; // doctor and list of patient profile he can access
    mapping(address => mapping(address => uint256)) internal institutionToPatient;

    struct Med_Institution {
        string name;
        address id; 
        address[] patient_list;
    }

    
    modifier checkDoctor(address id) {
        Med_Institution memory d = institutions[id];
        require(d.id > address(0x0)); //check if doctor exist
        _;
    }

    function getDoctorInfo()
        public
        view
        checkDoctor(msg.sender)
        returns (
            string memory,
            address,
            address[] memory
        )
    {
        Med_Institution memory d = institutions[msg.sender];
        return (d.name, d.id, d.patient_list);
    }

    function signupDoctor(string memory _name) public {
        Med_Institution memory d = institutions[msg.sender];
        require(keccak256(abi.encodePacked(_name)) != keccak256(""));
        require(!(d.id > address(0x0)));

        institutions[msg.sender] = Med_Institution({
            name: _name,
            id: msg.sender,
            patient_list: new address[](0)
        });
    }

}