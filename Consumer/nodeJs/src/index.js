const Kafka = require('no-kafka');

var valueSum = 0;

// Create an instance of the Kafka consumer
const consumer = new Kafka.SimpleConsumer({"connectionString":"10.30.80.164:29092"})
var data = function (messageSet, topic, partition) {

    messageSet.forEach(function (m) {
       
        let t = JSON.parse(m.message.value.toString('utf8'));
        console.log(t)
    });
};

// Subscribe to the Kafka topic
return consumer.init().then(function () {
    return consumer.subscribe('kafka-python-topic', data);
});