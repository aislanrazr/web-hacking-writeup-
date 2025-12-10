# Recomendações de Remediação

## SQL Injection
- Use consultas parametrizadas (prepared statements) para todas as interações com banco.
- Implementar ORM com proteção contra injection ou sanitização de entrada.
- Revisão de código (SAST) e testes automatizados para entradas críticas.
- Monitoramento e alertas para padrões de login anômalos.

## Controle de parâmetros client-side
- Nunca confiar em controles do cliente. Autorize ações no servidor.
- Validar e checar o estado do recurso no backend antes de executar ações (ex.: promo válido? pertence ao usuário?).

## Command injection
- Evitar execução de comandos do sistema quando possível. Usar bibliotecas/APIs.
- Se necessário, use listas brancas estritas (whitelists) e evite passar strings diretamente ao shell.
- Rodar processos com menor privilégio possível (principle of least privilege).

## Hardening e boas práticas
- WAF e rate limiting.
- Logging e resposta a incidentes.
- Testes de penetração regulares e integração do security as code.
