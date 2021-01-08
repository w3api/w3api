---
title: StackFrame.thisObject()
permalink: Java/StackFrame/thisObject
date: 2021-01-04
key: JavaJava.S.StackFrame
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackFrame.metodos valor="thisObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ObjectReference thisObject()
~~~

## Excepciones
[InvalidStackFrameException](/Java/InvalidStackFrameException/)

## Clase Padre
[StackFrame](/Java/StackFrame/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackFrame.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
