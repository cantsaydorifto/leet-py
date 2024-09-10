function getTestCases() {
  const arr = document.querySelectorAll(".elfjS > pre");
  let values = "";
  const functionName = document.querySelector(".mtk11").innerHTML;
  arr.forEach((el) => (values += el.innerHTML));
  let res = "";
  values
    .replace(/<strong>.*?<\/strong>/g, "")
    .split("\n")
    .filter((el, idx) => idx % 2 == 0 && el !== "")
    .forEach(
      (el) => (res += "print(Solution()." + functionName + "(" + el + "))\n")
    );
  // navigator.clipboard.writeText(res);
  // console.log("Copied to clipboard");
  return res;
}
getTestCases();

//PASTE THIS IN THE CONSOLE IN A QUESTION PAGE THEN CALL THE FUNCTION, DOES NOT WORK PERFECTLY, BUT NOT BAD
