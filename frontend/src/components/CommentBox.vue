<template>
<div class="card-container">
    <div class="user-container">
        <img class="icon" v-bind:src="picture">
        <p>
            <strong> {{ name }} </strong>
        </p>
        <div class="comment-rating">
            <b-button class="rating-button" variant="outline-dark" v-on:click="countLike">
              <p>&#128285;  {{ likesValue }}</p>
            </b-button>
            <b-button class="rating-button" variant="outline-dark" @click="countDislike">
              <p>&#128169;  {{ dislikesValue }}</p>
            </b-button>
        </div>
    </div>
    <div class="comment-container">
        <p> {{ comment }} </p>
    </div>
</div>
</template>

<script>
export default {
    data: function() {
        return {
          count: 0,
          likesValue: this.likes,
          dislikesValue: this.dislikes
        }
    },
    props: {
        name: String,
        comment: String,
        picture: String,
        likes: Number,
        dislikes: Number,
        id: Number
    },
    methods: {
      countLike: function() {
        this.$http.post(this.$api_url + '/api/cadastro/avaliacao_comentario', {
          id_comentario: this.id,
          like_dislike: 'gostei'
        })
        .then(response => {
          if(response.data.status == 'success'){
            this.likesValue += 1
          }
        })
      },
      countDislike: function() {
        this.$http.post(this.$api_url + '/api/cadastro/avaliacao_comentario', {
          id_comentario: this.id,
          like_dislike: 'nao_gostei'
        })
        .then(response => {
          if(response.data.status == 'success'){
            this.dislikesValue += 1
          }
        })
      }
    }
}
</script>

<style src='@/assets/styles/comment_box_style.css'></style>