 import React, {  Component } from 'react';
 import NewsCard from './NewsCard';

export default class NewsHome extends Component {
    state = {
        title: '',
        description:'',
        url:'',
        publishDate: ''
    };
    
    render() {
        
        return (
            <div className="container">
                <div className="row mt-3 mb-3">
                    <div className="col-6">
                        <NewsCard size="25rem"/>
                    </div>
                    <div className="col-6">
                        <NewsCard size="25rem"/>
                    </div>
                </div>

                <div className="row">
                    <div className="col-4">
                        <NewsCard size="15rem"/>
                    </div>
                    <div className="col-4">
                        <NewsCard size="15rem"/>
                    </div>
                    <div className="col-4">
                        <NewsCard size="15rem"/>
                    </div>
                </div>

                <div className="row mt-3 mb-3">
                    <div className="col-6">
                        <NewsCard size="25rem"/>
                    </div>
                    <div className="col-6">
                        <NewsCard size="25rem"/>
                    </div>
                </div>
                
            </div>
        )
    }
}


//ISSUE
// componentDidMount(){
        
    //     fetch("https://bing-news-search1.p.rapidapi.com/news/trendingtopics?count=10&safeSearch=Off&textFormat=Raw&cc=IN&setLang=EN", {
    //         "method": "GET",
    //         "headers": {
    //             "x-bingapis-sdk": "true",
    //             "x-rapidapi-key":"7b96adde4fmsha12e5b98e0c08bdp158387jsn30a26b09752e",
    //             "x-rapidapi-host": "bing-news-search1.p.rapidapi.com",
    //             "Access-Control-Allow-Origin":"*",
    //             "Access-Control-Allow-Headers":"*"
    //         },
    //         "mode":"cors" 
    //     })
    //     .then(response => {
    //         console.log(response);
    //     })
    //     .catch(err => {
    //         console.error(err);
    //     });


    //         // this.setState({
    //         //     title: data.title     
    //         // })
           
    // }
