

echo "Dağıtım işlemi başlatılıyor..."

docker stop e-commerce-app || true
docker rm e-commerce-app || true


docker run -d -p 5000:5000 --name e-commerce-app e-commerce-app:latest

echo "Dağıtım başarıyla tamamlandı!"
