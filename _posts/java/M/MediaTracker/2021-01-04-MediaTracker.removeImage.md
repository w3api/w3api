---
title: MediaTracker.removeImage()
permalink: Java/MediaTracker/removeImage
date: 2021-01-04
key: JavaJava.M.MediaTracker
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MediaTracker.metodos valor="removeImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void removeImage(Image image)
public void removeImage(Image image, int id)
public void removeImage(Image image, int id, int width, int height)
~~~

## Parámetros
* **Image image**,  {% include w3api/param_description.html metodo=_data parametro="Image image" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **int id**,  {% include w3api/param_description.html metodo=_data parametro="int id" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}

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
