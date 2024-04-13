---
title: Customizer
permalink: /Java/Customizer/
date: 2021-01-11
key: Java.C.Customizer
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.Customizer.description }}

## Sintaxis
~~~java
public interface Customizer
~~~

## Métodos
* [addPropertyChangeListener()](/Java/Customizer/addPropertyChangeListener/)
* [removePropertyChangeListener()](/Java/Customizer/removePropertyChangeListener/)
* [setObject()](/Java/Customizer/setObject/)

## Ejemplo
~~~java
{{ site.data.Java.C.Customizer.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.Customizer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
