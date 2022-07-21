// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
pragma experimental ABIEncoderV2;

import './medicalinstitution.sol';
import './Patients.sol';
import './FileStorage.sol';

contract healthCare is MedicalInstitution, Patient, File {
    address private owner;
    uint256 private gpos;

    ///////////////////////////////////////// Custom data structures//////////////////////////////////////

    struct records {
        address doctor_id;
        address patient_id;
        string files_metadata;
    }

    struct appointments {
        address doctor_id;
        address patient_id;
        string appointment_details;
    }

    mapping(address => appointments[]) public doctorAppointments;
    mapping(address => appointments[]) public patientAppointments;
    //////////////////////////////////////////////////////////////////////////////////////////////
    constructor() public {
        owner = msg.sender;
    }

    // check if the calling party has the access to the requesting file or not.
    modifier checkFileAccess(
        string memory role,
        address id,
        string memory fileHashId,
        address pat
    ) {
        uint256 pos;
        if (keccak256(abi.encodePacked(role)) == keccak256("doctor")) {
            require(patientToDoctor[pat][id] > 0);
            pos = patientToFile[pat][fileHashId];
            require(pos > 0);
        } else if (keccak256(abi.encodePacked(role)) == keccak256("patient")) {
            pos = patientToFile[id][fileHashId];
            require(pos > 0);
        }
        _;
    }

    // granting the file access to the doctor
    function grantAccessToDoctor(address doctor_id)
        public
        checkPatient(msg.sender)
        checkDoctor(doctor_id)
    {
        patient storage p = patients[msg.sender];
        Med_Institution storage d = institutions[doctor_id];
        require(patientToDoctor[msg.sender][doctor_id] < 1); // this means doctor already been access

        p.doctor_list.push(doctor_id); // new length of array
        uint256 pos = p.doctor_list.length;
        gpos = pos;
        patientToDoctor[msg.sender][doctor_id] = pos;
        d.patient_list.push(msg.sender);
    }

    // adding a file
    function addFile(
        string memory _file_name,
        string memory _file_type,
        string memory _fileHash
    ) public checkPatient(msg.sender) {
        patient storage p = patients[msg.sender];

        require(patientToFile[msg.sender][_fileHash] < 1);

        hashToFile[_fileHash] = files({
            file_name: _file_name,
            file_type: _file_type,
            file_hash: _fileHash
        });
        p.files.push(_fileHash);
        uint256 pos = p.files.length; // getting the updated length
        patientToFile[msg.sender][_fileHash] = pos;
    }

    function addUserFiles(
        string memory _file_name,
        string memory _file_type,
        string memory _file_hash
    ) public checkPatient(msg.sender) {
        patientFiles[msg.sender].push(
            files({
                file_name: _file_name,
                file_type: _file_type,
                file_hash: _file_hash
            })
        );
    }

    function getUserFiles(address sender) public view returns (files[] memory) {
        return patientFiles[sender];
    }

    function getPatientInfoForDoctor(address pat)
        public
        view
        checkPatient(pat)
        checkDoctor(msg.sender)
        returns (
            string memory,
            uint8,
            address,
            string[] memory
        )
    {
        patient memory p = patients[pat];

        //require(patientToDoctor[pat][msg.sender] > 0);

        return (p.name, p.age, p.patient_id, p.files);
    }
}
