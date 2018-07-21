import React from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

export class CollegesList extends React.Component{
    state={
        data:null
    }
    componentDidMount(){
        fetch('http://localhost:8000/apicolleges/')
            .then(response=>response.json())
            .then(responseJson => {console.log(responseJson);this.setState({data:responseJson});})
            .catch(e=>{console.log("Error Occured");});
    }
    render()
    {
        return(
            <Router>
            <div>
                <h2>
                    Colleges List
                </h2>
                {
                    this.state.data ?
                    this.state.data.map(college =>(<p key={college.id}><Link to={"/college/"+college.id}> {college.name},{college.id}</Link></p>))
                        : <p>loading...</p>
                }
            </div>
            </Router>
        );
    }
}

export default CollegesList