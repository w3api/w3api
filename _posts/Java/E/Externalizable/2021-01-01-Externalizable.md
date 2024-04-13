---
title: Externalizable
permalink: /Java/Externalizable/
date: 2021-01-11
key: Java.E.Externalizable
category: Java
tags: ['java se', 'java.io', 'java.base', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.Externalizable.description }}

## Sintaxis
~~~java
public interface Externalizable extends Serializable
~~~

## Métodos
* [readExternal()](/Java/Externalizable/readExternal/)
* [writeExternal()](/Java/Externalizable/writeExternal/)

## Ejemplo
~~~java
{{ site.data.Java.E.Externalizable.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Externalizable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
