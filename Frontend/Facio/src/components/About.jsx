import aboutus from "../assets/aboutus.png";
import mission from "../assets/ourmission.png";

export function About() {
  return (
    <div className="container mx-auto px-4 py-16">
      {/* About Us Section */}
      <div className="flex flex-col md:flex-row items-center justify-center md:space-x-12 mb-12">
        <div className="md:w-1/2 mb-8 md:mb-0">
          <img src={aboutus} alt="About Us" className="rounded-lg shadow-lg" />
        </div>
        <div className="md:w-1/2">
          <h2 className="text-4xl font-bold mb-4">About Us</h2>
          <p className="text-gray-600 leading-7">
            Facio is a cutting-edge web application that utilizes facial
            recognition technology to identify suspects and criminals. Designed
            as a powerful tool for law enforcement agencies, it enables the
            identification and tracking of criminals. Additionally, it empowers
            the general public to identify and report suspicious individuals.
          </p>
        </div>
      </div>

      {/* Our Mission Section */}
      <div className="flex flex-col md:flex-row-reverse items-center justify-center md:space-x-12">
        <div className="md:w-1/2 mb-8 md:mb-0">
          <img
            src={mission}
            alt="Our Mission"
            className="rounded-lg shadow-lg"
          />
        </div>
        <div className="md:w-1/2">
          <h2 className="text-4xl font-bold mb-4">Our Mission</h2>
          <p className="text-gray-600 leading-7">
            At Facio, our mission is to leverage advanced facial recognition
            technology to enhance public safety. We aim to provide law
            enforcement with a powerful tool for crime prevention and
            resolution. By enabling the community to actively participate in
            identifying and reporting criminals, we strive towards creating a
            safer and more secure society.
          </p>
        </div>
      </div>
    </div>
  );
}
