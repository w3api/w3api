---
title: ObjectInput
permalink: /Java/ObjectInput/
date: 2021-01-11
key: JavaJava.O.ObjectInput
category: java
tags: ['java se', 'java.io', 'java.base', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectInput.description }}

## Sintaxis
~~~java
public interface ObjectInput extends DataInput, AutoCloseable
~~~

## Métodos
* [available()](/Java/ObjectInput/available)
* [close()](/Java/ObjectInput/close)
* [read()](/Java/ObjectInput/read)
* [readObject()](/Java/ObjectInput/readObject)
* [skip()](/Java/ObjectInput/skip)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectInput.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectInput.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
