---
title: ImageInputStreamSpi.ImageInputStreamSpi()
permalink: /Java/ImageInputStreamSpi/ImageInputStreamSpi/
date: 2021-01-11
key: Java.I.ImageInputStreamSpi
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageInputStreamSpi.constructores valor="ImageInputStreamSpi" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ImageInputStreamSpi()
public ImageInputStreamSpi(String vendorName, String version, Class<?> inputClass)
~~~

## Parámetros
* **Class&lt;?&gt; inputClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> inputClass" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}
* **String vendorName**,  {% include w3api/param_description.html metodo=_dato parametro="String vendorName" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ImageInputStreamSpi](/Java/ImageInputStreamSpi/)

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
