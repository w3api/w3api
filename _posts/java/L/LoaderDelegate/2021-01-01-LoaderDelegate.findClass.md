---
title: LoaderDelegate.findClass()
permalink: /Java/LoaderDelegate/findClass/
date: 2021-01-11
key: Java.L.LoaderDelegate
category: Java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoaderDelegate.metodos valor="findClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Class<?> findClass(String name) throws ClassNotFoundException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[LoaderDelegate](/Java/LoaderDelegate/)

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
