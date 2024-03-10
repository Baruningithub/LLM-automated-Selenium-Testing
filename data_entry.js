let formData = [];

function handleSubmit(event) {
  event.preventDefault();

  const data1 = document.getElementById('data1').value;
  const data2 = document.getElementById('data2').value;

  const entry = {
    data1: data1,
    data2: data2
  };

  formData.push(entry);

  document.getElementById('data1').value = '';
  document.getElementById('data2').value = '';

  displayEntries();
}

function displayEntries() {
  const entriesList = document.getElementById('entries');
  entriesList.innerHTML = '';

  formData.forEach((entry, index) => {
    const li = document.createElement('li');
    li.textContent = `Entry ${index + 1}: Regd no. - ${entry.data1}, Sem - ${entry.data2}`;
    entriesList.appendChild(li);
  });
}

document.getElementById('dataEntryForm').addEventListener('submit', handleSubmit);
