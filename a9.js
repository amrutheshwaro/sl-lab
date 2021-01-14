calculate = function() {
    const sentence = document.getElementById("sentence").value;
    if (sentence === "") {
        alert("Enter a sentence in the text box");
    } else {
        const words = sentence.split(' ');
        var longestWord = "";
        for (const word of words) {
            if (word.length > longestWord.length) {
                longestWord = word;
            }
        }
        document.getElementById('longestWord').innerHTML = "Longest word: " + longestWord;
    }
}