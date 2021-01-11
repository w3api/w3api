---
title: StringProperty
permalink: Java/StringProperty
date: 2021-01-11
key: JavaJava.S.StringProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StringProperty.description }}

## Sintaxis
~~~java
public abstract class StringProperty extends ReadOnlyStringProperty implements Property<String>, WritableStringValue
~~~

## Constructores
* [StringProperty()](/Java/StringProperty/StringProperty/)

## Métodos
* [bindBidirectional()](/Java/StringProperty/bindBidirectional)
* [toString()](/Java/StringProperty/toString)
* [unbindBidirectional()](/Java/StringProperty/unbindBidirectional)

## Ejemplo
~~~java
{{ site.data.Java.S.StringProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StringProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
