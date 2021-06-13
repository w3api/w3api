---
title: RowSetListener
permalink: Java/RowSetListener
date: 2021-01-11
key: Java.R.RowSetListener
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'interface java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RowSetListener.description }}

## Sintaxis
~~~java
public interface RowSetListener extends EventListener
~~~

## Métodos
* [cursorMoved()](/Java/RowSetListener/cursorMoved)
* [rowChanged()](/Java/RowSetListener/rowChanged)
* [rowSetChanged()](/Java/RowSetListener/rowSetChanged)

## Ejemplo
~~~java
{{ site.data.Java.R.RowSetListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RowSetListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
