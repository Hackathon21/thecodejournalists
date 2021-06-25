import React from 'react';
import NavStrip from '../components/navigation/NavStrip';
import SearchBar from '../components/navigation/SearchBar';
import Results from '../components/content/Results';
import RelatedNews from '../components/content/RelatedNews';
import 'Assets/sass/main.scss';
import './app.scss';

class App extends React.Component {
    render() {
        return (
            <div style={{ backgroundColor: "#f7f8f8" }}>
                <NavStrip />
                <div className="container-fluid p-4">

                    <div className="row">
                        <div className="col-sm-12 col-md-8 mt-3 mb-3" >
                            <SearchBar />
                        </div>
                        <div className="col-md-4 mt-3 mb-3">
                            <h4>RELATED NEWS</h4>
                        </div>
                    </div>

                    <div className="row">
                        <div className="col-sm-12 col-md-8" >
                            <div style={{ backgroundColor: "#ffffff" }}>
                                <Results />
                            </div>
                        </div>
                        <div className="col-md-4">
                            <div style={{ backgroundColor: "#ffffff" }}>
                                <RelatedNews />
                                <RelatedNews />
                                <RelatedNews />
                                <RelatedNews />
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        )
    }
}

export default App;
