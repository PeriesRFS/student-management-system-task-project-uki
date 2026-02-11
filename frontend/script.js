const API_URL = "";
const form = document.getElementById("studentForm");
const tableBody = document.getElementById("studentTable");

//Load and Display student-list - when the page loads
//Load Students
window.onboard = fetchStudents;

//Fetch and Display students
function fetchStudents() {
  fetch(API_URL)
    .then((res) => res.json())
    .then((data) => {
      tableBody.innerHTML = "";
      data.forEach((student) => {
        const row = `
                <tr>
                    <td>${student.id}</td>
                    <td>${student.name} </td>
                    <td>${student.email}</td>
                    <td>${student.course}</td>
                    <td>
                        <button onclick="deleteStudent(${student.id})">Delete</button>
                    </td>
                </tr>
            `;
        tableBody.innerHTML += row;
      });
    });
}

//Add Student
form.addEventListener("submit", function (e) {
  e.preventDefault();

  //create a student object
  const student = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    course: document.getElementById("course").value,
  };

  //Send a POST request to the API to add a new student
  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(student),
  })
    
    //checking if the request sent was sucessful
    .then((res) => {
      if (!res.ok) throw new Error("Failled to add student");
      return res.json();
    });
});

//Delete Students using their id
function deletStudents(id) {

  //send the delete request to api with student id
  fetch(API_URL + id, { method: "DELETE" })
  
    //check if the delete was sucessful
    .then((res) => {
      if (!res.ok) throw new Error("Delete failed");
    });
}
