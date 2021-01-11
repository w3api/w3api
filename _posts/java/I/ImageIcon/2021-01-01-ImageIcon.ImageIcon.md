---
title: ImageIcon.ImageIcon()
permalink: Java/ImageIcon/ImageIcon
date: 2021-01-11
key: JavaJava.I.ImageIcon
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageIcon.constructores valor="ImageIcon" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageIcon()
public ImageIcon(byte[] imageData)
public ImageIcon(byte[] imageData, String description)
public ImageIcon(Image image)
public ImageIcon(Image image, String description)
@ConstructorProperties("description") public ImageIcon(String filename)
public ImageIcon(String filename, String description)
public ImageIcon(URL location)
public ImageIcon(URL location, String description)
~~~

## Parámetros
* **String description**,  {% include w3api/param_description.html metodo=_dato parametro="String description" %}
* **byte[] imageData**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] imageData" %}
* **Image image**,  {% include w3api/param_description.html metodo=_dato parametro="Image image" %}
* **String filename**,  {% include w3api/param_description.html metodo=_dato parametro="String filename" %}
* **URL location**,  {% include w3api/param_description.html metodo=_dato parametro="URL location" %}

## Clase Padre
[ImageIcon](/Java/ImageIcon/)

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
