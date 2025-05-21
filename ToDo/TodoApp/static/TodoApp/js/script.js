function logout() {
    confirmationDialog("Вы действительно хотите выйти из аккаунта?").then((value) => {
        if (value) {
            document.location.href = document.location.origin + "/logout/";
        }
    });
}

function task_delete(id) {
    confirmationDialog("Вы действительно хотите удалить?").then((value) => {
        if (value) {
            document.location.href = document.location.origin + "/delete/" + id;
        }
    });
}

function show_info() {
    infoPlace = document.querySelector('.info_place');
    console.log(infoPlace)
    infoPlace.style.display = "flex";
    infoPlace.style.opacity = 1;
}

function close_info() {
    infoPlace = document.querySelector('.info_place');
    console.log(infoPlace)
    infoPlace.style.display = "none";
    infoPlace.style.opacity = 0;
}