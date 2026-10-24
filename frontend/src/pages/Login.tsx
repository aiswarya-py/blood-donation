import { useState } from 'react';

function Login() {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="min-h-screen bg-zinc-950 flex items-center justify-center p-4">
      <div className="w-full max-w-sm bg-black text-white rounded-3xl overflow-hidden shadow-2xl border border-zinc-800 flex flex-col">
        {/* Top branding section */}
        <div className="flex flex-col items-center justify-center px-6 pt-14 pb-8">
          <div className="relative mb-6">
            <div className="absolute inset-0 bg-red-600/40 blur-3xl rounded-full scale-150" />
            <div className="relative w-20 h-20 rounded-2xl bg-zinc-900 border border-red-900/50 flex items-center justify-center text-4xl">
              🩸
            </div>
          </div>
          <h1 className="text-3xl font-bold mb-2">
            Blood <span className="text-red-500">Connect</span>
          </h1>
          <p className="text-gray-400 text-sm">Every drop connects life</p>
        </div>

        {/* Bottom sheet form */}
        <div className="bg-zinc-900 rounded-t-3xl px-8 pt-6 pb-10">
          <div className="w-10 h-1 bg-zinc-700 rounded-full mx-auto mb-7" />

          <h2 className="text-2xl font-bold mb-1">Welcome back</h2>
          <p className="text-gray-400 text-sm mb-7">
            Sign in to your donor or receiver portal
          </p>

          <form className="flex flex-col gap-4">
            <input
              type="email"
              placeholder="Email address"
              className="bg-zinc-800 border border-zinc-700 rounded-full px-5 py-3.5 text-white placeholder-gray-500 focus:outline-none focus:border-red-500 transition"
            />

            <div className="relative">
              <input
                type={showPassword ? 'text' : 'password'}
                placeholder="Password"
                className="w-full bg-zinc-800 border border-zinc-700 rounded-full px-5 py-3.5 pr-12 text-white placeholder-gray-500 focus:outline-none focus:border-red-500 transition"
              />
              <button
                type="button"
                onClick={() => setShowPassword((prev) => !prev)}
                className="absolute right-4 top-1/2 -translate-y-1/2 text-gray-400 hover:text-white"
                aria-label="Toggle password visibility"
              >
                {showPassword ? (
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24" />
                    <line x1="1" y1="1" x2="23" y2="23" />
                  </svg>
                ) : (
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8Z" />
                    <circle cx="12" cy="12" r="3" />
                  </svg>
                )}
              </button>
            </div>

            <div className="text-right">
              <a href="/forgot-password" className="text-sm text-gray-400 hover:text-white">
                Forgot password?
              </a>
            </div>

            <div className="flex items-center gap-3 mt-2">
              <button
                type="button"
                className="w-14 h-14 shrink-0 rounded-full bg-zinc-800 border border-red-900/50 flex items-center justify-center text-red-500 hover:bg-zinc-700 transition"
                aria-label="Biometric login"
              >
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M2 12C2 6.5 6.5 2 12 2a10 10 0 0 1 10 10c0 2-.5 4-1 5" />
                  <path d="M5 10a7 7 0 0 1 14 0v2" />
                  <path d="M8 12v-2a4 4 0 0 1 8 0" />
                  <path d="M12 10v3a6 6 0 0 0 1 3.5" />
                  <path d="M8 16a7 7 0 0 0 1.3 3" />
                </svg>
              </button>
              <button
                type="submit"
                className="flex-1 bg-white text-black font-semibold rounded-full py-3.5 hover:bg-gray-200 transition"
              >
                Log In
              </button>
            </div>
          </form>

          <p className="text-center text-sm text-gray-400 mt-6">
            New to BloodConnect?{' '}
            <a href="/register" className="text-white font-semibold hover:underline">
              Create Account
            </a>
          </p>
        </div>
      </div>
    </div>
  );
}

export default Login;
