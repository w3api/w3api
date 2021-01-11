---
title: FileTypeMap.getContentType()
permalink: Java/FileTypeMap/getContentType
date: 2021-01-11
key: JavaJava.F.FileTypeMap
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileTypeMap.metodos valor="getContentType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String getContentType(File file)
public abstract String getContentType(String filename)
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **String filename**,  {% include w3api/param_description.html metodo=_dato parametro="String filename" %}

## Clase Padre
[FileTypeMap](/Java/FileTypeMap/)

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
