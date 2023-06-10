import React, { useState } from 'react';

const App = () => {
  const [selections, setSelections] = useState({
    option1: '',
    option2: '',
    option3: '',
    option4: '',
  });

  const handleSelectionChange = (event) => {
    const { name, value } = event.target;
    setSelections((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleSubmit = () => {
    // Send API request to the Flask backend using selections object
    // You can use libraries like axios to make the API call
    // For example: axios.post('/api/your-endpoint', selections)
    // Handle the response accordingly
  };

  return (
    <div className="App">
      <div className="welcome-message">
        <h1>Hi! Select the settings below and click the 'Generate Workout' button to get started!</h1>
      </div>
      <div className="dropdowns">
        <select name="option1" value={selections.option1} onChange={handleSelectionChange}>
          <option value="">Days per week</option>
          <option value="option1Value1">Option 1 Value 1</option>
          <option value="option1Value2">Option 1 Value 2</option>
          {/* Add more options as needed */}
        </select>
        <select name="option2" value={selections.option2} onChange={handleSelectionChange}>
          <option value="">Time per Session</option>
          <option value="option2Value1">Option 2 Value 1</option>
          <option value="option2Value2">Option 2 Value 2</option>
          {/* Add more options as needed */}
        </select>
        <select name="option3" value={selections.option3} onChange={handleSelectionChange}>
          <option value="">Fitness Goal</option>
          <option value="option3Value1">Option 3 Value 1</option>
          <option value="option3Value2">Option 3 Value 2</option>
          {/* Add more options as needed */}
        </select>
        <select name="option4" value={selections.option4} onChange={handleSelectionChange}>
          <option value="">Gym Experience</option>
          <option value="option4Value1">Option 4 Value 1</option>
          <option value="option4Value2">Option 4 Value 2</option>
          {/* Add more options as needed */}
        </select>
      </div>
      <button className="submit-button" onClick={handleSubmit}>
        Generate Workout
      </button>
    </div>
  );
};

export default App;
