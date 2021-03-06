---
title: StackFrame.visibleVariables()
permalink: /Java/StackFrame/visibleVariables/
date: 2021-01-11
key: Java.S.StackFrame
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackFrame.metodos valor="visibleVariables" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
List<LocalVariable> visibleVariables() throws AbsentInformationException
~~~

## Excepciones
[AbsentInformationException](/Java/AbsentInformationException/), [NativeMethodException](/Java/NativeMethodException/), [InvalidStackFrameException](/Java/InvalidStackFrameException/)

## Clase Padre
[StackFrame](/Java/StackFrame/)

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
