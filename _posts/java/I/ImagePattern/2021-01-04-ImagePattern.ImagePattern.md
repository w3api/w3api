---
title: ImagePattern.ImagePattern()
permalink: Java/ImagePattern/ImagePattern
date: 2021-01-04
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
* **Image image**,  {% include w3api/param_description.html metodo=_data parametro="Image image" %}
* **double width**,  {% include w3api/param_description.html metodo=_data parametro="double width" %}
* **double height**,  {% include w3api/param_description.html metodo=_data parametro="double height" %}
* **double y**,  {% include w3api/param_description.html metodo=_data parametro="double y" %}
* **double x**,  {% include w3api/param_description.html metodo=_data parametro="double x" %}
* **boolean proportional**,  {% include w3api/param_description.html metodo=_data parametro="boolean proportional" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImagePattern](/Java/ImagePattern/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImagePattern.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
