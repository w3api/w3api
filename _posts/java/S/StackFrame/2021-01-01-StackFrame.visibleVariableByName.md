---
title: StackFrame.visibleVariableByName()
permalink: Java/StackFrame/visibleVariableByName
date: 2021-01-11
key: JavaJava.S.StackFrame
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackFrame.metodos valor="visibleVariableByName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LocalVariable visibleVariableByName(String name) throws AbsentInformationException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

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
