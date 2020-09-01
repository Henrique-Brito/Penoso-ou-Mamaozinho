<template>
  <div>
    <b-container>
      <h2><b-badge>TOP 3</b-badge> Penosas e Mamaozinhas </h2>
      <b-tabs>
        <b-tab title="Penosas pra ca#$!" active>
          <RankingCourses 
            :first_course="worst_courses_data[0]"
            :second_course="worst_courses_data[1]"
            :third_course="worst_courses_data[2]"
          />
        </b-tab>
        <b-tab title="Melzinho na chupeta">
          <RankingCourses 
            :first_course="top_courses_data[0]"
            :second_course="top_courses_data[1]"
            :third_course="top_courses_data[2]"
          />
        </b-tab>
      </b-tabs>
    </b-container>
    <!-- <b-container>
      <b-row>
        <b-col class="myText" sm="6">Mais penosas!</b-col>
        <b-col class="myText" sm="6">Mais mamaozinhas!</b-col>
      </b-row>
      <b-row align-h="between">
        <b-col sm="6"><ClassBox :classData="classData"/></b-col>
        <b-col sm="6"><ClassBox :classData="classData"/></b-col>
      </b-row>
      <b-row>
        <b-col sm="6"><ClassBox :classData="classData"/></b-col>
        <b-col sm="6"><ClassBox :classData="classData"/></b-col>
      </b-row>
      <b-row>
        <b-col sm="6"><ClassBox :classData="classData"/></b-col>
        <b-col sm="6"><ClassBox :classData="classData"/></b-col>
      </b-row>
    </b-container> -->
  </div>
</template>

<script>
// import ClassBox from './ClassBox.vue'
import RankingCourses from './RankingCourses.vue'


export default {
  components: {
    RankingCourses
    // ClassBox
  },
  data: () => {
    return {
      userData: {
        profilePicture: "https://avatars2.githubusercontent.com/u/42759576?s=460&u=1d2af611e2b6515f5b2a0b8da7c0708326b00880&v=4",
        profileUrl: "/profile",
        isLogged: false
      },
      classData: {
        name: "Engenharia de Software",
        rating: 0,
        numberVotes: 77
      }
    }
  },
  props: {
    top_courses_data: Array,
    worst_courses_data: Array
  }
}
</script>

<style scoped>
  .myText {
    font-size: 3.6rem;
    align-items: center;
  }
</style>
