---
title: ImageReader.setInput()
permalink: Java/ImageReader/setInput
date: 2021-01-04
key: JavaJava.I.ImageReader
category: java
tags: ['java se', 'javax.imageio', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageReader.metodos valor="setInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setInput(Object input)
public void setInput(Object input, boolean seekForwardOnly)
public void setInput(Object input, boolean seekForwardOnly, boolean ignoreMetadata)
~~~

## Parámetros
* **boolean ignoreMetadata**,  {% include w3api/param_description.html metodo=_data parametro="boolean ignoreMetadata" %}
* **boolean seekForwardOnly**,  {% include w3api/param_description.html metodo=_data parametro="boolean seekForwardOnly" %}
* **Object input**,  {% include w3api/param_description.html metodo=_data parametro="Object input" %}

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
