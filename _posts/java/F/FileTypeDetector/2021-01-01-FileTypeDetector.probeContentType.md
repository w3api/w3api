---
title: FileTypeDetector.probeContentType()
permalink: Java/FileTypeDetector/probeContentType
date: 2021-01-11
key: JavaJava.F.FileTypeDetector
category: java
tags: ['java se', 'java.nio.file.spi', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileTypeDetector.metodos valor="probeContentType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String probeContentType(Path path) throws IOException
~~~

## Parámetros
* **Path path**,  {% include w3api/param_description.html metodo=_dato parametro="Path path" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[FileTypeDetector](/Java/FileTypeDetector/)

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
