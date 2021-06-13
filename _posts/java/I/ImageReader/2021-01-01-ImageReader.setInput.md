---
title: ImageReader.setInput()
permalink: /Java/ImageReader/setInput/
date: 2021-01-11
key: Java.I.ImageReader
category: Java
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
* **Object input**,  {% include w3api/param_description.html metodo=_dato parametro="Object input" %}
* **boolean seekForwardOnly**,  {% include w3api/param_description.html metodo=_dato parametro="boolean seekForwardOnly" %}
* **boolean ignoreMetadata**,  {% include w3api/param_description.html metodo=_dato parametro="boolean ignoreMetadata" %}

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
