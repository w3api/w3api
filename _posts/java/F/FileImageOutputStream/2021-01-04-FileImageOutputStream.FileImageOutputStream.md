---
title: FileImageOutputStream.FileImageOutputStream()
permalink: Java/FileImageOutputStream/FileImageOutputStream
date: 2021-01-04
key: JavaJava.F.FileImageOutputStream
category: java
tags: ['java se', 'javax.imageio.stream', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileImageOutputStream.constructores valor="FileImageOutputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileImageOutputStream(File f) throws FileNotFoundException, IOException
public FileImageOutputStream(RandomAccessFile raf)
~~~

## Parámetros
* **File f**,  {% include w3api/param_description.html metodo=_data parametro="File f" %}
* **RandomAccessFile raf**,  {% include w3api/param_description.html metodo=_data parametro="RandomAccessFile raf" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/), [SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FileImageOutputStream](/Java/FileImageOutputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileImageOutputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
