const btnNodeList = document.querySelectorAll(".btn-show");
const containerNodeList = document.querySelectorAll(".card__container");

const categoryList = ["jewelry", "hair-accessories", "hair-making", "wig-making"];
// const category = containerNodeList.map(node => node);
const productSection = document.getElementById("products");
console.log(productSection)
// create section with className product
// create h2 with className product__category
// create div with className card__container

const jewelryList = [
    {
        cardTitle: "Leather Earring",
        cardImage: "url(../../img/product-images/leather-earring.jpeg)"
    },
    {
        cardTitle: "Black Earring",
        cardImage: "url(../../img/product-images/black-earring.jpeg)"
    },
    {
        cardTitle: "Leather Love Earring",
        cardImage: "url(../../img/product-images/leather-love-earring.jpeg)"
    },
    {
        cardTitle: "Wooden Earring",
        cardImage: "url(../../img/product-images/wooden-earrings.jpeg)"
    },
    {
        cardTitle: "Rock Earring",
        cardImage: "url(../../img/product-images/rocklike-earrings.jpeg)"
    },
    {
        cardTitle: "Love Earring",
        cardImage: "url(../../img/product-images/love-earrings.jpeg)"
    },
    {
        cardTitle: "Butterfly Necklace",
        cardImage: "url(../../img/product-images/butterfly-necklace.jpeg)"
    },
    {
        cardTitle: "Infinity Necklace",
        cardImage: "url(../../img/product-images/infinity-necklace.jpeg)"
    },
];

const wigList = [
    {
        cardTitle: "Short Wig",
        cardImage: "url(/img/product-images/short-wig.jpeg)"
    },
    {
        cardTitle: "Dyed Curled Wig",
        cardImage: "url(/img/product-images/dyed-curled-wig.jpeg)"
    }
];

const hairMakingList = [
    {
        cardTitle: "Knotless Braids With Curls",
        cardImage: "url(/img/product-images/knotless-braids-with-curls-1.jpeg)"
    },
    {
        cardTitle: "Passion Twist",
        cardImage: "url(/img/product-images/passion-twist.jpeg)"
    },
    {
        cardTitle: "Bohemian Braid",
        cardImage: "url(/img/product-images/Bohemian-braids.jpeg)"
    }
];



categoryList.forEach(category => {
    product = document.createElement("section");
    product.className = "product";

    productCategory = document.createElement("h2");
    productCategory.className = "product__category";
    productCategory.textContent = category;
    
    cardContainer = document.createElement("div");
    cardContainer.className = "card__container";

    viewAllBtn = document.createElement("button");
    viewAllBtn.className = "btn-show";
    viewAllBtn.textContent = "Show all";
    
    product.appendChild(productCategory);
    product.appendChild(cardContainer);
    product.appendChild(viewAllBtn);
    productSection.appendChild(product);
})


// The card content should be updated dynamically from the list 
// todo: get the card container
// todo: handle to card
// todo: create <a> with classname card__image

// todo: create div listName and an iterator that uniquely assigns className and background image property
// todo: create card title
// todo: feed in the card background image from the image list


































// containerNodeList.forEach(container => {
//     if (container.childElementCount > 3) {
//         const cards = container.children;
//         for (count = 3; count < container.childElementCount; count++) {
//             cards[count].style.display = "none";
//         }
//     }
//     containerList.push(container);

// })

// for (let i = 0; i < btnNodeList.length; i++) {
//     for (let button of btnNodeList) {
//         button.onclick = () => {
//             for (let content of containerNodeList[i]) {
//                     console.log(content)
//                 }
//         }
//     }
        
// }
// console.log(containerList);
// console.log(btnList);








// I want to view only one row at a time 
// When button is clicked, the remaining cards should be displayed and the textcontent should change
// i = 1;
// viewBtn.forEach(btn => {
//     console.log(btn)
//     btn.className = `btn-show-${i}`;
//     i++;
//     btn.onclick = () => {

//         cardContainer.item()
//     cardContainer.forEach((container) => {
//         cardTotal = container.childElementCount;
//         cardList = container.children;
//         if (cardTotal > 3) {
//             console.log(cardTotal);
            

//         }
//     });
// }});

// for (i = 0; i < cardContainer.length; i++) {

//     viewBtn[i].onclick = () => {
//         console.log(cardContainer[i])
//         if (cardContainer[i].childElementCount > 3 && cardContainer[i].every(element => element.style === "block")) {
//             for (j = 3; j < cardContainer[i].childElementCount; j++) {
//                 element.style = "none";
//             }
//         }
//         else {
//             cardContainer[i].every(element => element.style = "block");
//         }
//     }
// }

// how about: foreach btn, we separate them into different handles, same for the
