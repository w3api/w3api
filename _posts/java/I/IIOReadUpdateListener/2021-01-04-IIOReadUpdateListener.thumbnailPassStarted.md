---
title: IIOReadUpdateListener.thumbnailPassStarted()
permalink: Java/IIOReadUpdateListener/thumbnailPassStarted
date: 2021-01-04
key: JavaJava.I.IIOReadUpdateListener
category: java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IIOReadUpdateListener.metodos valor="thumbnailPassStarted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void thumbnailPassStarted(ImageReader source, BufferedImage theThumbnail, int pass, int minPass, int maxPass, int minX, int minY, int periodX, int periodY, int[] bands)
~~~

## Parámetros
* **int[] bands**,  {% include w3api/param_description.html metodo=_data parametro="int[] bands" %}
* **ImageReader source**,  {% include w3api/param_description.html metodo=_data parametro="ImageReader source" %}
* **int maxPass**,  {% include w3api/param_description.html metodo=_data parametro="int maxPass" %}
* **int minX**,  {% include w3api/param_description.html metodo=_data parametro="int minX" %}
* **int pass**,  {% include w3api/param_description.html metodo=_data parametro="int pass" %}
* **int minY**,  {% include w3api/param_description.html metodo=_data parametro="int minY" %}
* **int minPass**,  {% include w3api/param_description.html metodo=_data parametro="int minPass" %}
* **int periodX**,  {% include w3api/param_description.html metodo=_data parametro="int periodX" %}
* **BufferedImage theThumbnail**,  {% include w3api/param_description.html metodo=_data parametro="BufferedImage theThumbnail" %}
* **int periodY**,  {% include w3api/param_description.html metodo=_data parametro="int periodY" %}

## Clase Padre
[IIOReadUpdateListener](/Java/IIOReadUpdateListener/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOReadUpdateListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
