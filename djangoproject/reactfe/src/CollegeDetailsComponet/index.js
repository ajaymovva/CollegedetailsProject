import React from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

export class CollegeDetails extends React.Component{

    state={
        data:null
    }
    componentDidMount(){
        fetch('http://localhost:8000/apicollegesmodify/'+this.props.match.params.id+'/student/')
            .then(response=>response.json())
            .then(responseJson => {console.log(responseJson);this.setState({data:responseJson});})
            .catch(e=>{console.log("Error Occured");});
    }
    render()
    {
        return(
            <div>
                <h2>
                    Students List
                </h2>
                {
                    this.state.data ?
                    this.state.data.map(college =>(<p>{college.name},{college.email},{college.db_folder}</p>))
                        : <p>loading...</p>
                }
            </div>
        );
    }
}

export default CollegeDetails


