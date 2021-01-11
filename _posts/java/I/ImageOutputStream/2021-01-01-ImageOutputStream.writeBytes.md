---
title: ImageOutputStream.writeBytes()
permalink: Java/ImageOutputStream/writeBytes
date: 2021-01-11
key: JavaJava.I.ImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeBytes(String s) throws IOException
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

## Excepciones
[IOException](/Java/IOException/), [NullPointerException](/Java/NullPointerException/)

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
