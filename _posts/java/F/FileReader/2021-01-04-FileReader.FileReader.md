---
title: FileReader.FileReader()
permalink: Java/FileReader/FileReader
date: 2021-01-04
key: JavaJava.F.FileReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileReader.constructores valor="FileReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileReader(File file) throws FileNotFoundException
public FileReader(FileDescriptor fd)
public FileReader(String fileName) throws FileNotFoundException
~~~

## Parámetros
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **FileDescriptor fd**,  {% include w3api/param_description.html metodo=_data parametro="FileDescriptor fd" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/)

## Clase Padre
[FileReader](/Java/FileReader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FileReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
