---
title: ImageReader.processPassStarted()
permalink: Java/ImageReader/processPassStarted
date: 2021-01-11
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="processPassStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void processPassStarted(BufferedImage theImage, int pass, int minPass, int maxPass, int minX, int minY, int periodX, int periodY, int[] bands)
~~~

## Parámetros
* **int pass**,  {% include w3api/param_description.html metodo=_dato parametro="int pass" %}
* **int minX**,  {% include w3api/param_description.html metodo=_dato parametro="int minX" %}
* **int minPass**,  {% include w3api/param_description.html metodo=_dato parametro="int minPass" %}
* **int minY**,  {% include w3api/param_description.html metodo=_dato parametro="int minY" %}
* **int periodY**,  {% include w3api/param_description.html metodo=_dato parametro="int periodY" %}
* **int[] bands**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bands" %}
* **int maxPass**,  {% include w3api/param_description.html metodo=_dato parametro="int maxPass" %}
* **BufferedImage theImage**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage theImage" %}
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
