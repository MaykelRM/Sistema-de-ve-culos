# Sistema de Cadastro de Veículos

## 📋 Descrição
Este é um programa em Python para gerenciar diferentes tipos de veículos (carros e motos). Ele utiliza conceitos de **Programação Orientada a Objetos (POO)**, como herança e sobrescrita de métodos, para criar um sistema organizado e funcional.

O programa possibilita:
- Cadastrar veículos com informações como marca, modelo, ano, capacidade do tanque e consumo médio.
- Diferenciar entre carros e motos, adicionando atributos específicos a cada tipo.
- Calcular a autonomia de cada veículo com base na capacidade do tanque e no consumo médio.
- Exibir as informações detalhadas de todos os veículos cadastrados.

## 🛠️ Estrutura do Projeto
O projeto está organizado da seguinte forma:
- **`main.py`**: Arquivo principal que contém o fluxo do programa e interage com o usuário.
- **`veiculo.py`**: Arquivo que define a classe base `Veiculo` e suas subclasses `Carro` e `Moto`.
- **`README.md`**: Arquivo com a documentação do projeto.

## 🚀 Funcionalidades
1. **Cadastrar Veículo**: Insira as informações básicas do veículo, como marca, modelo, ano, capacidade do tanque, consumo médio e atributos específicos (quantidade de portas ou cilindradas).
2. **Exibir Veículos**: Liste todos os veículos cadastrados, mostrando suas informações detalhadas e autonomia.
3. **Sair**: Encerre o programa.

## 📦 Como Executar o Projeto
1. Certifique-se de ter o [Python](https://www.python.org/) instalado em sua máquina.
2. Clone o repositório:
3. Navegue até o diretório do projeto:
4. Execute o programa:

## 📚 Exemplo de Uso
### Menu Principal:
```
1. Cadastrar veículo
2. Exibir todos os veículos
3. Sair
Escolha uma opção:
```

### Exemplo de Cadastro de Carro:
```
Escolha uma opção: 1
Carro ou moto: Carro
Qual a marca: Toyota
Qual o modelo: Corolla
Qual o ano do veículo: 2020
Capacidade do tanque (litros): 50
Consumo médio (km/l): 12
Quantidade de portas: 4
Veículo cadastrado com sucesso!
```

### Exemplo de Cadastro de Moto:
```
Escolha uma opção: 1
Carro ou moto: Moto
Qual a marca: Honda
Qual o modelo: CG 160
Qual o ano do veículo: 2019
Capacidade do tanque (litros): 16
Consumo médio (km/l): 35
Cilindradas: 160
Veículo cadastrado com sucesso!
```

### Exemplo de Exibição de Veículos:
```
Escolha uma opção: 2
--- Veículos Cadastrados ---
Carro:
Marca: Toyota, Modelo: Corolla, Ano: 2020
Capacidade do Tanque: 50L, Consumo Médio: 12 km/L
Quantidade de Portas: 4
Autonomia: 600 km

Moto:
Marca: Honda, Modelo: CG 160, Ano: 2019
Capacidade do Tanque: 16L, Consumo Médio: 35 km/L
Cilindradas: 160
Autonomia: 560 km
```

## 📂 Estrutura de Arquivos
```
sistema_cadastro_veiculos/
│
├── main.py        # Arquivo principal do programa
├── veiculo.py     # Classe Veiculo e suas subclasses Carro e Moto
└── README.md      # Documentação do projeto
```

## 🤝 Contribuições
Sinta-se à vontade para contribuir com este projeto. Para isso:
1. Faça um fork do repositório.
2. Crie uma branch para suas alterações:
   ```bash
   git checkout -b minha-feature
   ```
3. Faça o commit das alterações:
   ```bash
   git commit -m 'Adicionei uma nova funcionalidade'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---
