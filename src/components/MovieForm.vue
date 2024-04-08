<template>
  <form @submit.prevent="saveMovie" id="movieForm">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input type="text" name="title" v-model="movie.title" class="form-control" />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea name="description" v-model="movie.description" class="form-control"></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input type="file" name="poster" @change="handleFileChange" class="form-control" />
    </div>

    <div v-if="successMessage" class="alert alert-success" role="alert">
      {{ successMessage }}
    </div>

    <div v-if="errorMessages.length > 0" class="alert alert-danger" role="alert">
      <ul>
        <li v-for="error in errorMessages" :key="error">{{ error }}</li>
      </ul>
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted  } from 'vue';

const successMessage = ref('');
const errorMessages = ref([]);

let csrf_token = ref(""); 

function getCsrfToken() { 

  fetch('/api/v1/csrf-token') 
  .then((response) => response.json()) 
  .then((data) => { 
    console.log(data); 
    csrf_token.value = data.csrf_token;
    //saveMovie(); 
  }) 
} 

onMounted(() => { 
  getCsrfToken(); 
}); 

const movie = ref({
  title: '',
  description: '',
  poster: null
});

const saveMovie = () => {
  let movieForm = document.getElementById('movieForm'); 
  let formData = new FormData(movieForm);

  formData.append('title', movie.value.title);
  formData.append('description', movie.value.description);
  formData.append('poster', movie.value.poster);

  fetch("/api/v1/movies", {
    method: 'POST',
    body: formData, 
    headers: { 
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(function (response) { 
      return response.json(); 
  }) 
  .then(function (data) { 
    // display a success message 
    successMessage.value = data.message;
    errorMessages.value = [];
    
    //console.log(data); 
  }) 
  .catch(function (error) { 
    console.error('There was a problem with the fetch operation:', error);
    successMessage.value = '';
    errorMessages.value = ['Failed to save movie. Please try again.'];
    
    //console.log(error); 
  });
};

const handleFileChange = (event) => {
    movie.value.poster = event.target.files[0];
    };
</script>
