import { useState } from "react";
import upload from "../assets/upload.png";

export function Upload() {
  const [imagePreview, setImagePreview] = useState(null);

  // Function to handle file selection
  const handleFileChange = (event) => {
    const file = event.target.files[0];

    // Display the selected image
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setImagePreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <>
      <div className="flex p-72">
        <div>
          <h1>Upload Files</h1>
          <p className="w-96">
            Welcome to our secure file upload section. Here, you can easily
            submit suspect images or relevant data for analysis. Our advanced
            Face Detection and Recognition algorithms will swiftly process the
            content, bringing us one step closer to a safer tomorrow.
          </p>
          <ul className="list-disc pl-6">
            Guidelines for Upload:
            <li>
              Ensure images are clear and high-resolution for optimal analysis.
            </li>
            <li>Supported formats: JPEG, PNG, MP4.</li>
            <li>
              For multiple images, consider zipping them into a single file for
              efficiency.
            </li>
          </ul>

          {/* Your file input and image preview */}
          <div className="mt-4">
            <label
              htmlFor="fileInput"
              className="cursor-pointer bg-blue-500 text-white py-2 px-4 rounded"
            >
              Click to Upload Image
            </label>
            <input
              type="file"
              id="fileInput"
              className="hidden"
              onChange={handleFileChange}
            />

            {/* Image preview */}
            {imagePreview && (
              <div className="mt-4">
                <img
                  src={imagePreview}
                  alt="Uploaded Image"
                  className="max-w-full h-auto"
                />
              </div>
            )}
          </div>
        </div>
        <div>
          <img src={upload} alt="Upload Icon" />
        </div>
      </div>
    </>
  );
}
