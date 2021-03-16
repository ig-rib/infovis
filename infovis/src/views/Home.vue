<template>
  <v-container id="home-container">
    <v-layout mt-5 justify-center id="home-title">
      Infovis
    </v-layout>
    <v-layout my-8 justify-center id="home-description">
      Portfolio con tareas de la materia Visualización de la Información de ITBA
    </v-layout>
    <div class="fill-width">
      <!-- <masonry
          class="masonry-flex"
          :cols="{default: 4, 1700: 3, 1300: 2, 960: 1}"
          :gutter="{default: '2px', 1600: '2px', 1300: '2px', 960: '2px'}"
          > -->
        <v-layout justify-center>
          <v-flex mx-1 shrink class="week-card-flex">
            <week-card
              :titletext="weekInfo.week1.title"
              :description="weekInfo.week1.description"
              :link="'semana1'"
              img="semana1/makeoverMonday/2003.png">
            </week-card>
          </v-flex>
          <v-flex mx-1 shrink class="week-card-flex">
            <week-card
              :titletext="weekInfo.week3.title"
              :description="weekInfo.week3.description"
              :link="'semana3'"
              img="semana3/week3overview.png">
            </week-card>
          </v-flex>
        </v-layout>
        <!-- </masonry> -->
    </div>
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
        },
        week3: {
          title: 'Semana 3',
          description: 'Makeover Monday Week 11 - World\'s Largest Crops'
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
  #home-container {
    height: 100%;
  }
  #home-main-layout {
    height: 100%;
  }
  .masonry-flex {
    justify-content: center;
  }
  .masonry-flex > div {
    min-width: min-content !important;
  }
  .week-card-flex {
    display: flex;
    justify-content: center;
    min-width: max-content !important;
    padding: 5% 0 0 0;
  }
  .fill-width {
    min-width: 100% !important;
    width: 100% !important;
  }
  #home-title {
    font-size: 60px;
    font-weight: 300;
  }
  #home-description {
    font-size: 30px;
    font-weight: 300;
  }
</style>
