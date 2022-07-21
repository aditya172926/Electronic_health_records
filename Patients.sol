// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

contract Patient {
    mapping(address => patient) internal patients;
    mapping(address => mapping(address => uint256)) internal patientToDoctor;
    mapping(address => mapping(string => uint256)) internal patientToFile;


    struct patient {
        string name;
        uint8 age;
        address patient_id;
        string residence_address;
        string contact_number;
        string email_id;
        string[] files; // hashes of file that belong to this user for display purpose
        address[] doctor_list;
    }

    modifier checkPatient(address id) {
        patient memory p = patients[id];
        require(p.patient_id > address(0x0)); //check if patient exist
        _;
    }
    function getPatientInfo()
        public
        view
        checkPatient(msg.sender)
        returns (
            string memory,
            address,
            uint8,
            string[] memory,
            address[] memory
        )
    {
        patient memory p = patients[msg.sender];
        return (p.name, p.patient_id, p.age, p.files, p.doctor_list);
    }

    function signupPatient(
        string memory _name,
        uint8 _age,
        string calldata _residence_address,
        string calldata _contact_number,
        string calldata _email_id
    ) public {
        patient memory p = patients[msg.sender];
        require(keccak256(abi.encodePacked(_name)) != keccak256(""));
        require((_age > 0) && (_age < 100));
        require(!(p.patient_id > address(0x0)));

        patients[msg.sender] = patient({
            name: _name,
            age: _age,
            patient_id: msg.sender,
            residence_address: _residence_address,
            contact_number: _contact_number,
            email_id: _email_id,
            files: new string[](0),
            doctor_list: new address[](0)
        });
    }
}