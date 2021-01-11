---
title: ThreadReference.currentContendedMonitor()
permalink: Java/ThreadReference/currentContendedMonitor
date: 2021-01-11
key: JavaJava.T.ThreadReference
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadReference.metodos valor="currentContendedMonitor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectReference currentContendedMonitor() throws IncompatibleThreadStateException
~~~

## Excepciones
[IncompatibleThreadStateException](/Java/IncompatibleThreadStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
