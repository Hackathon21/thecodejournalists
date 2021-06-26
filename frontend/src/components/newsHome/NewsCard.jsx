import React, { Component } from 'react'

export default class NewsCard extends Component {

    componentDidMount(){
        fetch("https://jsonplaceholder.typicode.com/users")
        .then(response => {
            console.log(response.data);
        })
        .catch(err => {
            console.error(err);
        });
    }

    render() {
        const {size} = this.props;        
        
        return (
            <div className="card mb-2" style={{width: size}}>
                
                <div className="card-body">
                    <a href="#" className="btn btn-primary btn-sm mb-3">Trending</a>
                    <h5 className="card-title">News Title</h5>
                    <img src="..." className="card-img-top" alt="..."/>
                    <p className="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                    
                </div>
            </div>
        )
    }
}
