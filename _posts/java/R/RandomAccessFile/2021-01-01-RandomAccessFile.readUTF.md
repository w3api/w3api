---
title: RandomAccessFile.readUTF()
permalink: /Java/RandomAccessFile/readUTF/
date: 2021-01-11
key: Java.R.RandomAccessFile
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RandomAccessFile.metodos valor="readUTF" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final String readUTF() throws IOException
~~~

## Excepciones
[UTFDataFormatException](/Java/UTFDataFormatException/), [EOFException](/Java/EOFException/), [IOException](/Java/IOException/)

## Clase Padre
[RandomAccessFile](/Java/RandomAccessFile/)

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
