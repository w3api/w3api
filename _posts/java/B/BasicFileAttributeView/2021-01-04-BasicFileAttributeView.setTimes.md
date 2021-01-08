---
title: BasicFileAttributeView.setTimes()
permalink: Java/BasicFileAttributeView/setTimes
date: 2021-01-04
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
* **FileTime createTime**,  {% include w3api/param_description.html metodo=_data parametro="FileTime createTime" %}
* **FileTime lastModifiedTime**,  {% include w3api/param_description.html metodo=_data parametro="FileTime lastModifiedTime" %}
* **FileTime lastAccessTime**,  {% include w3api/param_description.html metodo=_data parametro="FileTime lastAccessTime" %}

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
{%- for _ldc in site.data.Java.B.BasicFileAttributeView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
