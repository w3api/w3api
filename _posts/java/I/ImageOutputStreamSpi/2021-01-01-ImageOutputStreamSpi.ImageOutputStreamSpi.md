---
title: ImageOutputStreamSpi.ImageOutputStreamSpi()
permalink: Java/ImageOutputStreamSpi/ImageOutputStreamSpi
date: 2021-01-11
key: JavaJava.I.ImageOutputStreamSpi
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStreamSpi.constructores valor="ImageOutputStreamSpi" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ImageOutputStreamSpi()
public ImageOutputStreamSpi(String vendorName, String version, Class<?> outputClass)
~~~

## Parámetros
* **Class&lt;?&gt; outputClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> outputClass" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}
* **String vendorName**,  {% include w3api/param_description.html metodo=_dato parametro="String vendorName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageOutputStreamSpi](/Java/ImageOutputStreamSpi/)

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
