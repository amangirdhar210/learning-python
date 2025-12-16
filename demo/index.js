//1st demo js 

function logAnalytics(event) {
    Promise.resolve().then(() => {
        console.log(`Analytics event processed: ${event}`);
    });
}

function fetchUserProfile() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("User profile loaded");
        }, 0);
    });
}

function renderUI() {
    console.log("UI render scheduled");
}

function simulateUserFlow() {
    renderUI();

    for (let i = 1; i <= 10; i++) {
        logAnalytics(`click-${i}`);
    }

    fetchUserProfile().then(result => {
        console.log(result);
    });
}

simulateUserFlow();


//2nd demo


async function loadUser() {
    console.log("Loading user");
    await Promise.resolve()
    console.log("User loaded");
}

function startHeartbeat() {
    setInterval(() => {
        console.log("Heartbeat tick");
    }, 800);
}

loadUser();
startHeartbeat();

