---
title: StackFrame.setValue()
permalink: /Java/StackFrame/setValue/
date: 2021-01-11
key: Java.S.StackFrame
category: Java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackFrame.metodos valor="setValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setValue(LocalVariable variable, Value value) throws InvalidTypeException, ClassNotLoadedException
~~~

## Parámetros
* **Value value**,  {% include w3api/param_description.html metodo=_dato parametro="Value value" %}
* **LocalVariable variable**,  {% include w3api/param_description.html metodo=_dato parametro="LocalVariable variable" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidTypeException](/Java/InvalidTypeException/), [ClassNotLoadedException](/Java/ClassNotLoadedException/), [InvalidStackFrameException](/Java/InvalidStackFrameException/), [VMCannotBeModifiedException](/Java/VMCannotBeModifiedException/)

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
