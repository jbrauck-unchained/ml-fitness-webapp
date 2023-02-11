const Navbar = () => {
    return ( 
        <nav className="navbar">
            <h1> Workout </h1>
            <div className="links">
                <a href="/">Home</a>
                <a href="/about" style={{
                    color: "white",
                    backgroundColor: '#f1356d',
                    borderRadius:'8px'
                }}>About Us</a>
            </div>
        </nav>
     );
}
 
export default Navbar;