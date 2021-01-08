---
title: FileSystem.close()
permalink: Java/FileSystem/close
date: 2021-01-04
key: JavaJava.F.FileSystem
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystem.metodos valor="close" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void close() throws IOException
~~~

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[FileSystem](/Java/FileSystem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileSystem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
