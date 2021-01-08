---
title: FileImageInputStream.FileImageInputStream()
permalink: Java/FileImageInputStream/FileImageInputStream
date: 2021-01-04
key: JavaJava.F.FileImageInputStream
category: java
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
* **File f**,  {% include w3api/param_description.html metodo=_data parametro="File f" %}
* **RandomAccessFile raf**,  {% include w3api/param_description.html metodo=_data parametro="RandomAccessFile raf" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FileImageInputStream](/Java/FileImageInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileImageInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
