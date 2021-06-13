---
title: StandardJavaFileManager.getLocation()
permalink: /Java/StandardJavaFileManager/getLocation/
date: 2021-01-11
key: Java.S.StandardJavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardJavaFileManager.metodos valor="getLocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Iterable<? extends File> getLocation(JavaFileManager.Location location)
~~~

## Parámetros
* **JavaFileManager.Location location**,  {% include w3api/param_description.html metodo=_dato parametro="JavaFileManager.Location location" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

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
