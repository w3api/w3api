---
title: StatementEventListener
permalink: /Java/StatementEventListener/
date: 2021-01-11
key: Java.S.StatementEventListener
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StatementEventListener.description }}

## Sintaxis
~~~java
public interface StatementEventListener extends EventListener
~~~

## Métodos
* [statementClosed()](/Java/StatementEventListener/statementClosed)
* [statementErrorOccurred()](/Java/StatementEventListener/statementErrorOccurred)

## Ejemplo
~~~java
{{ site.data.Java.S.StatementEventListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StatementEventListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
