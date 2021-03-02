<template>
  <v-container id="home-container">
    <v-layout my-5 row wrap justify-center>
      <v-flex px-4 md5 sm12 lg3 xl3>
        <week-card :titletext="weekInfo.week1.title" :description="weekInfo.week1.description" :link="'semana1'">
        </week-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import WeekCard from '@/components/WeekCard.vue'

export default {
  name: 'Home',
  components: {
    'week-card': WeekCard
  },
  data () {
    return {
      weekInfo: {
        week1: {
          title: 'Semana 1',
          description: 'Conceptos nuevos en "A Tour Through The Visualization Zoo" e intento de visualización del dataset "Seats Held by Women in National Parliaments and Governments"'
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  #home-container {
    height: 100%;
    .week-card {
      height: 400px;
    }
  }
  #home-main-layout {
    height: 100%;
  }
</style>
