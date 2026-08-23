const shelf = [...document.querySelectorAll("span.h1Shelf")]
  .find((span) => span.textContent.trim().startsWith("Want to Read"));

const books = [...document.querySelectorAll("table#books tr")]
  .map((row) => {
    const cover = row.querySelector("td.field.cover div.value a");
    const title = row.querySelector("td.field.title div.value a");
    const author = row.querySelector("td.field.author div.value a");

    return {
      cover: cover?.querySelector("img")?.src ?? cover?.href ?? null,
      title: title?.textContent.trim() ?? null,
      author: author?.textContent.trim() ?? null,
    };
  })
  .filter((book) => book.title);

if (shelf && books) {
  console.log("Want to Read");
  console.log(books);

}
