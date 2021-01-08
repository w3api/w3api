---
title: RandomAccessFile.writeBytes()
permalink: Java/RandomAccessFile/writeBytes
date: 2021-01-04
key: JavaJava.R.RandomAccessFile
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RandomAccessFile.metodos valor="writeBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final void writeBytes(String s) throws IOException
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RandomAccessFile](/Java/RandomAccessFile/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RandomAccessFile.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
