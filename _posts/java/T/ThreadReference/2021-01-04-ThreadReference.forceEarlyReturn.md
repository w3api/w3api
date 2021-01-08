---
title: ThreadReference.forceEarlyReturn()
permalink: Java/ThreadReference/forceEarlyReturn
date: 2021-01-04
key: JavaJava.T.ThreadReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadReference.metodos valor="forceEarlyReturn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void forceEarlyReturn(Value value) throws InvalidTypeException, ClassNotLoadedException, IncompatibleThreadStateException
~~~

## Parámetros
* **Value value**,  {% include w3api/param_description.html metodo=_data parametro="Value value" %}

## Excepciones
[IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/), [InvalidStackFrameException](/Java/InvalidStackFrameException/), [NativeMethodException](/Java/NativeMethodException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [InvalidTypeException](/Java/InvalidTypeException/), [ClassNotLoadedException](/Java/ClassNotLoadedException/)

## Clase Padre
[ThreadReference](/Java/ThreadReference/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
