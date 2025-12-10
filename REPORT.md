# Relatório Técnico — Web Hacking

**Data do teste:** 05/12/2025  
**Responsável:** Aislan Guedes

## 1. Escopo
- Aplicação alvo  — análise focada em autenticação, recursos de promoções e endpoint de análise de domínio.

## 2. Sumário executivo
Foram identificadas falhas de severidade variada que podem levar à exposição de dados, geração de vouchers indevidos e execução remota de comandos em um ambiente vulnerável. As evidências foram redigidas para esta publicação pública.

## 3. Achados (priorizados)
### A. Injection SQL — Área de login (ALTA)
**Impacto:** bypass de autenticação / acesso administrativo.  
**Recomendação:** usar consultas parametrizadas (prepared statements); aplicar WAF; limitar tentativas de login.

### B. Parmetro client-side control (MÉDIO)
**Impacto:** campo oculto `promo` pode ser ativado no cliente permitindo criação/uso indevido de vouchers.  
**Recomendação:** validar todos os parâmetros no servidor; aplicar verificação de autorização.

### C. Command injection (ALTA) — Endpoint de teste de domínio
**Impacto:** execução remota de comandos como usuário do processo web.  
**Recomendação:** não usar concatenação direta de entradas em chamadas de sistema; usar APIs seguras (bibliotecas) e sanitização estrita.

## 4. Metodologia
- Enumeração de diretórios (ferramentas automatizadas + manual)
- Inspeção de front-end para campos ocultos
- Interceptação de requisições (Burp / proxy)
- Testes em ambiente controlado

## 5. Provas / Logs
- Arquivos em `assets/screenshots/` (todas as imagens redigidas para remover dados sensíveis)
- PoCs simuladas em `poc/` (simulam comportamento sem executar comandos no host real)

## 6. Conclusão
As vulnerabilidades demonstram falta de validação no servidor e práticas inseguras de desenvolvimento. Recomenda-se ciclo de correção imediato para itens de criticidade alta.

