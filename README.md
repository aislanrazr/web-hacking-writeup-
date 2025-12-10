# Web Hacking — Writeup & Lab

**Autor:** Aislan Guedes  
**Objetivo:** Demonstrar habilidades práticas em segurança ofensiva através de um writeup profissional baseado em avaliação de segurança. Este projeto inclui análises, ambiente de laboratório, ferramentas de apoio e provas de conceito seguras (não exploráveis).

> ⚠️ **Aviso Ético:**  
> Todo o conteúdo deste repositório é para fins educativos. Nenhum payload acionável ou código de ataque real está incluído.  
> Testes de segurança só devem ser realizados com autorização explícita.

---

## 📌 Conteúdo do Repositório
- **REPORT.md** – relatório técnico completo, estruturado em metodologia, achados e evidências.
- **remediation.md** – recomendações de correção e checklist.
- **LAB/** – ambiente vulnerável seguro com Docker (Juice Shop).
- **tools/** – scripts de automação utilizados no processo de varredura.
- **poc/** – provas de conceito seguras e simuladas.
- **assets/** – diagramas e imagens redigidas (adicione suas capturas aqui).
- **LICENSE** – licença MIT padrão.

---

## 🧪 Habilidades Demonstradas
- Reconhecimento e enumeração de diretórios.
- Análise e manipulação de parâmetros client-side.
- Testes de SQL Injection e Command Injection em ambiente seguro.
- Interceptação e modificação de requisições.
- Construção de ambiente vulnerável via Docker.
- Criação de PoCs seguras e reprodutíveis.

---

## 🚀 Como Executar o Ambiente
1. Instale Docker + Docker Compose.
2. Entre na pasta `LAB/`.
3. Execute:
   ```bash
   docker compose up -d
