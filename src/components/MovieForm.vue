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
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted  } from 'vue';

const movie = ref({
  title: '',
  description: '',
  poster: null
});

const saveMovie = () => {
  let movieForm = document.getElementById('movieForm'); 
  let form_data = new FormData(movieForm);

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
    console.log(data); 
  }) 
  .catch(function (error) { 
    console.log(error); 
  });
};

let csrf_token = ref(""); 

function getCsrfToken() { 

  fetch('/api/v1/csrf-token') 
  .then((response) => response.json()) 
  .then((data) => { 
    console.log(data); 
    csrf_token.value = data.csrf_token; 
  }) 
} 

onMounted(() => { 
  getCsrfToken(); 
}); 

const handleFileChange = (event) => {
    movie.value.poster = event.target.files[0];
    };
</script>
