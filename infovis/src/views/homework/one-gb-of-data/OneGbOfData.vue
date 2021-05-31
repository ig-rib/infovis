<template>
    <v-container>
        <v-layout class="week-title-layout" justify-center py-5>
            One GB of Data
        </v-layout>
        <v-layout pt-3 mb-5 justify-center class="week-description-layout">
            Visualizaciones en Python, R y Observable//JS para la semana 19 del #MakeoverMonday
        </v-layout>
        <v-layout column justify-center>
            <v-flex mx-3 shrink class="week-card-flex">
                <image-card
                    titletext="Python"
                    img="one-gb-of-data/one-gb-of-data-overview.png"
                    :hyperlink="'https://colab.research.google.com/drive/1eTx1bz6jbFI88hqxhbkw_ZPPuUqFq6Hv?usp=sharing'"
                >
                </image-card>
            </v-flex>
            <v-flex mx-3 shrink class="week-card-flex">
                <image-card
                    titletext="R"
                    img="one-gb-of-data/R.png"
                    :hyperlink="'https://colab.research.google.com/drive/16VhGswMArGXueR399JiM2aJu7DAowXpt?usp=sharing'"
                >
                </image-card>
            </v-flex>
            <v-flex mx-3 shrink class="week-card-flex">
                <image-card
                    titletext="Observable"
                    img="one-gb-of-data/observable.png"
                    :hyperlink="'https://observablehq.com/@ig-rib/price-of-1gb-in-each-country'"
                >
                </image-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import ImageCard from '@/components/ImageCard.vue'

export default {
    components: {
        'image-card': ImageCard
    }
}
</script>