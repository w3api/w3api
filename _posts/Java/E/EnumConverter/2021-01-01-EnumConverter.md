---
title: EnumConverter
permalink: /Java/EnumConverter/
date: 2021-01-11
key: Java.E.EnumConverter
category: Java
tags: ['java se', 'javafx.css.converter', 'javafx.graphics', 'clase java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.EnumConverter.description }}

## Sintaxis
~~~java
public final class EnumConverter<E extends Enum<E>> extends StyleConverter<String,E>
~~~

## Constructores
* [EnumConverter()](/Java/EnumConverter/EnumConverter/)

## Métodos
* [getInstance()](/Java/EnumConverter/getInstance/)
* [readBinary()](/Java/EnumConverter/readBinary/)

## Ejemplo
~~~java
{{ site.data.Java.E.EnumConverter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.EnumConverter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
