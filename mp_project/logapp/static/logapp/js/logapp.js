var currentAccount;

// deployed contract address
const contractAddress = "0xc01399A54bEd59FC9337182BE3BA4A582d9e5bEe";
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
            // console.log(doctorProfile);
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