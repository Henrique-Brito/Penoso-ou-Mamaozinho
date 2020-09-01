<template>
<div class="card-container">
    <div class="user-container">
        <img class="icon" v-bind:src="picture">
        <p>
            <strong> {{name}} </strong>
        </p>
        <div class="comment-rating">
            <b-button class="rating-button" variant="outline-dark" v-on:click="countLike">
              <p>&#128285;  {{likes}}</p>
            </b-button>
            <b-button class="rating-button" variant="outline-dark" @click="countDislike">
              <p>&#128169;  {{dislikes}}</p>
            </b-button>
        </div>
    </div>
    <div class="comment-container">
        <p>{{comment}}</p>
    </div>
</div>
</template>

<script>
export default {
    data: () => {
        return {
          count: 0
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
        this.likes += 1;
      },
      countDislike: function() {
        this.dislikes += 1;
      }
    }
}
</script>

<style scoped>
    .card-container {
        display: flex;
        background-color: #f7f7f7;
        border-radius: 3rem;
        padding: 1.2rem;
        margin: 1.6rem;
        min-height: 160px;
    }
    .user-container {
        justify-content: center;
        text-align: center;
        min-width: 160px;
        max-width: 160px;
    }
    .user-container p strong {
      display: block;
      overflow: hidden;
    }
    .comment-container {
        margin-left: 1.2rem;
        max-height: 300px;
        overflow: scroll;
    }
    img {
        margin-bottom: 0.6rem;
    }
    .icon {
        width: 50px;
        border-radius: 1.2rem;
    }
    .comment-rating {
      display: flex;
      justify-content: center;
      text-align: center;
    }
    .rating-button {
      border: 0;
    }
    .rating-button p {
      /* margin-left: 1.2rem; */
    }
</style>