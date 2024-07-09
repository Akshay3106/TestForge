import React, { useState } from 'react';
import { MdEmail, MdVisibility, MdVisibilityOff } from 'react-icons/md'; // Import visibility icons along with email icon
import { RiLockPasswordLine } from 'react-icons/ri'; // Import for lock icon

// Dummy user data for demonstration purposes
const USERS = [
  {
    email: 'user@example.com',
    password: 'password123',
  },
];

const AuthHandler = ({ onLoginSuccess }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false); // State to toggle password visibility

  const handleLogin = (e) => {
    e.preventDefault();
    // Verify user credentials
    const user = USERS.find((user) => user.email === email && user.password === password);
    if (user) {
      onLoginSuccess();
    } else {
      alert('Invalid credentials');
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <form onSubmit={handleLogin}>
      <div className="bg-gray-200 flex items-center gap-5 my-4 p-4 rounded">
        <MdEmail className="text-gray-500" /> {/* Email icon */}
        <input
          type="email"
          className="bg-transparent border-none outline-none flex-grow transform transition duration-300 ease-in-out hover:scale-105"
          placeholder="Your Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
      </div>
      <div className="bg-gray-200 flex items-center gap-5 my-4 p-4 rounded relative">
        <RiLockPasswordLine className="text-gray-500" /> {/* Lock icon */}
        <input
          type={showPassword ? "text" : "password"}
          className="bg-transparent border-none outline-none flex-grow transform transition duration-300 ease-in-out hover:scale-105"
          placeholder="Your Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="button" onClick={togglePasswordVisibility} className="absolute right-4">
          {showPassword ? <MdVisibilityOff className="text-gray-500" /> : <MdVisibility className="text-gray-500" />}
        </button>
      </div>
      <div className="flex flex-col items-center gap-4 mt-10">
        <a href="#" className="text-blue-900 hover:underline">Forgot Password?</a>
        <button type="submit" className="text-xl text-white py-2 w-36 rounded-3xl bg-blue-900 transform transition duration-300 ease-in-out hover:scale-105 hover:bg-blue-800">
          Login
        </button>
      </div>
    </form>
  );
};

export default AuthHandler;