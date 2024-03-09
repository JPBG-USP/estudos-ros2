# Here we have the script that build our spotnoetic

# Check if you are on the right directory to run the build
if [[ $PWD = *estudos-ros2 ]]; then
    cd docker
elif [[ ! $PWD = *estudos-ros2/docker ]]; then
    echo -e "You must be in either 'estudos-ros2' or the 'estudos-ros2/docker' directory to run this command."
    echo -e "Você precisa estar na pasta 'estudos-ros2' ou em 'estudos-ros2/docker' para rodar esse commando."
    return 1
fi

# Configs da build
# -f Dockerfile.spotnoetic  (-f ou --file informa o arquivo a ser dado o build)
# -t estudos-ros2:spotnoetic  (-t ou --tag é para o repositório e para a tag respectivamente, separados por dois pontos)
# --rm (Ouvi que é bom deixar, acho que remove as versões de builds antigas)

docker build \
    --network=host \
    -f Dockerfile.roshumble \
    -t estudos-ros2:roshumble \
    --rm \
    .