import React, { Component } from 'react'

export default class FlaggedSite extends Component {
    render() {
        return (
            <div className="row container">
                <div className="col-4">
                    <h5 className="mt-3 fw-bold text-center">Fake News SITES</h5>
                </div>
                <div className="col-4">
                    <h5 className="mt-3 fw-bold text-center">UNRELIABLE SITES</h5>
                </div>
                <div className="col-4">
                    <h5 className="mt-3 fw-bold text-center">UNVERIFIED SOURCES</h5>
                </div>
            </div>
        )
    }
}
