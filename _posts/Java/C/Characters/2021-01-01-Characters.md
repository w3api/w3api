---
title: Characters
permalink: /Java/Characters/
date: 2021-01-11
key: Java.C.Characters
category: Java
tags: ['java se', 'javax.xml.stream.events', 'java.xml', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Characters.description }}

## Sintaxis
~~~java
public interface Characters extends XMLEvent
~~~

## Métodos
* [getData()](/Java/Characters/getData/)
* [isCData()](/Java/Characters/isCData/)
* [isIgnorableWhiteSpace()](/Java/Characters/isIgnorableWhiteSpace/)
* [isWhiteSpace()](/Java/Characters/isWhiteSpace/)

## Ejemplo
~~~java
{{ site.data.Java.C.Characters.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Characters.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
