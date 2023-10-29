import image from "../assets/1.jpg";
import icon from "../assets/icon.png";

export function Landing() {
  return (
    <div className="container mx-auto p-10 flex flex-col md:flex-row items-center justify-center">
      <div className="md:w-1/2">
        <div className="flex items-center mb-4">
          <img src={icon} alt="Facio Icon" className="w-10 h-10 mr-2" />
          <h1 className="text-4xl font-bold">Facio</h1>
        </div>
        <h3 className="text-2xl mb-4">Start Detection</h3>
        <p className="text-gray-600 mb-6">
          Securing our future: Effortless Face Detection and Recognition for
          Advanced Policing and Counterterrorism. Quickly detect and recognize
          faces from CCTV video streams using our powerful web app.
        </p>
        <button className="bg-[#31F2F2] text-white px-6 py-3 rounded-full hover:bg-[#0E9AA7] transition">
          Get Started
        </button>
      </div>
      <div className="md:w-1/2 mt-6 md:mt-0">
        <img
          src={image}
          alt="Facio Description"
          className="w-full h-auto rounded-lg shadow-lg"
        />
      </div>
    </div>
  );
}