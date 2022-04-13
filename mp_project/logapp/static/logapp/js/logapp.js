var currentAccount;

const contractAddress = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
var contractAbi = '';

fetch("../static/logapp/utils/healthCare.json")
.then(response => {
    return response.json();
})
.then(data => contractAbi = data.abi);

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

const connectWallet = async () => {
    try {
        const {ethereum} = window;
        if (!ethereum) {
            alert("Get Metamask extension!");
            return;
        }
        const accounts = await ethereum.request({method:"eth_requestAccounts"});
        console.log("Connected", accounts[0]);
        currentAccount = accounts[0];
    } catch (error) {
        console.log(error);
    }
}