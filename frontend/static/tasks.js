const addTask = document.querySelector('.addTask');
const btn = document.querySelector('.btn');
const url = 'https://73kxgsq5r1.execute-api.ap-northeast-1.amazonaws.com/dev/tasks';

const postFetch = () => {
    let formData = new FormData(addTask);
    for (let value of formData.entries()) {
        console.log(value);
    }

    fetch(url, {
        method: 'POST',
        body: formData
    }).then((response) => {
        if(!response.ok) {
            console.log('error!');
        } 
        console.log('ok!');
        return response.json();
    }).then((data)  => {
        console.log(data);
    }).catch((error) => {
        console.log(error);
    });
};

btn.addEventListener('click', postFetch, false);