---
title: FileImageInputStream.FileImageInputStream()
permalink: /Java/FileImageInputStream/FileImageInputStream/
date: 2021-01-11
key: Java.F.FileImageInputStream
category: Java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileImageInputStream.constructores valor="FileImageInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileImageInputStream(File f) throws FileNotFoundException, IOException
public FileImageInputStream(RandomAccessFile raf)
~~~

## Parámetros
* **File f**,  {% include w3api/param_description.html metodo=_dato parametro="File f" %}
* **RandomAccessFile raf**,  {% include w3api/param_description.html metodo=_dato parametro="RandomAccessFile raf" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [FileNotFoundException](/Java/FileNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[FileImageInputStream](/Java/FileImageInputStream/)

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
