import React, { useState } from 'react';

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

export default function SearchBar() {
    const [val, setVal] = useState("")

    const csrftoken = getCookie('csrftoken');

    function checkNews(url) {
        console.log('fetching data...', url)
        const testurl = 'http://a.msn.com/01/en-in/AALoo9a'

        fetch('/api/check-news/', {
            // credentials: 'include',
            method: 'POST',
            // mode: 'cors',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
                'Access-Control-Allow-Origin': '*',
            },
            body: JSON.stringify({ 'enteredURL': url }),
        })
            .then(response => { console.log(response); response.json() })
            .then(data => console.log("Data", JSON.stringify(data, null, 4)))
        // .then(data => console.log(data))
        // .catch(error => console.log(error))
    }

    return (
        <form method="post" onSubmit={(e) => { e.preventDefault(); }}>
            <div id="div_id_entryURL" className="row">
                <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
                <input type="search" name="enteredURL" className="col-11" placeholder="Enter the link of the news article to check" value={val} onChange={e => setVal(e.target.value)} id="id_entryURL" required />
                <button //type="submit"
                    onSubmit={(e) => { e.preventDefault(); checkNews(val) }}
                    onClick={(e) => { e.preventDefault(); checkNews(val) }}
                    name="submit"
                    className="col-1 input-group-text btn btn-dark"
                    id="submit-id-submit">CHECK</button>
            </div>
        </form>
    )
}

{/* <form method="GET" action=".">
    <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken} />
    <div className="input-group rounded">
        <input type="search" className="form-control rounded" placeholder="Enter the link of the news article here!" aria-label="Search"
            aria-describedby="search-addon" />
        <button onClick={checkNews} className="input-group-text btn btn-dark" id="search-addon">
            CHECK
        </button>
    </div>
</form> */}