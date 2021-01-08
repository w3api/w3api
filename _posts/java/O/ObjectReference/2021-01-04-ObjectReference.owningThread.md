---
title: ObjectReference.owningThread()
permalink: Java/ObjectReference/owningThread
date: 2021-01-04
key: JavaJava.O.ObjectReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectReference.metodos valor="owningThread" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ThreadReference owningThread() throws IncompatibleThreadStateException
~~~

## Excepciones
[IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ObjectReference](/Java/ObjectReference/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectReference.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
