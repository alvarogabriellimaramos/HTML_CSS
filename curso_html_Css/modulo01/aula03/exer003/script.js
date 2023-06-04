const entrou = () => {
    let texto = document.getElementById('txt-js')
    texto.innerHTML = "<p>JavaScript é uma linguagem de alto nivel,utilizada para crianção de sites e aplicações web,ela é uma linguagem com POO (orientação a objeto)</p>"
    texto.style.boxShadow = '1px 1px 2px 1px black '
}
const saiu = () => {
    let texto = document.getElementById('txt-js')
    texto.innerHTML = ''
    texto.style.boxShadow = '0 0 0 0'
}