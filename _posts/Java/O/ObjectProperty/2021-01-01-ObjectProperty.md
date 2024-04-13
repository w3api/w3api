---
title: ObjectProperty
permalink: /Java/ObjectProperty/
date: 2021-01-11
key: Java.O.ObjectProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.O.ObjectProperty.description }}

## Sintaxis
~~~java
public abstract class ObjectProperty<T> extends ReadOnlyObjectProperty<T> implements Property<T>, WritableObjectValue<T>
~~~

## Constructores
* [ObjectProperty()](/Java/ObjectProperty/ObjectProperty/)

## Métodos
* [toString()](/Java/ObjectProperty/toString)

## Ejemplo
~~~java
{{ site.data.Java.O.ObjectProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
