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
      <button
        className={`switcher-button ${currentTab === "swift" ? "active" : ""}`}
        onClick={() => setTab("swift")}
      >
        Swift
      </button>
      <button
        className={`switcher-button ${currentTab === "objc" ? "active" : ""}`}
        onClick={() => setTab("objc")}
      >
        Objective-C
      </button>
      <div key={currentTab}>
        {currentTab === "swift" && <Swift />}
        {currentTab === "objc" && <ObjC />}
      </div>
    </div>
  );
};

export default ContentSwitcher;
