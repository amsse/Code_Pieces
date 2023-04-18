// Complete the solution so that it returns true if the 
// 1st argument(string) passed in ends with the
// 2nd argument (also a string).
//
// Examples:
//
// solution('abc', 'bc') // returns true
// solution('abc', 'd') // returns false
//
//
//
// SOLUTION:

function solution(str, ending){
    return str.indexOf(ending, str.length - ending.length) !== -1;
  }
  // elemento de pesquisa é 'ending', ponto inicial é 'str.length - ending.length'
  // -1 é quando indexOf() não encontra nada, então diferente de -1 é true

// indexOf() retorna o primeiro índice em que o elemento pode ser
// encontrado no array, retorna -1 caso o mesmo não esteja presente.
// 
// Sintaxe:
//
// array.indexOf(elementoDePesquisa, [pontoInicial = 0])