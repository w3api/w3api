---
title: ImageView.ImageView()
permalink: Java/ImageView-javafx-scene-image/ImageView
date: 2021-01-11
key: JavaJava.I.ImageView-javafx-scene-image
category: java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageView-javafx-scene-image.constructores valor="ImageView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageView()
public ImageView(String url)
public ImageView(Image image)
~~~

## Parámetros
* **Image image**,  {% include w3api/param_description.html metodo=_dato parametro="Image image" %}
* **String url**,  {% include w3api/param_description.html metodo=_dato parametro="String url" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ImageView](/Java/ImageView-javafx-scene-image/)

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
