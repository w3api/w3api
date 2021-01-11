---
title: ImagePattern.ImagePattern()
permalink: Java/ImagePattern/ImagePattern
date: 2021-01-11
key: JavaJava.I.ImagePattern
category: java
tags: ['java se', 'javafx.scene.paint', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImagePattern.constructores valor="ImagePattern" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImagePattern(Image image)
public ImagePattern(Image image, double x, double y, double width, double height, boolean proportional)
~~~

## Parámetros
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **double width**,  {% include w3api/param_description.html metodo=_dato parametro="double width" %}
* **boolean proportional**,  {% include w3api/param_description.html metodo=_dato parametro="boolean proportional" %}
* **Image image**,  {% include w3api/param_description.html metodo=_dato parametro="Image image" %}
* **double height**,  {% include w3api/param_description.html metodo=_dato parametro="double height" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ImagePattern](/Java/ImagePattern/)

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
