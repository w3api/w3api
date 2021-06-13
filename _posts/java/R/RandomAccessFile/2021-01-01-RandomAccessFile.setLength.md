---
title: RandomAccessFile.setLength()
permalink: Java/RandomAccessFile/setLength
date: 2021-01-11
key: Java.R.RandomAccessFile
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RandomAccessFile.metodos valor="setLength" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setLength(long newLength) throws IOException
~~~

## Parámetros
* **long newLength**,  {% include w3api/param_description.html metodo=_dato parametro="long newLength" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
