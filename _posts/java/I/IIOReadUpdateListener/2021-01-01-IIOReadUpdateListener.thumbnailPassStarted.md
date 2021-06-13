---
title: IIOReadUpdateListener.thumbnailPassStarted()
permalink: /Java/IIOReadUpdateListener/thumbnailPassStarted/
date: 2021-01-11
key: Java.I.IIOReadUpdateListener
category: Java
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
* **ImageReader source**,  {% include w3api/param_description.html metodo=_dato parametro="ImageReader source" %}
* **int pass**,  {% include w3api/param_description.html metodo=_dato parametro="int pass" %}
* **int minX**,  {% include w3api/param_description.html metodo=_dato parametro="int minX" %}
* **BufferedImage theThumbnail**,  {% include w3api/param_description.html metodo=_dato parametro="BufferedImage theThumbnail" %}
* **int minPass**,  {% include w3api/param_description.html metodo=_dato parametro="int minPass" %}
* **int minY**,  {% include w3api/param_description.html metodo=_dato parametro="int minY" %}
* **int periodY**,  {% include w3api/param_description.html metodo=_dato parametro="int periodY" %}
* **int maxPass**,  {% include w3api/param_description.html metodo=_dato parametro="int maxPass" %}
* **int[] bands**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bands" %}
* **int periodX**,  {% include w3api/param_description.html metodo=_dato parametro="int periodX" %}

## Clase Padre
[IIOReadUpdateListener](/Java/IIOReadUpdateListener/)

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
