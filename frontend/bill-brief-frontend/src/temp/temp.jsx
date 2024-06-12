import React from 'react';

const SignIn = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
        <h2 className="text-2xl font-semibold text-center mb-4">Sign In</h2>
        <p className="text-center mb-6">
          Not registered yet? <a href="#" className="text-blue-600">Sign Up</a>
        </p>
        <div className="flex flex-col space-y-4">
          <button className="flex items-center justify-center py-2 px-4 border border-gray-300 rounded-md bg-white text-gray-700 hover:bg-gray-50">
            <img src="github-icon.png" alt="GitHub" className="w-5 h-5 mr-2" />
            Continue with GitHub
          </button>
          <button className="flex items-center justify-center py-2 px-4 border border-gray-300 rounded-md bg-white text-gray-700 hover:bg-gray-50">
            <img src="google-icon.png" alt="Google" className="w-5 h-5 mr-2" />
            Continue with Google
          </button>
        </div>
        <div className="flex items-center justify-center my-4">
          <span className="border-b border-gray-300 w-1/5"></span>
          <span className="mx-2 text-gray-500">or</span>
          <span className="border-b border-gray-300 w-1/5"></span>
        </div>
        <form>
          <div className="mb-4">
            <label htmlFor="email" className="block text-gray-700">Email</label>
            <input
              type="email"
              id="email"
              className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Email address"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="password" className="block text-gray-700">Password</label>
            <input
              type="password"
              id="password"
              className="w-full px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              placeholder="Password"
            />
          </div>
          <button className="w-full py-2 px-4 bg-teal-600 text-white rounded-md hover:bg-teal-700">
            Sign In
          </button>
          <div className="text-center mt-4">
            <a href="#" className="text-blue-600">Forgot password?</a>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignIn;