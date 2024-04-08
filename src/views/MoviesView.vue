<template>
  <div>
    <h1>Movies</h1>
    <div class="movie-card" v-for="movie in movies" :key="movie.id">
      <img :src="movie.poster" alt="Movie Poster" class="movie-poster" />
      <div class="movie-info">
        <h2>{{ movie.title }}</h2>
        <p>{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let movies = ref([]);

const fetchMovies = () => {
  fetch('/api/v1/movies')
    .then(response => response.json())
    .then(data => {
      movies.value = data.movies;
    })
    .catch(error => {
      console.error('Error fetching movies:', error);
    });
};

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movie-card {
  display: flex;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.movie-poster {
  width: 150px;
  height: auto;
  margin-right: 20px;
}

.movie-info {
  flex: 1;
}
</style>
