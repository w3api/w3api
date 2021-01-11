---
title: FileHandler.FileHandler()
permalink: Java/FileHandler/FileHandler
date: 2021-01-11
key: JavaJava.F.FileHandler
category: java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FileHandler.constructores valor="FileHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FileHandler() throws IOException, SecurityException
public FileHandler(String pattern) throws IOException, SecurityException
public FileHandler(String pattern, boolean append) throws IOException, SecurityException
public FileHandler(String pattern, int limit, int count) throws IOException, SecurityException
public FileHandler(String pattern, int limit, int count, boolean append) throws IOException, SecurityException
public FileHandler(String pattern, long limit, int count, boolean append) throws IOException
~~~

## Parámetros
* **long limit**,  {% include w3api/param_description.html metodo=_dato parametro="long limit" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}
* **String pattern**,  {% include w3api/param_description.html metodo=_dato parametro="String pattern" %}
* **int limit**,  {% include w3api/param_description.html metodo=_dato parametro="int limit" %}
* **boolean append**,  {% include w3api/param_description.html metodo=_dato parametro="boolean append" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[FileHandler](/Java/FileHandler/)

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
