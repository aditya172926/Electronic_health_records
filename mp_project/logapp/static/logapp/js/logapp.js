var currentAccount;

// deployed contract address
const contractAddress = "0x174A3EdAF646fd9B9B946F3836Cf472097e47efA";
var contractAbi = '';

// getting the contract ABI
fetch("../static/logapp/utils/healthCare.json")
    .then(response => {
        return response.json();
    })
    .then(data => contractAbi = data.abi);

$(document).ready(function() {
    checkIfWalletIsConnected();
})

// importing the ethers from the JavaScript file.
var ethers = Object;
var provider = Object;
var healthCareContract;
function assignEtherObject(ethers) {
    ethers = ethers;
    provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    healthCareContract = new ethers.Contract(contractAddress, contractAbi, signer);
    // console.log(healthCareContract);
}

function test() {
    console.log("Function working");
    console.log(contractAbi);
    try {
        const ethereum = window;
        if (!ethereum) {
            console.log("Make sure you have metamask");
            return;
        } else {
            console.log("We have ethereum object ", ethereum);
        }
    } catch (error) {
        console.log(error);
    }
}

// check if the wallet account is connected or not.
const checkIfWalletIsConnected = async () => {
    try {
        const { ethereum } = window;

        if (!ethereum) {
            console.log("Make sure you have metamask!");
            return;
        } else {
            console.log("We have the ethereum object", ethereum);
        }

        const accounts = await ethereum.request({ method: "eth_accounts" });

        if (accounts.length !== 0) {
            const account = accounts[0];
            console.log("Found an authorized account:", account); // confirms that the wallet is connected
            currentAccount = account; // sets the current account's address.
        } else {
            console.log("No authorized account found");
        }
    } catch (error) {
        console.log(error);
    }
}

// function to connect to the metamask wallet
const connectWallet = async () => {
    try {
        const { ethereum } = window;
        if (!ethereum) {
            alert("Get Metamask extension!");
            return;
        }
        const accounts = await ethereum.request({ method: "eth_requestAccounts" });
        console.log("Connected", accounts[0]);
        currentAccount = accounts[0];
    } catch (error) {
        console.log(error);
    }
}

$(document).ready(function () {
    $("#patientSignUpForm").submit(function (event) {
        event.preventDefault();
        try {
            let name = $("#name").val();
            let address = $("#address").val();
            let age = $("#age").val();
            let contact_number = $("#contact").val();
            let email = $("#email").val();
            let categoryType = document.querySelector('input[name="signupRadios"]:checked').value;
            console.log(name, address, age, contact_number, email, categoryType);
            if (categoryType == "patient") {
                signupPatient(name, age, address, contact_number, email);
            }
            else if (categoryType == "doctor") {
                signUpdoctor(name);
            }
            else {
                console.log(categoryType);
            }
        } catch (error) {
            console.log(error);
        }
    });

    $("#giveAccessForm").submit(function(event) {
        event.preventDefault();
        try {   
            let doctorAddress = $("#doctoraddress").val();
            console.log("The give doctor address is - ", doctorAddress);
            giveAccessToDoctor(doctorAddress);
        } catch (error) {
            console.log(error);
        }
    });
});

// function to register a patient
const signupPatient = async (name, age, address, contact_number, email_id) => {
    try {
        const { ethereum } = window;
        if (ethereum) {
            // const provider = new ethers.providers.Web3Provider(ethereum);
            // const signer = provider.getSigner();
            // const healthCareContract = new ethers.Contract(contractAddress, contractAbi, signer);

            const patientTxn = await healthCareContract.signupPatient(
                name,
                age,
                address,
                contact_number,
                email_id
            );
            console.log("Mining...", patientTxn.hash);
            await patientTxn.wait();
            console.log("Mined", patientTxn.hash);
        } else {
            console.log("Ethereum object doesn't exists");
        }
    } catch (error) {
        console.log(error);
    }
}

// getting the patient profile
const getPatientProfile = async () => {
    try {
        const { ethereum } = window;
        if (ethereum) {
            // const provider = new ethers.providers.Web3Provider(ethereum);
            // const signer = provider.getSigner();
            // const healthCareContract = new ethers.Contract(contractAddress, contractAbi, signer);

            const patient = await healthCareContract.getPatientInfo();
            console.log(patient);
            let registerType = "patient";
            $("#patientName").html("Name: ");
            $("#patientAddress").html("Account Address: ");
            $("#patientAge").html("Age: ");
            $("#patientDoctorAccess").html("Doctors Address: ");
            $("#patientName").append(patient[0]);
            $("#patientAddress").append(patient[1]);
            $("#patientAge").append(patient[2]);
            $("#patientDoctorAccess").append(patient[4]);
        } else {
            console.log("Ethereum object not found");
        }
    } catch (error) {
        console.log(error);
    }
}

// function to register a doctor/medical personnel
const signUpdoctor = async (name) => {
    console.log(healthCareContract);
    try {
        const { ethereum } = window;
        if (ethereum) {
            const doctorTxn = await healthCareContract.signupDoctor(name);
            console.log("Mining...", doctorTxn.hash);
            await doctorTxn.wait();
            console.log("Mined ", doctorTxn.hash);
        } else {
            console.log("Ethereum object doesn't exists");
        }
    } catch (error) {
        console.log(error);
    }
}

