import { useState } from "react";

const Home = () => {

    const [name, setName] = useState('mario')

    const handleClick = () => {
        setName('luigi');
    }


    return ( 
        <div className="home">
            <h2>Homepage</h2>
            <p> { name } </p>
            <button onClick={handleClick}>Click here</button>
        </div>
     );
}
 
export default Home;
