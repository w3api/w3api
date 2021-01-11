---
title: Component.prepareImage()
permalink: Java/Component/prepareImage
date: 2021-01-11
key: JavaJava.C.Component
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="prepareImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean prepareImage(Image image, int width, int height, ImageObserver observer)
public boolean prepareImage(Image image, ImageObserver observer)
~~~

## Parámetros
* **Image image**,  {% include w3api/param_description.html metodo=_dato parametro="Image image" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}
* **ImageObserver observer**,  {% include w3api/param_description.html metodo=_dato parametro="ImageObserver observer" %}

## Clase Padre
[Component](/Java/Component/)

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
