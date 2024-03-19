// Function to generate tab buttons
function generateTabButtons() {
    const tabContainer = document.getElementById('tabContainer');
    datas.forEach((data, index) => {
        const button = document.createElement('button');
        button.textContent = data.tabName;
        button.classList.add('tablinks');
        button.addEventListener('click', () => openTab(event, `tab${index + 1}`));
        tabContainer.appendChild(button);
    });
}

// Function to populate tabs with images
function populateTabs() {
    datas.forEach((data, index) => {
        const tab = document.createElement('div');
        tab.id = `tab${index + 1}`;
        tab.classList.add('tab');
        console.log(data);
        images = data.images;
        const ul = document.createElement('ul');
        ul.classList.add('image-list');
        images.forEach(image => {
            const li = document.createElement('li');

            const img = document.createElement('img');
            img.src = image.src;
            img.alt = image.src.split('.')[0]; // Assuming image names are unique

            const a_link = document.createElement('a');
            a_link.href = image.link;

            const image_text = document.createElement('p')
            image_text.innerText = image.text;

            a_link.appendChild(img)
            li.appendChild(a_link);
            li.appendChild(image_text);

            ul.append(li);
        });
        tab.append(ul);
        document.body.appendChild(tab);
    });
}

// Set the default tab and generate tab buttons
generateTabButtons();
populateTabs();
document.getElementById('tab1').style.display = 'block';
document.getElementsByClassName('tablinks')[0].classList.add('active');

// Function to open tabs
function openTab(evt, tabName) {
    const tabcontent = document.getElementsByClassName("tab");
    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    const tablinks = document.getElementsByClassName("tablinks");
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.classList.add("active");
}