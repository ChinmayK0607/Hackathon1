import support from "../assets/support.png";
import { Mail, Phone, Linkedin } from "react-feather";

export function Support() {
  return (
    <div className="container mx-auto px-4 py-16">
      <div className="flex flex-col md:flex-row items-center justify-center md:space-x-12">
        <div className="md:w-1/2">
          <h1 className="text-4xl font-bold mb-4">Support</h1>
          <p className="text-gray-600 leading-7">
            Please submit your detailed query via our support email id or
            toll-free contact number mentioned below, and our team will
            diligently review and respond to your request. We strive to provide
            timely and effective solutions to ensure your experience with Facio
            remains optimal. Our support team operates during standard business
            hours [9am to 7pm IST]. Requests received outside of these hours
            will be addressed promptly on the next business day.
          </p>
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
            <span>LinkedIn </span>
          </div>
        </div>
        <div className="md:w-1/2">
          <img
            src={support}
            alt="Support Image"
            className="w-full h-auto rounded-lg shadow-lg"
          />
        </div>
      </div>
    </div>
  );
}
