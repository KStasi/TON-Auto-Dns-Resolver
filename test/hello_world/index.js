const { TONClient } = require('ton-client-node-js');

const helloPackage = require('./helloPackage');

const helloKeys = {
    public: '55d7bab463a6a3ef5e03bb5f975836ddfb589b9ccb00329be7da8ea981c5268a',
    secret: 'de93a97c7103c2d44e47972265cfdfe266fd28c8cadc4875804ee9f57cf786d6',
};

async function main(ton) {
    const helloAddress = (await ton.contracts.deploy({
        package: helloPackage,
        constructorParams: {},
        keyPair: helloKeys,
    })).address;
    console.log(`Hello contract was deployed at address: ${helloAddress}`);

    const response = await ton.contracts.run({
        address: helloAddress,
        abi: helloPackage.abi,
        functionName: 'sayHello',
        input: {},
        keyPair: helloKeys,
    });
    console.log('Hello contract was responded to sayHello:', response);

    const localResponse = await ton.contracts.runLocal({
        address: helloAddress,
        abi: helloPackage.abi,
        functionName: 'sayHello',
        input: {},
        keyPair: helloKeys,
    });
    console.log('Hello contract was ran on a client TVM and also responded to sayHello:', localResponse);
}

(async () => {
    try {
        const ton = TONClient.shared;
        ton.config.setData({
            servers: ['http://0.0.0.0']
        });
        await ton.setup();
        await main(ton);
        console.log('Hello TON Done');
        process.exit(0);
    } catch (error) {
        console.error(error);
    }
})();
