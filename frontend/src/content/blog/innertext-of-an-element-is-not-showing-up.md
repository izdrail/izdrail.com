---
title: How to fix inner text of an element is not showing up
img: /assets/blog/data-visualization-with-d3.png
description: Learn how to visualize your data with the power of D3.
tags:
  - Tutorial
  - Javascript
  - Issue
  - Learn
---


## Understanding innerText in Javascript

If you’re working with _contentEditable_ elements in React and using hooks like _useRef()_, you might encounter a puzzling situation: _innerText logs correctly_ in the console but doesn’t appear in alerts. 
Let’s dive into the possible reasons and solutions for this behavior, with a focus on debugging effectively.

### Problem Overview

#### Code Example
Here's a common implementation that might cause issues:
```aiignore
import React, { useRef } from 'react';  

export default function Input() {  
  const inputRef = useRef();  

  const showText = () => {  
    console.log("text: ", inputRef.current.innerText);  
    alert("text: ", inputRef.current.innerText);  
  };  

  return (  
    <>  
      <div ref={inputRef} contentEditable="true" suppressContentEditableWarning={true} />  
      <button onClick={showText}>Show text</button>  
    </>  
  );  
}  
```

## How to fix
There are several solutions to this issue:

1. Use Template Literals:

```aiignore
const showText = () => {
  alert(`text: ${inputRef.current.innerText}`);
};
```
2. Use textContent Instead:

```aiignore
const showText = () => {
  alert("text: " + inputRef.current.textContent);
};

```

3. Add State Management:
```aiignore
**const [text, setText] = useState('');

const showText = () => {
  const currentText = inputRef.current.innerText;
  setText(currentText);
  alert("text: " + currentText);
};**
```


## Why It Happens
The issue often occurs because:
1. Alert concatenation might not properly convert the innerText to a string
2. The reference might not be fully updated when the alert is called
3. React's synthetic events and state updates can interfere with direct DOM manipulation


## Best Practices
Always verify that your ref is properly initializedConsider using controlled components instead of refs when possibleUse state management for better predictabilityAdd error handling for cases where the ref might be null