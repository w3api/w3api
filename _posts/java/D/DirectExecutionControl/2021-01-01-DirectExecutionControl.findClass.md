---
title: DirectExecutionControl.findClass()
permalink: Java/DirectExecutionControl/findClass
date: 2021-01-11
key: JavaJava.D.DirectExecutionControl
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectExecutionControl.metodos valor="findClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected Class<?> findClass(String name) throws ClassNotFoundException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/)

## Clase Padre
[DirectExecutionControl](/Java/DirectExecutionControl/)

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
