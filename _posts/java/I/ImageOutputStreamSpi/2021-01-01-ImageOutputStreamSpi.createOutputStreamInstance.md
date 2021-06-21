---
title: ImageOutputStreamSpi.createOutputStreamInstance()
permalink: /Java/ImageOutputStreamSpi/createOutputStreamInstance/
date: 2021-01-11
key: Java.I.ImageOutputStreamSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStreamSpi.metodos valor="createOutputStreamInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageOutputStream createOutputStreamInstance(Object output) throws IOException
public abstract ImageOutputStream createOutputStreamInstance(Object output, boolean useCache, File cacheDir) throws IOException
~~~

## Parámetros
* **File cacheDir**,  {% include w3api/param_description.html metodo=_dato parametro="File cacheDir" %}
* **Object output**,  {% include w3api/param_description.html metodo=_dato parametro="Object output" %}
* **boolean useCache**,  {% include w3api/param_description.html metodo=_dato parametro="boolean useCache" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageOutputStreamSpi](/Java/ImageOutputStreamSpi/)

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
