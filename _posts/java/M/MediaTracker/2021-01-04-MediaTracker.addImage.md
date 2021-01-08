---
title: MediaTracker.addImage()
permalink: Java/MediaTracker/addImage
date: 2021-01-04
key: JavaJava.M.MediaTracker
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MediaTracker.metodos valor="addImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addImage(Image image, int id)
public void addImage(Image image, int id, int w, int h)
~~~

## Parámetros
* **Image image**,  {% include w3api/param_description.html metodo=_data parametro="Image image" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}

## Clase Padre
[MediaTracker](/Java/MediaTracker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MediaTracker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
