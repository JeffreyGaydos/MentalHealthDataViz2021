import './BarGraph1.css';
import { Component } from 'react';
import { render } from 'react-dom';

class BarGraph1 extends Component {
    
    constructor(props, context) {
        super(props);
        this.state = {
            address: "",
            addressLoading: true,
            error: false,
            results: {},
        };
    }
    
    
    getData() {
        console.log("This works");
        fetch('http://localhost:8000/responses/list', {
                method: "GET",
                headers: { "Content-Type": "application/json", },
            }).then(response => response.json()).then(data => {
                console.log("Success:", data);
                this.setState({
                    results: data,
                    error: false,
                    addressLoading: false,
                })
            }).catch((error) => {
                console.error("Error:", error);
                this.setState({ error: true, })
            });
    }

    componentDidMount()  {   
        this.getData();
    }

    render() {
    return (    
        <div className="BarGraph">
            <script type="text/javascript">
             <p>{this.state.results[0]}</p>
            </script>
        Bar Graph
        </div>
    );
    }
}

export default BarGraph1;
