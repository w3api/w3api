---
title: InterfaceType.invokeMethod()
permalink: Java/InterfaceType/invokeMethod
date: 2021-01-04
key: JavaJava.I.InterfaceType
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InterfaceType.metodos valor="invokeMethod" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Value invokeMethod(ThreadReference thread, Method method, List<? extends Value> arguments, int options) throws InvalidTypeException, ClassNotLoadedException, IncompatibleThreadStateException, InvocationException
~~~

## Parámetros
* **Method method**,  {% include w3api/param_description.html metodo=_data parametro="Method method" %}
* **int options**,  {% include w3api/param_description.html metodo=_data parametro="int options" %}
* **List&lt;? extends Value&gt; arguments**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends Value> arguments" %}
* **ThreadReference thread**,  {% include w3api/param_description.html metodo=_data parametro="ThreadReference thread" %}

## Excepciones
[IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [InvocationException](/Java/InvocationException/), [InvalidTypeException](/Java/InvalidTypeException/), [ClassNotLoadedException](/Java/ClassNotLoadedException/)

## Clase Padre
[InterfaceType](/Java/InterfaceType/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InterfaceType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
