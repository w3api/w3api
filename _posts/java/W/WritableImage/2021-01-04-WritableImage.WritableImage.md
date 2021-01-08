---
title: WritableImage.WritableImage()
permalink: Java/WritableImage/WritableImage
date: 2021-01-04
key: JavaJava.W.WritableImage
category: java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WritableImage.constructores valor="WritableImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public WritableImage(int width, int height)
public WritableImage(PixelReader reader, int width, int height)
public WritableImage(PixelReader reader, int x, int y, int width, int height)
~~~

## Parámetros
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **int height**,  {% include w3api/param_description.html metodo=_data parametro="int height" %}
* **PixelReader reader**,  {% include w3api/param_description.html metodo=_data parametro="PixelReader reader" %}
* **int width**,  {% include w3api/param_description.html metodo=_data parametro="int width" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[WritableImage](/Java/WritableImage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WritableImage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
