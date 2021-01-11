---
title: JavaFileManager.listLocationsForModules()
permalink: Java/JavaFileManager/listLocationsForModules
date: 2021-01-11
key: JavaJava.J.JavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="listLocationsForModules" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Iterable<Set<JavaFileManager.Location>> listLocationsForModules(JavaFileManager.Location location) throws IOException
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

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
