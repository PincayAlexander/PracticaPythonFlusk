const btnDelete= document.querySelectorAll('.btn__delete');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('Estas seguro que quieres borrarlo?')){
        e.preventDefault();
      }
    });
  })
}
