import React from 'react';


class Header extends React.Component
{
    state={
        isLoggedIn: this.props.isLoggedIn
    }

    toggleLoggedIn=()=>{
        this.setState(prev=>({isLoggedIn:!prev.isLoggedIn}))
    }
    render()
    {
        const {title}=this.props;
        const {count}=this.state;
        return(
        <div className="header">
        <div className="menu" onClick={this.toggleLoggedIn}>
        {
            this.state.isLoggedIn?
            <span>Logout</span>:
            <span>Login</span>
        }
        </div>
        </div>
        );
    }
}

export default Header