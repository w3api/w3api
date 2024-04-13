---
title: ImageReader.processThumbnailPassStarted()
permalink: /Java/ImageReader/processThumbnailPassStarted/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
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
* **int minX**,  {% include w3api/param_description.html metodo=_dato parametro="int minX" %}
* **int pass**,  {% include w3api/param_description.html metodo=_dato parametro="int pass" %}
* **BufferedImage theThumbnail**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage theThumbnail" %}
* **int minPass**,  {% include w3api/param_description.html metodo=_dato parametro="int minPass" %}
* **int minY**,  {% include w3api/param_description.html metodo=_dato parametro="int minY" %}
* **int periodY**,  {% include w3api/param_description.html metodo=_dato parametro="int periodY" %}
* **int maxPass**,  {% include w3api/param_description.html metodo=_dato parametro="int maxPass" %}
* **int[] bands**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bands" %}
* **int periodX**,  {% include w3api/param_description.html metodo=_dato parametro="int periodX" %}

## Clase Padre
[ImageReader](/Java/ImageReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
