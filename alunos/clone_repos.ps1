# Clona todos os repositorios listados em alunos.md para dentro da pasta alunos/
$ErrorActionPreference = "Continue"

$repos = @(
    "https://github.com/Erikmfp/Computa-o-grafica_Erik-marcio-",
    "https://github.com/CastroRic/Computa-o-Gr-fica",
    "https://github.com/jotinhalocobr/Computacao-Grafica",
    "https://github.com/csmedeiros/computacao-visual",
    "https://github.com/Alexepddeoliveira/ComputacaoGrafica2026.2",
    "https://github.com/mlutegar/CG_26.2_8001",
    "https://github.com/IgorMariano25/AC-Computacao-grafica",
    "https://github.com/jpgiovanelli/ibmec.computacao-grafica",
    "https://github.com/rfdnnr/Computacao-Grafica",
    "https://github.com/BeMascarenhasM/Aula-de-computacao_Grafica",
    "https://github.com/andreccoelho/andre_CG_26.2_8001",
    "https://github.com/Marcio202302986072/AC-1---Marcio-Moreira-do-Nascimento-Filho",
    "https://github.com/bernardp112/Computacao_Grafica",
    "https://github.com/marceufilho/Marceu_CG_26.2_8001",
    "https://github.com/vitorsossa/Ac_Computacao_grafica"
)

$destino = Join-Path $PSScriptRoot "repos"
New-Item -ItemType Directory -Path $destino -Force | Out-Null

foreach ($repo in $repos) {
    $nome = ($repo -split "/")[-1]
    $caminho = Join-Path $destino $nome

    if (Test-Path $caminho) {
        Write-Host "[SKIP] $nome ja existe, atualizando (git pull)..." -ForegroundColor Yellow
        git -C $caminho pull
    } else {
        Write-Host "[CLONE] $repo" -ForegroundColor Cyan
        git clone $repo $caminho
    }
}

Write-Host "Concluido." -ForegroundColor Green
