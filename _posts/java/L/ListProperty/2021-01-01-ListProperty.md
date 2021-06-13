---
title: ListProperty
permalink: /Java/ListProperty/
date: 2021-01-11
key: Java.L.ListProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.ListProperty.description }}

## Sintaxis
~~~java
public abstract class ListProperty<E> extends ReadOnlyListProperty<E> implements Property<ObservableList<E>>, WritableListValue<E>
~~~

## Constructores
* [ListProperty()](/Java/ListProperty/ListProperty/)

## Métodos
* [toString()](/Java/ListProperty/toString)

## Ejemplo
~~~java
{{ site.data.Java.L.ListProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.ListProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
