---
title: ImageReader.processWarningOccurred()
permalink: Java/ImageReader/processWarningOccurred
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
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
* **String keyword**,  {% include w3api/param_description.html metodo=_data parametro="String keyword" %}
* **String baseName**,  {% include w3api/param_description.html metodo=_data parametro="String baseName" %}
* **String warning**,  {% include w3api/param_description.html metodo=_data parametro="String warning" %}

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
{%- for _ldc in site.data.Java.I.ImageReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