// function to get the doctor's profile
const getDoctorProfile = async() => {
    // console.log(healthCareContract);
    try {
        const { ethereum } = window;
        if (ethereum) {
            const doctorProfile = await healthCareContract.getDoctorInfo();
            console.log("The doctor's profile", doctorProfile);
            $("#doctorname").html("");
            $("#doctoraddress").html("");
            $("#doctorpatients").html("");
            $("#doctorname").append("Doctor Name: " + doctorProfile[0]);
            $("#doctoraddress").append("Doctor id: " + doctorProfile[1]);
            $("#doctorpatients").append("Patients: " + doctorProfile[2]);
            let url = document.getElementById("doctorProfileButton").attributes.url.value;
            data = {};
            data['doctor'] = doctorProfile;
            $.ajax({
                method: 'GET',
                url: url,
                data: data,
                success: function(result) {
                    console.log(result);
                },
                error: function(response) {
                    console.log(response);
                }
            })
        } else {
            console.log("Ethereum object doesn't exists");
        }
    } catch (error) {
        console.log(error);
    }
}

const getPatInfoDoc = async (patientAddress) => {
    await console.log(patientAddress.toString());
    try {
        const { ethereum } = window;
        if (ethereum) {
            const patinfoTxn = await healthCareContract.getPatientInfoForDoctor(patientAddress);
            console.log(patinfoTxn);
            $("#docPatname").html("");
            $("#docPatAge").html("");
            $("#docPatAddr").html("");
            $("#docPatname").html("Patient Name: " + patinfoTxn[0]);
            $("#docPatAge").html("Patient Age: " + patinfoTxn[1]);
            $("#docPatAddr").html("Patient id: " + patinfoTxn[2]);
            $.each(patinfoTxn[3], function(a,b) {
                patFileBtn = `<button class='btn btn-light'><a target='blank' href='http://127.0.0.1:8080/ipfs/` + b + `?filename=` + b + `' >File ` + a + `</a></button> `;
                $('#patientPrescriptions').append(patFileBtn);
            })
        } else {
            console.log("Ethereum object not found");
        }
    } catch (error) {
        console.log(error);
    }
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
}

const getDoctorPatients = async () => {
    try {
        const { ethereum } = window;
        if (ethereum) {
            const getPatients = await healthCareContract.getDoctorInfo();
            console.log(getPatients);
            $("#patientAddesss").html("");
            $("#patientAddesss").html(getPatients[2]);
            $.each(getPatients[2], function(a,b) {
                patient_card = `<br><button class='btn btn-primary' onclick='getPatInfoDoc("${b}")' value='` + b + `'>`+ `Patient ` + a + `</button><br>`;
                $('#getDoctorsPatients').append(patient_card);
            });
        } else {
            console.log("Ethereum object not found");
        }
    } catch (error) {
        console.log(error);
    }
}

// patient can give the access to the doctor of his/her files.
const giveAccessToDoctor = async(doctorAddress) => {
    try {
        const { ethereum } = window;
        if (ethereum) {
            const giveAccessTxn = await healthCareContract.grantAccessToDoctor(doctorAddress);
            console.log("Mining... ", giveAccessTxn.hash);
            await giveAccessTxn.wait();
            console.log("Mined ", giveAccessTxn.hash);
            console.log("Access give from patient - " + currentAccount + " to doctor - " + doctorAddress);
        } else {
            console.log("Ethereum object not found");
        }
    } catch (error) {
        console.log(error);
    }
}

// get CSRF token to make a post request.
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const addFileToPatientChain = async (fileName, fileType, filehash) => {
    try {
        const { ethereum } = window;
        if (ethereum) {
            const addPatientFileTxn = await healthCareContract.addFile(fileName, fileType, filehash);
            console.log("Minig...", addPatientFileTxn.hash);
            await addPatientFileTxn.wait();
            console.log("Mined", addPatientFileTxn.hash);
        } else {
            console.log("Ethereum object not found");
        }
    } catch (error) {
        console.log(error);
    }
}

// function to upload a file which is added as text.
const uploadFile = async () => {
    let data = new FormData($('#uploadFileForm').get(0));
    console.log(data);
    // let csrf_token = document.getElementById("uploadFileForm").attributes.csrf_token.value;
    // console.log(csrf_token);
    const csrf_token = getCookie('csrftoken');
    console.log(csrf_token);
    $.ajax({
        url: document.getElementById("uploadFileForm").attributes.url.value,
        method: document.getElementById("uploadFileForm").attributes.method.value,
        headers: {'X-CSRFToken': csrf_token},
        data: data,
        cache: false,
        processData: false,
        contentTypr: false,
        success: function(result) {
            console.log("The file was sent");
        },
        error: function(response) {
            console.log(response);
        }
    });
}

const uploadPrescriptions = async () => {
    let presName = $("#pres-fname").val();
    let treatmentName = $("#pres-treatment").val();
    let dose = $("#pres-dose").val();
    let presData = {
        "presName": presName,
        "treatmentName": treatmentName,
        "dose": dose
    }
    // var data = $(this).serialize();
    // const csrf_token = getCookie('csrftoken');
    $.ajax({
        url: document.getElementById("prescriptionForm").attributes.url.value,
        method: "GET",
        data: presData,
        success: function(result) {
            console.log(result["Name"]);
            console.log(result["Hash"])
            addFileToPatientChain(result["Name"], "txt", result["Hash"]);
            console.log("The pres was sent");
        },
        error: function(response) {
            console.log(response);
        }
    });
}