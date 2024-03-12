<!DOCTYPE html>
<html>
<head>
    <title>Soma de Valores</title>
    <script>
        function calcularSoma() {
            // Obtém os valores dos campos de entrada
            var numero1 = parseFloat(document.getElementById("numero1").value);
            var numero2 = parseFloat(document.getElementById("numero2").value);

            // Calcula a soma dos números
            var soma = numero1 + numero2;

            // Exibe o resultado
            document.getElementById("resultado").innerHTML = "A soma de " + numero1 + " e " + numero2 + " é: " + soma;
        }
    </script>
</head>
<body>
    <h2>Soma de Valores</h2>
    <label for="numero1">Digite o primeiro número:</label>
    <input type="text" id="numero1"><br><br>
    <label for="numero2">Digite o segundo número:</label>
    <input type="text" id="numero2"><br><br>
    <button onclick="calcularSoma()">Calcular Soma</button><br><br>
    <div id="resultado"></div>
</body>
</html>
