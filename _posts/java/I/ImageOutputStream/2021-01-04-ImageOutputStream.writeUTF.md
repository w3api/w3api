---
title: ImageOutputStream.writeUTF()
permalink: Java/ImageOutputStream/writeUTF
date: 2021-01-04
key: JavaJava.I.ImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.ImageOutputStream.metodos valor="writeUTF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeUTF(String s) throws IOException
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}

## Excepciones
[UTFDataFormatException](/Java/UTFDataFormatException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[ImageOutputStream](/Java/ImageOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.ImageOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
