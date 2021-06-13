---
title: ImageOutputStream.flushBefore()
permalink: /Java/ImageOutputStream/flushBefore/
date: 2021-01-11
key: Java.I.ImageOutputStream
category: Java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="flushBefore" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void flushBefore(long pos) throws IOException
~~~

## Parámetros
* **long pos**,  {% include w3api/param_description.html metodo=_dato parametro="long pos" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageOutputStream](/Java/ImageOutputStream/)

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
