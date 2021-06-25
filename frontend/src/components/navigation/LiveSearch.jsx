import React from 'react'

export default function LiveSearch() {
    return (
        <div>
            <h5 className="fw-bold mt-3 ">Live Results Search</h5>
            <div className="input-group rounded mt-3">
            <input type="search" className="form-control rounded" placeholder="Enter the link of the news article here!" aria-label="Search"
                aria-describedby="search-addon" />
            <button className="input-group-text btn btn-dark" id="search-addon">
                <i className="fas fa-search"></i>
            </button>
            </div>
        </div>
    )
}
