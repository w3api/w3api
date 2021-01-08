---
title: AudioSpectrumListener.spectrumDataUpdate()
permalink: Java/AudioSpectrumListener/spectrumDataUpdate
date: 2021-01-04
key: JavaJava.A.AudioSpectrumListener
category: java
tags: ['java se', 'javafx.scene.media', 'javafx.media', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AudioSpectrumListener.metodos valor="spectrumDataUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void spectrumDataUpdate(double timestamp, double duration, float[] magnitudes, float[] phases)
~~~

## Parámetros
* **float[] phases**,  {% include w3api/param_description.html metodo=_data parametro="float[] phases" %}
* **double timestamp**,  {% include w3api/param_description.html metodo=_data parametro="double timestamp" %}
* **float[] magnitudes**,  {% include w3api/param_description.html metodo=_data parametro="float[] magnitudes" %}
* **double duration**,  {% include w3api/param_description.html metodo=_data parametro="double duration" %}

## Clase Padre
[AudioSpectrumListener](/Java/AudioSpectrumListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AudioSpectrumListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
