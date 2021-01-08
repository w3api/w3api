---
title: ImageObserver.imageUpdate()
permalink: Java/ImageObserver/imageUpdate
date: 2021-01-04
key: JavaJava.I.ImageObserver
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageObserver.metodos valor="imageUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean imageUpdate(Image img, int infoflags, int x, int y, int width, int height)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **Image img**,  {% include w3api/param_description.html metodo=_data parametro="Image img" %}
* **int infoflags**,  {% include w3api/param_description.html metodo=_data parametro="int infoflags" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[ImageObserver](/Java/ImageObserver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageObserver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
