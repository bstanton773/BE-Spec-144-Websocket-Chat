console.log('Hello from main.js!')


const socket = io()


socket.send('Hello from the client side')

socket.send({"name": "Brian"})

socket.on('message', (data) => {
    console.log("The client handle message received:", data)
})

socket.emit('custom_test_event', {"test": 123})

socket.on('another_event', (data) => {
    console.log('Another event received:', data)
})
