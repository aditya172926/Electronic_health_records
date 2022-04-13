const test2 = () => {
    console.log("Function working");
}

var currentAccount;

function test() {
    console.log("Function working");
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