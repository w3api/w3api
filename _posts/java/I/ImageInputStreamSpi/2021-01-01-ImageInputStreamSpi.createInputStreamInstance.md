---
title: ImageInputStreamSpi.createInputStreamInstance()
permalink: /Java/ImageInputStreamSpi/createInputStreamInstance/
date: 2021-01-11
key: Java.I.ImageInputStreamSpi
category: Java
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
* **Object input**,  {% include w3api/param_description.html metodo=_dato parametro="Object input" %}
* **File cacheDir**,  {% include w3api/param_description.html metodo=_dato parametro="File cacheDir" %}
* **boolean useCache**,  {% include w3api/param_description.html metodo=_dato parametro="boolean useCache" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageInputStreamSpi](/Java/ImageInputStreamSpi/)

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
