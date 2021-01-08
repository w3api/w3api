---
title: ImageWriter.processWarningOccurred()
permalink: Java/ImageWriter/processWarningOccurred
date: 2021-01-04
key: JavaJava.I.ImageWriter
category: java
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
* **int imageIndex**,  {% include w3api/param_description.html metodo=_data parametro="int imageIndex" %}
* **String baseName**,  {% include w3api/param_description.html metodo=_data parametro="String baseName" %}
* **String keyword**,  {% include w3api/param_description.html metodo=_data parametro="String keyword" %}
* **String warning**,  {% include w3api/param_description.html metodo=_data parametro="String warning" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageWriter](/Java/ImageWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
