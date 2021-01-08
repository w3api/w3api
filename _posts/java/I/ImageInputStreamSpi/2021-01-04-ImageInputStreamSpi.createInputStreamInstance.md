---
title: ImageInputStreamSpi.createInputStreamInstance()
permalink: Java/ImageInputStreamSpi/createInputStreamInstance
date: 2021-01-04
key: JavaJava.I.ImageInputStreamSpi
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageInputStreamSpi.metodos valor="createInputStreamInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageInputStream createInputStreamInstance(Object input) throws IOException
public abstract ImageInputStream createInputStreamInstance(Object input, boolean useCache, File cacheDir) throws IOException
~~~

## Parámetros
* **boolean useCache**,  {% include w3api/param_description.html metodo=_data parametro="boolean useCache" %}
* **File cacheDir**,  {% include w3api/param_description.html metodo=_data parametro="File cacheDir" %}
* **Object input**,  {% include w3api/param_description.html metodo=_data parametro="Object input" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageInputStreamSpi](/Java/ImageInputStreamSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageInputStreamSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
