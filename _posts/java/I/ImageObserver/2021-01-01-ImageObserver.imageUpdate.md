---
title: ImageObserver.imageUpdate()
permalink: Java/ImageObserver/imageUpdate
date: 2021-01-11
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
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **Image img**,  {% include w3api/param_description.html metodo=_dato parametro="Image img" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int infoflags**,  {% include w3api/param_description.html metodo=_dato parametro="int infoflags" %}

## Clase Padre
[ImageObserver](/Java/ImageObserver/)

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
