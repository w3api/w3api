---
title: ImageOutputStreamSpi.createOutputStreamInstance()
permalink: Java/ImageOutputStreamSpi/createOutputStreamInstance
date: 2021-01-04
key: JavaJava.I.ImageOutputStreamSpi
category: java
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
* **Object output**,  {% include w3api/param_description.html metodo=_data parametro="Object output" %}
* **File cacheDir**,  {% include w3api/param_description.html metodo=_data parametro="File cacheDir" %}
* **boolean useCache**,  {% include w3api/param_description.html metodo=_data parametro="boolean useCache" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageOutputStreamSpi](/Java/ImageOutputStreamSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageOutputStreamSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
