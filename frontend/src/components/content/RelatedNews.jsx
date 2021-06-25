import React, { Component } from 'react'

export default class RelatedNews extends Component {
    render() {
        return (
            <div>
                <div className="card mb-3 border-0" >
                    <div className="row no-gutters">
                        <div className="col-md-4">
                            <img src="https://img.icons8.com/plasticine/100/000000/image.png" className="card-img" alt="..."/>
                        </div>
                        <div className="col-md-8">
                            <div className="card-body">
                                <h5 className="card-title">Article Heading</h5>
                                <p className="card-text">This is the excerpt of the article...</p>
                                <p className="card-text"><small className="text-muted"><a href="./">Original Source Site</a></small></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}
