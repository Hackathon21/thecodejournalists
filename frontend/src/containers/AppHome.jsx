import React, { Component } from 'react';
import 'Assets/sass/main.scss';
import './app.scss';
import NewsHome from '../components/newsHome/NewsHome';
import LiveSearch from '../components/navigation/LiveSearch';
import Posts from '../components/posts/Posts';

class AppHome extends Component {
    render() {
        return (
            <div className="row">
                <div className="col-8">
                    <NewsHome/>
                </div>
                <div className="col-4">
                    <div className="container">
                    <LiveSearch/>
                    <Posts/>
                    </div>
                </div>
                
            </div>
        )
    }
}

export default AppHome;