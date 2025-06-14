export const deleteAutorRow = (event) => {
  if (event.target && event.target.classList.contains("remove-btn")) {
    const rowId = event.target.getAttribute("data-row-id");
    const rowToRemove = document.getElementById(`autor-row-${rowId}`);
    if (rowToRemove) {
      rowToRemove.remove();
    }
  }
};
