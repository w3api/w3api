---
title: StackWalker.StackFrame.getDeclaringClass()
permalink: Java/StackWalker/StackFrame/getDeclaringClass
date: 2021-01-04
key: JavaJava.S.StackWalker.StackFrame
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackWalker.StackFrame.metodos valor="getDeclaringClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Class<?> getDeclaringClass()
~~~

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[StackWalker.StackFrame](/Java/StackWalker/StackFrame/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackWalker.StackFrame.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
