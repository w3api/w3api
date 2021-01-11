---
title: FileInputStream.FileInputStream()
permalink: Java/FileInputStream/FileInputStream
date: 2021-01-11
key: JavaJava.F.FileInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileInputStream.constructores valor="FileInputStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileInputStream(File file) throws FileNotFoundException
public FileInputStream(FileDescriptor fdObj)
public FileInputStream(String name) throws FileNotFoundException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **FileDescriptor fdObj**,  {% include w3api/param_description.html metodo=_dato parametro="FileDescriptor fdObj" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FileNotFoundException](/Java/FileNotFoundException/)

## Clase Padre
[FileInputStream](/Java/FileInputStream/)

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
