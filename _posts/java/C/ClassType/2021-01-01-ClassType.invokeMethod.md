---
title: ClassType.invokeMethod()
permalink: /Java/ClassType/invokeMethod/
date: 2021-01-11
key: Java.C.ClassType
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassType.metodos valor="invokeMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Value invokeMethod(ThreadReference thread, Method method, List<? extends Value> arguments, int options) throws InvalidTypeException, ClassNotLoadedException, IncompatibleThreadStateException, InvocationException
~~~

## Parámetros
* **ThreadReference thread**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadReference thread" %}
* **Method method**,  {% include w3api/param_description.html metodo=_dato parametro="Method method" %}
* **List&lt;? extends Value&gt; arguments**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Value> arguments" %}
* **int options**,  {% include w3api/param_description.html metodo=_dato parametro="int options" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidTypeException](/Java/InvalidTypeException/), [ClassNotLoadedException](/Java/ClassNotLoadedException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/), [InvocationException](/Java/InvocationException/)

## Clase Padre
[ClassType](/Java/ClassType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
