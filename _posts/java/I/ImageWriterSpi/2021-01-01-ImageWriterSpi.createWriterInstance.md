---
title: ImageWriterSpi.createWriterInstance()
permalink: /Java/ImageWriterSpi/createWriterInstance/
date: 2021-01-11
key: Java.I.ImageWriterSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageWriterSpi.metodos valor="createWriterInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ImageWriter createWriterInstance() throws IOException
public abstract ImageWriter createWriterInstance(Object extension) throws IOException
~~~

## Parámetros
* **Object extension**,  {% include w3api/param_description.html metodo=_dato parametro="Object extension" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageWriterSpi](/Java/ImageWriterSpi/)

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
