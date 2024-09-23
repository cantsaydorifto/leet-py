function getTestCases() {
  const arr = document.querySelectorAll(".elfjS pre");
  const functionName = document.querySelector(".mtk11").textContent.trim();

  let res = "";
  arr.forEach((el) => {
    const inputMatch = el.textContent.trim().match(/Input:\s*(.*)/);

    if (inputMatch) {
      let input = inputMatch[1].trim();
      res += `print(Solution().${functionName}(${input}))\n`;
    }
  });
  // navigator.clipboard.writeText(res);
  // console.log("Copied to clipboard");
  return res;
}
getTestCases();

//PASTE THIS IN THE CONSOLE IN A QUESTION PAGE THEN CALL THE FUNCTION, DOES NOT WORK PERFECTLY, BUT NOT BAD
