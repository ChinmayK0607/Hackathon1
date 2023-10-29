import servicesImage from "../assets/servicesImage.png";
import { Mail, Phone, Linkedin } from "react-feather";

export function Services() {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="flex flex-col md:flex-row items-center justify-center md:space-x-12">
        <div className="md:w-1/2">
          <h1 className="text-4xl font-bold mb-4">Our Services</h1>
          <p className="text-gray-600 leading-7">
            We offer a variety of services, each designed to enhance security
            and streamline investigative processes. Explore the range of
            services we provide:
          </p>

          {/* List of services */}
          <ul className="list-disc pl-6 text-gray-700 mt-4">
            <li>
              <strong>Face Detection:</strong> Our cutting-edge Face Detection
              technology ensures real-time analysis of live CCTV video streams.
              Swift and accurate, it forms the foundation of our security
              framework, identifying faces with precision.
            </li>
            <li>
              <strong>Face Recognition:</strong> Elevate your investigative
              capabilities with our advanced Face Recognition feature.
              Seamlessly matching faces against a desired input, it expedites
              the identification process, aiding law enforcement in targeting
              suspects efficiently.
            </li>
            <li>
              <strong>Suspect Image Analysis:</strong> Submit suspect images
              through our secure Upload File section. Our sophisticated
              algorithms analyze images with meticulous detail, providing
              valuable insights for investigations.
            </li>
            <li>
              <strong>Secure Data Storage:</strong> Trust is paramount. We offer
              secure data storage, ensuring that sensitive information is
              safeguarded at all times. Our robust encryption measures guarantee
              the confidentiality of stored data.
            </li>
            <li>
              <strong>Technical Support:</strong> Our dedicated support team is
              at your service. From clarifying software features to addressing
              technical concerns, we provide timely assistance to ensure a
              smooth and efficient user experience.
            </li>
            <li>
              <strong>Continuous Innovation:</strong> Technology never stands
              still, and neither do we. Benefit from continuous updates and
              innovations, ensuring your security infrastructure remains at the
              forefront of technological advancement.
            </li>
          </ul>
          <div className="flex items-center mt-6">
            <Mail className="mr-2" size={20} />
            <span>support@facio.com</span>
          </div>
          <div className="flex items-center mt-2">
            <Phone className="mr-2" size={20} />
            <span>+91 xxxxxxxxx99</span>
          </div>
          <div className="flex items-center mt-2">
            <Linkedin className="mr-2" size={20} />
            <span>LinkedIn Profile</span>
          </div>
        </div>
        <div className="md:w-1/2">
          <img
            src={servicesImage}
            alt="Services Image"
            className="w-full h-auto rounded-lg shadow-lg"
          />
        </div>
      </div>
    </div>
  );
}
