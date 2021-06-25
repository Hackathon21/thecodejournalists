import React, { Component } from 'react'

export default class Results extends Component {
    render() {
        return (
            <div className="row ">
                <div className="col-6">
                    <div className="container">
                        <h5 className="mt-3 fw-bold">RESULTS</h5>
                        <h6 className="fs-5 fw-bold">ML Analyser Results:</h6>
                        <button type="button" className="btn btn-success btn-rounded">Real</button>
                        <span> OR </span>
                        <button type="button" className="btn btn-danger btn-rounded">Fake</button>

                        <p className="fs-5 fw-bold mb-1 mt-3">Users Trust Votes: 2</p>
                        <p className="fs-5 fw-bold mt-1 mb-1">No of related article : 4</p>
                    </div>
                </div>
                <div className="col-6">
                    <div className="container">
                        <h5 className="mt-3 fw-bold">PIE CHART (ML Results)</h5>
                        <div >
                            <div className="p-5 mb-1 bg-dark text-white rounded"
                                style={{ height: "165px", width: "220px" }}
                            >PIE CHART HERE</div>
                            {/*PIE CHART HERE*/}
                        </div>
                    </div>
                </div>


                <div className="container">
                    <div className="ms-4 mt-3">
                        <h5 className="fw-bold">WORD CLOUD</h5>
                        {/*WORD CLOUD HERE */}
                        <img className="img-fluid" src="https://crimetechweekly.com/wp-content/uploads/2017/07/bigdatawordmap-1264x736.jpg" alt="" />
                    </div>
                    <div></div>
                </div>

            </div>
        )
    }
}
