<template>
  <v-container mb-5 id="home-container">
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
        <v-layout row wrap justify-center>
          <v-flex mx-3 shrink class="week-card-flex">
            <week-card
              :titletext="weekInfo.week1.title"
              :description="weekInfo.week1.description"
              :link="'semana1'"
              img="semana1/makeoverMonday/2003.png">
            </week-card>
          </v-flex>
          <v-flex mx-3 shrink class="week-card-flex">
            <week-card
              :titletext="weekInfo.week3.title"
              :description="weekInfo.week3.description"
              :link="'semana3'"
              img="semana3/week3overview.png">
            </week-card>
          </v-flex>
          <v-flex mx-3 shrink class="week-card-flex">
            <week-card
              :titletext="weekInfo.week6.title"
              :description="weekInfo.week6.description"
              :link="'semana6'"
              img="semana6/week6overview.png">
            </week-card>
          </v-flex>
          <v-flex mx-3 shrink class="week-card-flex">
            <week-card
              :titletext="weekInfo.tpdatospersonales.title"
              :description="weekInfo.tpdatospersonales.description"
              :link="'tp-datos-personales'"
              img="tp-datos-personales/tp-datos-personalesoverview.png">
            </week-card>
          </v-flex>
          <v-flex mx-3 shrink class="week-card-flex">
            <image-card
              :titletext="weekInfo.oneGbOfDataPython.title"
              :description="weekInfo.oneGbOfDataPython.description"
              :hyperlink="'https://colab.research.google.com/drive/1eTx1bz6jbFI88hqxhbkw_ZPPuUqFq6Hv?usp=sharing'"
              img="one-gb-of-data/one-gb-of-data-overview.png">
            </image-card>
          </v-flex>
          <v-flex mx-3 shrink class="week-card-flex">
            <image-card
              :titletext="weekInfo.oneGbOfDataR.title"
              :description="weekInfo.oneGbOfDataR.description"
              :hyperlink="'https://colab.research.google.com/drive/16VhGswMArGXueR399JiM2aJu7DAowXpt?usp=sharing'"
              img="one-gb-of-data/R.png">
            </image-card>
          </v-flex>
          <v-flex mx-3 shrink class="week-card-flex">
            <image-card
              :titletext="weekInfo.oneGbOfDataObservable.title"
              :description="weekInfo.oneGbOfDataObservable.description"
              :hyperlink="'https://observablehq.com/@ig-rib/price-of-1gb-in-each-country'"
              img="one-gb-of-data/observable.png">
            </image-card>
          </v-flex>
        </v-layout>
        <!-- </masonry> -->
    </div>
  </v-container>
</template>

<script>
import WeekCard from '@/components/WeekCard.vue'
import ImageCard from '@/components/ImageCard.vue'

export default {
  name: 'Home',
  components: {
    'week-card': WeekCard,
    'image-card': ImageCard
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
        },
        week6: {
          title: 'Semana 6',
          description: 'Población por Provincias Argentinas'
        },
        tpdatospersonales: {
          title: 'TP Infovis - Datos Personales',
          description: 'Noticias'
        },
        oneGbOfDataPython: {
          title: 'One GB of Data - Python Viz',
          description: 'Visualización en Python para la semana 19 del #MakeoverMonday'
        },
        oneGbOfDataR: {
          title: 'One GB of Data - R Viz',
          description: 'Visualización en R para la semana 19 del #MakeoverMonday'
        },
        oneGbOfDataObservable: {
          title: 'One GB of Data - Observable Viz',
          description: 'Visualización en Observable//JS para la semana 19 del #MakeoverMonday'
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/styles/weekCard.scss';

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
