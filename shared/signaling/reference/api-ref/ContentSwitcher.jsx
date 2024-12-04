import React, { useState } from 'react';
import Swift from './swift.mdx';
import ObjC from './obj-c.mdx';

const ContentSwitcher = () => {
  const [selected, setSelected] = useState('swift');

  return (
    <div>
      <button
        className={`switcher-button ${selected === "swift" ? "active" : ""}`}
        onClick={() => setSelected("swift")}
      >
        Swift
      </button>
      <button
        className={`switcher-button ${selected === "objc" ? "active" : ""}`}
        onClick={() => setSelected("objc")}
      >
        Objective-C
      </button>
      <div>
        {selected === 'swift' && <Swift />}
        {selected === 'objc' && <ObjC />}
      </div>
    </div>
  );
};

export default ContentSwitcher;
