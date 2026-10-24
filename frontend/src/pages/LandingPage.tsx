function LandingPage() {
  return (
    <div className="min-h-screen bg-black text-white flex flex-col font-sans">
      <header className="flex justify-between items-center px-12 py-6 border-b border-white">
        <div className="text-xl font-bold tracking-wide">🩸 BloodConnect</div>
        <nav className="flex items-center gap-6">
          <a href="/login" className="text-sm hover:underline">
            Login
          </a>
          <a
            href="/register"
            className="text-sm border border-white px-4 py-2 rounded hover:bg-white hover:text-black transition"
          >
            Register
          </a>
        </nav>
      </header>

      <main className="flex-1 flex flex-col items-center justify-center text-center px-6 py-20">
        <h1 className="text-5xl md:text-6xl font-bold tracking-tight mb-4">
          Every Drop Counts.
        </h1>
        <p className="max-w-xl text-lg text-gray-300 mb-9 leading-relaxed">
          Connect blood donors with people in need, quickly and reliably.
          Join our network and help save lives.
        </p>
        <div className="flex gap-4">
          <a
            href="/register"
            className="px-8 py-3.5 rounded font-semibold bg-white text-black hover:bg-gray-300 transition"
          >
            Become a Donor
          </a>
          <a
            href="/donors"
            className="px-8 py-3.5 rounded font-semibold border border-white text-white hover:bg-white hover:text-black transition"
          >
            Find Donors
          </a>
        </div>
      </main>

      <section className="flex justify-center gap-12 flex-wrap px-12 py-16 border-t border-white">
        <div className="max-w-xs text-center">
          <h3 className="text-xl font-semibold mb-2">Register</h3>
          <p className="text-gray-300 text-sm leading-relaxed">
            Create an account and set up your donor profile in minutes.
          </p>
        </div>
        <div className="max-w-xs text-center">
          <h3 className="text-xl font-semibold mb-2">Get Matched</h3>
          <p className="text-gray-300 text-sm leading-relaxed">
            Hospitals and patients find donors by blood group and city.
          </p>
        </div>
        <div className="max-w-xs text-center">
          <h3 className="text-xl font-semibold mb-2">Save Lives</h3>
          <p className="text-gray-300 text-sm leading-relaxed">
            Respond to requests near you and make a real difference.
          </p>
        </div>
      </section>

      <footer className="text-center py-6 border-t border-white text-gray-500 text-xs">
        <p>&copy; {new Date().getFullYear()} BloodConnect. All rights reserved.</p>
      </footer>
    </div>
  );
}

export default LandingPage;
