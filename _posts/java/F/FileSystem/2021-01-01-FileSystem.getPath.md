---
title: FileSystem.getPath()
permalink: Java/FileSystem/getPath
date: 2021-01-11
key: JavaJava.F.FileSystem
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileSystem.metodos valor="getPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Path getPath(String first, String... more)
~~~

## Parámetros
* **String first**,  {% include w3api/param_description.html metodo=_dato parametro="String first" %}
* **String... more**,  {% include w3api/param_description.html metodo=_dato parametro="String... more" %}

## Excepciones
[InvalidPathException](/Java/InvalidPathException/)

## Clase Padre
[FileSystem](/Java/FileSystem/)

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
