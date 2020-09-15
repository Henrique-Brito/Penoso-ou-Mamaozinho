<template>
<div id='CoursePage'>
   <Header />
  <b-container>
    <b-alert v-show="avaliacao_erro" show variant="danger">{{ avaliacao_erro }}</b-alert>
    <b-row align-v="start" class="page-header">
      <b-col class="course-name-area">{{ disciplina.nome }}</b-col>
      <b-col class="rating-area">
        <b-progress variant="danger" height="2rem">
          <b-progress-bar :value="val_penoso">
            <span><strong>{{ val_penoso }}%</strong> Penosa</span>
          </b-progress-bar>
        </b-progress>
        <b-progress variant="success" height="2rem">
          <b-progress-bar :value="val_mamao">
            <span><strong>{{ val_mamao }}%</strong> Mamão</span>
          </b-progress-bar>
        </b-progress>
      </b-col>
    </b-row>
    <div class="user-rating p-3 ">
      <b-form-group label="Avalie essa disciplina!">
        <b-form-radio-group
          id="btn-radios-3"
          v-model="selected"
          :options="options"
          buttons
          name="radio-btn-stacked"
        ></b-form-radio-group>
      </b-form-group>
    </div>
    <b-tabs card>
      <b-tab title="Comentários" active>
        <!-- <button class="btn" @click="adicionar_comentario = !adicionar_comentario">Adicionar comentário</button> -->
        <div class="comment_button">
          <div v-if="adicionar_comentario">
            <b-alert v-show="comentario_erro" show variant="danger">{{ comentario_erro }}</b-alert>
            <b-button pill variant="danger" class="close_button" @click="adicionar_comentario = !adicionar_comentario">Fechar</b-button>
            <b-button pill variant="success" class="btn text-center" @click="cadastrar_comentario">Enviar</b-button>
          </div>
          <div v-else>
            <b-button pill variant="success" class="btn text-center" @click="adicionar_comentario = !adicionar_comentario">Adicionar comentário</b-button>
          </div>
          
          <div class="comment_form" v-show="adicionar_comentario">
            <b-form-textarea
              id="textarea"
              v-model="comentario"
              placeholder="Digite seu comentário..."
              rows="3"
              max-rows="6"
            ></b-form-textarea>
          </div>
        </div>
        <CommentBox 
          v-for="comment in comments"
          v-bind:key="comment.id_comentario"
          v-bind:name="comment.username"
          v-bind:picture="comment.picture"
          v-bind:comment="comment.texto"
          v-bind:likes="comment.num_gostei"
          v-bind:dislikes="comment.num_nao_gostei"
        />
      </b-tab>
      <b-tab title="Links úteis">
        <p> {{ selected }} </p>
      </b-tab>
      <b-tab title="Adicionar comentario">
        <p> {{disciplina}} </p>
      </b-tab>
    </b-tabs>
  </b-container>
</div>
</template>

<script>
import CommentBox from '@/components/CommentBox.vue'
import Header from '@/components/Header.vue'

export default {
  name: 'DisciplinaPagina',
  components: {
    CommentBox,
    Header
  },
  data: () => {
    return {
      id_disciplina: '',
      disciplina: '',
      comments: [],
      val_mamao: 0,
      val_penoso: 0,
      selected: '',
      options: [
        { text: 'Penosa', value: 'penoso' },
        { text: 'Mamão', value: 'mamao' }
      ],
      adicionar_comentario: false,
      comentario: '',
      teste: '',
      avaliacao_erro: '',
      comentario_erro: ''
    }
  },
  methods: {
    cadastrar_comentario: function(e) {
      e.preventDefault();
      if(!this.comentario) {
        this.comentario_erro = "Escreva seu comentário!"
      }
      else {
        this.$http.post(this.$api_url+'/api/cadastro/comentario', {
          id_disciplina: this.id_disciplina,
          comentario: this.comentario
        })
        .then(response => {
           if(response.data.status === 'error'){
            this.comentario_erro = response.data.message
          }
          else {
            this.comentario = ''
            this.adicionar_comentario = false
            this.get_comentarios()
          }
        })
      }
    },
    get_comentarios: function() {
      this.$http.get(this.$api_url+'/api/comentarios/' + this.id_disciplina)
      .then(response => {
        this.comments = response.data
      })
    },
    get_disciplina: function() {
      this.$http.get(this.$api_url + '/api/disciplina/' + this.id_disciplina)
      .then(response => {
        this.disciplina = response.data
      })
    }
  },
  watch: {
    selected: function(){
      this.$http.post(this.$api_url + '/api/cadastro/avaliacao_disciplina', {
        id_disciplina: this.id_disciplina,
        penoso_mamao: this.selected
      })
      .then(response => {
        if(response.data.status === 'error'){
          this.avaliacao_erro = response.data.message
        }
      })
    },
    disciplina: function() {
      this.val_penoso = (this.disciplina.num_penoso/(this.disciplina.num_mamao + this.disciplina.num_penoso)).toFixed(2)*100
      this.val_mamao = 100 - this.val_penoso
    }
  },
  created() {
    this.id_disciplina = window.location.href.split('/').pop()
    this.get_disciplina()
    this.get_comentarios()
  },
}
</script>

<style src='@/assets/styles/course_page_style.css' scoped></style>