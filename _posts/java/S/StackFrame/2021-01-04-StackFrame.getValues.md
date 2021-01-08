---
title: StackFrame.getValues()
permalink: Java/StackFrame/getValues
date: 2021-01-04
key: JavaJava.S.StackFrame
category: java
tags: ['java se', 'com.sun.jdi', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackFrame.metodos valor="getValues" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Map<LocalVariable,Value> getValues(List<? extends LocalVariable> variables)
~~~

## Parámetros
* **List&lt;? extends LocalVariable&gt; variables**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends LocalVariable> variables" %}

## Excepciones
[InvalidStackFrameException](/Java/InvalidStackFrameException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
