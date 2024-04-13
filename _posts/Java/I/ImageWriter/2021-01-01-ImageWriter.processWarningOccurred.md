---
title: ImageWriter.processWarningOccurred()
permalink: /Java/ImageWriter/processWarningOccurred/
date: 2021-01-11
key: Java.I.ImageWriter
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriter.metodos valor="processWarningOccurred" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void processWarningOccurred(int imageIndex, String warning)
protected void processWarningOccurred(int imageIndex, String baseName, String keyword)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **String keyword**,  {% include w3api/param_description.html metodo=_dato parametro="String keyword" %}
* **String warning**,  {% include w3api/param_description.html metodo=_dato parametro="String warning" %}
* **int imageIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int imageIndex" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
