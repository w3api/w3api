---
title: StandardJavaFileManager.setLocationFromPaths()
permalink: Java/StandardJavaFileManager/setLocationFromPaths
date: 2021-01-04
key: JavaJava.S.StandardJavaFileManager
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="setLocationFromPaths" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void setLocationFromPaths(JavaFileManager.Location location, Collection<? extends Path> paths) throws IOException
~~~

## Parámetros
* **Collection&lt;? extends Path&gt; paths**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends Path> paths" %}
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileManager.Location location" %}

## Excepciones
[IOException](/Java/IOException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StandardJavaFileManager](/Java/StandardJavaFileManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardJavaFileManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
