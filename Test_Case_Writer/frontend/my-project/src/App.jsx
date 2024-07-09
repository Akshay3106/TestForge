import { useState } from "react";
import AuthHandler from './AuthHandler.jsx';

const App = () => {
  const handleLoginSuccess = () => {
    // Redirect to the home screen
    window.location.href = '/home.html';
  };

  return (
    <div className="bg-banner-image bg-cover h-[100vh]">
      <div className="flex justify-center items-center h-full">
        <div className="lg:w-[450px] bg-white py-20 px-10 rounded-bl-[40px] rounded-se-[40px]">
          <h1 className="text-4xl text-blue-900 text-center mb-6 transition-all">Login</h1>
          <div className="w-full">
            <AuthHandler onLoginSuccess={handleLoginSuccess} />
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;