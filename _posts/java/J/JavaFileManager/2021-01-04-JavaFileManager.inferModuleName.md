---
title: JavaFileManager.inferModuleName()
permalink: Java/JavaFileManager/inferModuleName
date: 2021-01-04
key: JavaJava.J.JavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="inferModuleName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default String inferModuleName(JavaFileManager.Location location) throws IOException
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager.Location location" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
