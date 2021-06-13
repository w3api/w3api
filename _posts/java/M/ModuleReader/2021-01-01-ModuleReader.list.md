---
title: ModuleReader.list()
permalink: Java/ModuleReader/list
date: 2021-01-11
key: JavaJava.M.ModuleReader
category: Java
tags: ['java se', 'java.lang.module', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModuleReader.metodos valor="list" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Stream<String> list() throws IOException
~~~

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

## Clase Padre
[ModuleReader](/Java/ModuleReader/)

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
