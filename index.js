


const creds = require('./creds');
const data = require('./data.json');
const { IotData } = require('aws-sdk');

async function publishData() {
    const iotdata = new IotData({ ...creds, endpoint: 'a2ebpuf0caw23t-ats.iot.ap-south-1.amazonaws.com' });
    while (true) {
        await Promise.all(data.map(
            d => iotdata.publish({
                topic: 'iot/abhi-streaming-etl-iottopic',
                payload: JSON.stringify(d),
                qos: 0
            }).promise()
        ));
        console.log("published dataset.");
    }
}

publishData().catch(e => console.log(e.stack));