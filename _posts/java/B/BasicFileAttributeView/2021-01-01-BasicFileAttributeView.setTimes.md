---
title: BasicFileAttributeView.setTimes()
permalink: Java/BasicFileAttributeView/setTimes
date: 2021-01-11
key: JavaJava.B.BasicFileAttributeView
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicFileAttributeView.metodos valor="setTimes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setTimes(FileTime lastModifiedTime, FileTime lastAccessTime, FileTime createTime) throws IOException
~~~

## Parámetros
* **FileTime lastAccessTime**,  {% include w3api/param_description.html metodo=_dato parametro="FileTime lastAccessTime" %}
* **FileTime lastModifiedTime**,  {% include w3api/param_description.html metodo=_dato parametro="FileTime lastModifiedTime" %}
* **FileTime createTime**,  {% include w3api/param_description.html metodo=_dato parametro="FileTime createTime" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[BasicFileAttributeView](/Java/BasicFileAttributeView/)

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
