---
title: RandomAccessFile.RandomAccessFile()
permalink: Java/RandomAccessFile/RandomAccessFile
date: 2021-01-11
key: Java.R.RandomAccessFile
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RandomAccessFile.constructores valor="RandomAccessFile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RandomAccessFile(File file, String mode) throws FileNotFoundException
public RandomAccessFile(String name, String mode) throws FileNotFoundException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String mode**,  {% include w3api/param_description.html metodo=_dato parametro="String mode" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [FileNotFoundException](/Java/FileNotFoundException/)

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
