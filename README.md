# IHC – Loja Online / Projeto de Interfaces Homem-Computador

Este repositório contém o projeto **IHC** — uma loja online conceptual, desenvolvido no âmbito de Interfaces Homem-Computador. O objetivo é demonstrar a tua capacidade de idealização, concepção de interface e prototipagem, assim como organização de requisitos e análise crítica.

---

## Índice

1. [Visão Geral](#visão-geral)  
2. [Objetivos do Projeto](#objetivos-do-projeto)  
3. [Conteúdo do Repositório](#conteúdo-do-repositório)  
4. [Funcionalidades Planeadas / Implementadas](#funcionalidades-planeadas--implementadas)  
5. [Tecnologias & Ferramentas](#tecnologias--ferramentas)  
6. [Processo de Desenvolvimento](#processo-de-desenvolvimento)  
7. [Aprendizagens & Pontos Fortes](#aprendizagens--pontos-fortes)  
8. [Como Usar / Explorar](#como-usar--explorar)  
9. [Possíveis Extensões Futuras](#possíveis-extensões-futuras)  
10. [Autores / Colaboradores](#autores--colaboradores)

---

## Visão Geral

O projeto **IHC** simula uma loja online, com foco em usabilidade, experiência do utilizador (UX), interface visual (UI), e estrutura funcional. Inclui desde fases iniciais de planeamento até prototipagem funcional e análise crítica.

---

## Objetivos do Projeto

- Entender e aplicar boas práticas de interfaces humano-computador: usabilidade, acessibilidade, layout, navegação, feedback ao utilizador.  
- Estruturar o ciclo de desenvolvimento: definição de contexto, requisitos, protótipos (baixo e alto detalhe), refinamento e análise.  
- Demonstrar capacidade de prototipar uma interface funcional (mesmo que não implementada como produto real).  
- Documentar todo o processo num logbook / relatório técnico para evidenciar o raciocínio.

---

## Conteúdo do Repositório

| Pasta / Ficheiro | Descrição |
|------------------|-----------|
| `stage0_planning/` | Planeamento inicial do projeto: cronograma, objetivos, escopo. |
| `stage1_context/` | Contexto do projeto: análise de mercado, utilizadores alvo, personas, cenário de uso. |
| `stage2_requirements/` | Requisitos funcionais e não-funcionais. |
| `stage3_low_fidelity/` | Protótipos de baixa fidelidade (sketches, wireframes). |
| `stage4_functional_prototype/` | Protótipo funcional / de alta fidelidade, com interatividade (dependendo do que estiver implementado). |
| `stage5_discussion_and_refinement/` | Discussão dos resultados do protótipo, feedback, melhorias. |
| `stage6_critical_analysis/` | Análise crítica: o que funcionou, o que falhou, lições aprendidas. |
| `LogBook/` ou `hci_logbook.md` | Registo contínuo do progresso, decisões tomadas, problemas encontrados. |

---

## Funcionalidades Planeadas / Implementadas

- Visualização de produtos (categorias, descrições, imagens)  
- Sistema de pesquisa / filtragem por características  
- Adicionar ao carrinho, ver carrinho, remover itens  
- Processo de checkout simulado  
- Feedback visual ao utilizador para ações (ex: confirmação, erro)  
- Responsividade (adaptar a dispositivos móveis)  
- Cuidados de acessibilidade (contraste de cores, navegação teclado, etiquetas…)

---

## Tecnologias & Ferramentas

- HTML  
- CSS  
- JavaScript  
- Ferramentas de design ou prototipagem (ex: Figma, Adobe XD, Sketch)  
- GitHub 

---

## Processo de Desenvolvimento

1. Planeamento / definição de escopo  
2. Investigação de contexto / análise de utilizadores  
3. Levantamento de requisitos  
4. Protótipos de baixa fidelidade  
5. Protótipo funcional  
6. Feedback, refinamento  
7. Análise crítica  

---

## Aprendizagens & Pontos Fortes

- Tomada de decisões de design fundamentadas  
- Capacidade de organizar um projeto de interface de ponta a ponta  
- Trabalhar com feedback e iterar versões  
- Atenção à usabilidade, acessibilidade, boas práticas de interface  
- Comunicação de ideias através de protótipos  

---

# Como Usar / Explorar


1. Create the virtual environment:
```bash
python3 -m venv venv
```
2. Activate the virtual environment (Every time you open a new terminal you need to do this to make the virtual environment the default Python interpreter of this shell):
```bash
source venv/bin/activate
```
or (Windows):
```bash
.\venv\Scripts\activate.ps1
```

3. Install the requirements:
```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
./run.sh app_sec <PORT>
```

&emsp;&emsp;In Windows use instead:

```bash
.\run.bat app_sec <PORT>
```
5. Access the website:

```bash
http://127.0.0.1:<PORT>
```

6. To generate the database you need to access the following link:

```bash
/generate/all
```
