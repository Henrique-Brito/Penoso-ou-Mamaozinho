<template>
<div>
  <b-container>
    <b-row align-v="start" class="page-header">
      <b-col class="course-name-area">{{ course_data.name }}</b-col>
      <b-col class="rating-area">
        <b-input-group>
          <b-form-rating v-model="course_data.rating" color="#ff8800" readonly show-value show-value-max inline></b-form-rating>
        </b-input-group>
      </b-col>
    </b-row>
    <div class="user-rating p-3 ">
      <b-input-group class="w-50 ">
        <label for="rating-course">Avalie essa disciplina!</label> 
        <b-form-rating id="rating-course" v-model="user_rate" color="#ff8800" size="sm"></b-form-rating>
        <b-button size="sm" lg="4" class="pb-2" @click="user_rate = null">Clear</b-button>
      </b-input-group>
    </div>
    <b-tabs card>
      <b-tab title="Comentários" active>
        <CommentBox 
          v-for="comment in comments"
          v-bind:key="comment.id"
          v-bind:name="comment.user_name"
          v-bind:picture="comment.user_picture"
          v-bind:comment="comment.comment"
          v-bind:likes="comment.likes"
          v-bind:dislikes="comment.dislikes"
        />
      </b-tab>
      <b-tab title="Links úteis">
        <p>Tab contents 2</p>
      </b-tab>
      <b-tab title="Adicionar comentario">
        <p>Tab contents 2</p>
      </b-tab>
    </b-tabs>
  </b-container>
</div>
</template>

<script>
import CommentBox from './CommentBox.vue'

export default {
  name: 'App',
  components: {
    CommentBox
  },
  data: () => {
    return {
      user_rate: null
    }
  },
  props: {
    course_data: Object,
    comments: Array
  }
}
</script>

<style>
  .page-header {
    font-size: 3.6rem;
    padding: 3.6rem 0;
  }
  .course-name-area {
    font-size: 2.4rem;
  }
  .rating-area {
    padding-top: 0.6rem;
  }
  .user-rating {
    /* margin-top: 2.4rem;  */
    display: flex;
    justify-content: center;
  }
  #rating-course {
    margin-left: 0.6rem;
  }
  label {
    font-size: 1.2rem;
  }
  .myText {
    font-size: 3.6rem;
    align-items: center;
  }
</style>
