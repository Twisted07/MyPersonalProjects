const btnNodeList = document.querySelectorAll(".btn-show");
const productSection = document.getElementById("products");


// * This function takes a "product category list" and iterates over its content to gain access to their properties
// * and use them to create the content for every product card that make up the card container at container "position" 
// * in the nodeList.

function appendProductCard (productObject, node) {
    productKey = productObject.productList

    productKey.forEach(content => {
        card = document.createElement("a");
        card.href = "#";
        card.className = "card";
        
        productImage = document.createElement("div");
        productImage.className = "card__image jewelry-1";
        productImage.style.backgroundImage = content.cardImage;
        
        productName = document.createElement("h3");
        productName.className = "card__title";
        productName.textContent = content.cardTitle;
        
        card.appendChild(productImage);
        card.appendChild(productName);
        node.appendChild(card);

    })

}

// * This function takes 
function loadSection (data, parent, sectionName, sectionClass, categoryClass, buttonName, buttonClass) {

    data.forEach(category => {
        
        sectionName = document.createElement("section");
        sectionName.className = sectionClass;

        sectionCategory = document.createElement("h2");
        sectionCategory.className = categoryClass;
        sectionCategory.textContent = category.categoryName;

        cardContainer = document.createElement("div");
        cardContainer.className = "card__container";

        btn = document.createElement("button");
        btn.className = buttonClass;
        btn.textContent = buttonName;

        sectionName.appendChild(sectionCategory);

        appendProductCard(category, cardContainer);

        sectionName.appendChild(cardContainer);
        sectionName.appendChild(btn);
        parent.appendChild(sectionName);
    })

}


// ? We have to keep every product category object organized in a list so as to help keep track and make it easy to update
productData = [
    {
        categoryName: "Jewelry",
        productList: [
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
        ] 
    },
    {
        categoryName: "Hair Accessories",
        productList: [
            {
                cardTitle: "none",
                cardImage: "none"
            }
        ]
    },
    {
        categoryName: "Wigs",
        productList: [
            {
                cardTitle: "Short Wig",
                cardImage: "url(/img/product-images/short-wig.jpeg)"
            },
            {
                cardTitle: "Dyed Curled Wig",
                cardImage: "url(/img/product-images/dyed-curled-wig.jpeg)"
            }
        ]
    },
    {
        categoryName: "Hair Making",
        productList: [
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
        ]
    }
];

loadSection(productData, productSection, "product", "product", "product__category", "showAll", "btn-show");