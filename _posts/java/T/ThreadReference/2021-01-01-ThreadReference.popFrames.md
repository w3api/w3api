---
title: ThreadReference.popFrames()
permalink: /Java/ThreadReference/popFrames/
date: 2021-01-11
key: Java.T.ThreadReference
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadReference.metodos valor="popFrames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void popFrames(StackFrame frame) throws IncompatibleThreadStateException
~~~

## Parámetros
* **StackFrame frame**,  {% include w3api/param_description.html metodo=_dato parametro="StackFrame frame" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidStackFrameException](/Java/InvalidStackFrameException/), [NativeMethodException](/Java/NativeMethodException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/)

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
