---
title: ObjectOutput
permalink: /Java/ObjectOutput/
date: 2021-01-11
key: JavaJava.O.ObjectOutput
category: java
tags: ['java se', 'java.io', 'java.base', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectOutput.description }}

## Sintaxis
~~~java
public interface ObjectOutput extends DataOutput, AutoCloseable
~~~

## Métodos
* [close()](/Java/ObjectOutput/close)
* [flush()](/Java/ObjectOutput/flush)
* [write()](/Java/ObjectOutput/write)
* [writeObject()](/Java/ObjectOutput/writeObject)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectOutput.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectOutput.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
