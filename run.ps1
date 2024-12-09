# Nome dell'immagine e del container
$imageName = "python-streamlit-app"
$containerName = "streamlit-app"

# Abilita il logging colorato
Write-Host "`nStarting Python Application in Podman..." -ForegroundColor Green

# Controlla che Podman sia disponibile
Write-Host "Controllo della connessione a Podman..." -ForegroundColor Cyan
try {
    $podmanVersion = podman --version
    if (-Not $podmanVersion) {
        throw "Podman non è installato o non è configurato nel PATH."
    }
    Write-Host "Podman rilevato: $podmanVersion" -ForegroundColor Green
} catch {
    Write-Host "Errore: Podman non è disponibile. Assicurati che sia installato e configurato correttamente." -ForegroundColor Red
    exit 1
}

# Controlla lo stato delle Podman Machines
Write-Host "Verifica delle Podman Machines attive..." -ForegroundColor Cyan
$activeMachine = podman machine list --format json | ConvertFrom-Json | Where-Object { $_.Running -eq $true }

if (-Not $activeMachine) {
    Write-Host "Errore: Nessuna Podman Machine attiva trovata." -ForegroundColor Red
    Write-Host "Esegui `podman machine init` e `podman machine start` per configurare una nuova macchina." -ForegroundColor Yellow
    exit 1
}

Write-Host "Una Podman Machine attiva è stata trovata." -ForegroundColor Green

# Controlla se esiste un container con lo stesso nome
$existingContainer = podman ps -aq --filter "name=$containerName"
if ($existingContainer) {
    Write-Host "Un container esistente è stato trovato. Lo sto eliminando..." -ForegroundColor Yellow
    podman stop $containerName | Out-Null
    podman rm $containerName | Out-Null
    Write-Host "Container esistente rimosso." -ForegroundColor Green
}

# Costruisce l'immagine
Write-Host "Costruzione dell'immagine Podman..." -ForegroundColor Cyan
podman build -t $imageName .
Write-Host "Immagine Podman creata con successo." -ForegroundColor Green


# Avvia il container
Write-Host "Avvio del container Podman..." -ForegroundColor Yellow
podman run --name $containerName -p 8501:8501 $imageName &

# Attende un momento per permettere al container di avviarsi
Write-Host "Attesa 10 secondi..." -ForegroundColor Cyan
Start-Sleep -Seconds 10

# Collegamento ai log del container
Write-Host "Collegamento ai log del container..." -ForegroundColor Cyan
try {
    podman logs -f $containerName
} catch {
    Write-Host "Errore durante il collegamento ai log del container." -ForegroundColor Red
}
