import React from "react";
import { useLocation, useHistory } from "@docusaurus/router";
import Swift from "./swift.mdx";
import ObjC from "./obj-c.mdx";

const ContentSwitcher = () => {
  const location = useLocation();
  const history = useHistory();
  const searchParams = new URLSearchParams(location.search);
  const currentTab = searchParams.get("tab") || "swift";

  const setTab = (tab) => {
    searchParams.set("tab", tab);
    history.replace({ search: searchParams.toString() });
  };

  return (
    <div>
      {/* Tab buttons */}
      <div className="flex border-b border-gray-300 mb-4">
        <button
          className={`px-4 py-2 -mb-px text-sm font-medium border-b-2 transition-colors ${
            currentTab === "swift"
              ? "border-blue-500 text-blue-600"
              : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
          }`}
          onClick={() => setTab("swift")}
        >
          Swift
        </button>
        <button
          className={`px-4 py-2 -mb-px text-sm font-medium border-b-2 transition-colors ${
            currentTab === "objc"
              ? "border-blue-500 text-blue-600"
              : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
          }`}
          onClick={() => setTab("objc")}
        >
          Objective-C
        </button>
      </div>

      {/* Content */}
      <div key={currentTab} className="p-2">
        {currentTab === "swift" && <Swift />}
        {currentTab === "objc" && <ObjC />}
      </div>
    </div>
  );
};

export default ContentSwitcher;
