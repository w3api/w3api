---
title: StandardJavaFileManager.setLocationFromPaths()
permalink: /Java/StandardJavaFileManager/setLocationFromPaths/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
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
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}
* **Collection&lt;? extends Path&gt; paths**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends Path> paths" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[StandardJavaFileManager](/Java/StandardJavaFileManager/)

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
