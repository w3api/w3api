---
title: BufferCapabilities.BufferCapabilities()
permalink: Java/BufferCapabilities/BufferCapabilities
date: 2021-01-11
key: JavaJava.B.BufferCapabilities
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferCapabilities.constructores valor="BufferCapabilities" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BufferCapabilities(ImageCapabilities frontCaps, ImageCapabilities backCaps, BufferCapabilities.FlipContents flipContents)
~~~

## Parámetros
* **ImageCapabilities frontCaps**,  {% include w3api/param_description.html metodo=_dato parametro="ImageCapabilities frontCaps" %}
* **ImageCapabilities backCaps**,  {% include w3api/param_description.html metodo=_dato parametro="ImageCapabilities backCaps" %}
* **BufferCapabilities.FlipContents flipContents**,  {% include w3api/param_description.html metodo=_dato parametro="BufferCapabilities.FlipContents flipContents" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BufferCapabilities](/Java/BufferCapabilities/)

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
