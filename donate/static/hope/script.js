document.getElementById('donation_Form')?.addEventListener('submit', function(e) {
  e.preventDefault();
  alert('Thank you for your donation! We will arrange a pickup soon.');
  this.reset();
});
