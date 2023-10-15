import React, { useState } from 'react'

function Home() {
    let [customers, setCustomers] = useState([]);

    const fetchCustomers = () => {
        const requestOptions = {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'applications/json'
            }
        }

        fetch('http://127.0.0.1:8000/user/all/', requestOptions)
        .then((response) => {
            if (response.ok) {
                return response.json();
            }
            console.log("error")
        })
        .then((data) => setCustomers(data))
        .catch((err) => console.log(err))
    }

    return (
        <div>
            <button onClick={fetchCustomers}>click</button>
            <p>{customers}</p>
        </div>
    )
}

export default Home