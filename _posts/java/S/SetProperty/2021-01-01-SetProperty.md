---
title: SetProperty
permalink: Java/SetProperty
date: 2021-01-11
key: JavaJava.S.SetProperty
category: java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SetProperty.description }}

## Sintaxis
~~~java
public abstract class SetProperty<E> extends ReadOnlySetProperty<E> implements Property<ObservableSet<E>>, WritableSetValue<E>
~~~

## Constructores
* [SetProperty()](/Java/SetProperty/SetProperty/)

## Métodos
* [toString()](/Java/SetProperty/toString)

## Ejemplo
~~~java
{{ site.data.Java.S.SetProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SetProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
