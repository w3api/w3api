---
title: ClassType.newInstance()
permalink: Java/ClassType/newInstance
date: 2021-01-11
key: JavaJava.C.ClassType
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassType.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectReference newInstance(ThreadReference thread, Method method, List<? extends Value> arguments, int options) throws InvalidTypeException, ClassNotLoadedException, IncompatibleThreadStateException, InvocationException
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

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
