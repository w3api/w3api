---
title: ImageReader.processThumbnailPassStarted()
permalink: Java/ImageReader/processThumbnailPassStarted
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="processThumbnailPassStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void processThumbnailPassStarted(BufferedImage theThumbnail, int pass, int minPass, int maxPass, int minX, int minY, int periodX, int periodY, int[] bands)
~~~

## Parámetros
* **int[] bands**,  {% include w3api/param_description.html metodo=_data parametro="int[] bands" %}
* **int maxPass**,  {% include w3api/param_description.html metodo=_data parametro="int maxPass" %}
* **int minX**,  {% include w3api/param_description.html metodo=_data parametro="int minX" %}
* **int pass**,  {% include w3api/param_description.html metodo=_data parametro="int pass" %}
* **int minY**,  {% include w3api/param_description.html metodo=_data parametro="int minY" %}
* **int minPass**,  {% include w3api/param_description.html metodo=_data parametro="int minPass" %}
* **int periodX**,  {% include w3api/param_description.html metodo=_data parametro="int periodX" %}
* **BufferedImage theThumbnail**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage theThumbnail" %}
* **int periodY**,  {% include w3api/param_description.html metodo=_data parametro="int periodY" %}

## Clase Padre
[ImageReader](/Java/ImageReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
