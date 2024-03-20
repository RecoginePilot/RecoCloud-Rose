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
        // Create tab class
        const tab = document.createElement('div');
        tab.id = `tab${index + 1}`;
        tab.classList.add('tab');

        // Create title text
        const title_text = document.createElement('h3');
        title_text.innerHTML = data.tabName;

        // Create image list
        console.log(data);
        const ul = document.createElement('ul');
        ul.classList.add('image-list');
        ul.appendChild(title_text);

        images = data.images;
        images.forEach(image => {
            const li = document.createElement('li');

            const img = document.createElement('img');
            img.src = image.src;
            img.alt = image.src.split('.')[0]; // Assuming image names are unique

            const image_link = document.createElement('a');
            image_link.href = image.href;

            const image_text = document.createElement('a')
            image_text.href = image.href;
            image_text.innerText = image.text;

            image_link.appendChild(img)
            // li.appendChild(image_link);
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