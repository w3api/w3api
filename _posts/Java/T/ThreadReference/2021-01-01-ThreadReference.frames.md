---
title: ThreadReference.frames()
permalink: /Java/ThreadReference/frames/
date: 2021-01-11
key: Java.T.ThreadReference
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadReference.metodos valor="frames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<StackFrame> frames() throws IncompatibleThreadStateException
List<StackFrame> frames(int start, int length) throws IncompatibleThreadStateException
~~~

## Parámetros
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[ThreadReference](/Java/ThreadReference/)

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
