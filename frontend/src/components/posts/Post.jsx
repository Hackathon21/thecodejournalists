import React, { Component } from 'react'

export default class Post extends Component {
    render() {
        return (
            <div className="card mb-3 border-0" style={{maxWidth: "540px"}}>
                <div className="row g-0">
                    <div className="col-md-4">
                        <img src="../../" className="img-fluid rounded-start" alt="..."/>
                    </div>
                    <div className="col-md-8">
                        <div className="card-body">
                            <h5 className="card-title">News title</h5>
                            <p className="card-text"><small className="text-muted">25/6/21</small></p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
