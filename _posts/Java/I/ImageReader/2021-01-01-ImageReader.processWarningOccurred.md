---
title: ImageReader.processWarningOccurred()
permalink: /Java/ImageReader/processWarningOccurred/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="processWarningOccurred" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void processWarningOccurred(String warning)
protected void processWarningOccurred(String baseName, String keyword)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **String keyword**,  {% include w3api/param_description.html metodo=_dato parametro="String keyword" %}
* **String warning**,  {% include w3api/param_description.html metodo=_dato parametro="String warning" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageReader](/Java/ImageReader/)

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
