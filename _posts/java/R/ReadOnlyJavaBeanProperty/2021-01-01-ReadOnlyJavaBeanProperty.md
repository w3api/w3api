---
title: ReadOnlyJavaBeanProperty
permalink: Java/ReadOnlyJavaBeanProperty
date: 2021-01-11
key: JavaJava.R.ReadOnlyJavaBeanProperty
category: java
tags: ['java se', 'javafx.beans.property.adapter', 'javafx.base', 'interface java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ReadOnlyJavaBeanProperty.description }}

## Sintaxis
~~~java
public interface ReadOnlyJavaBeanProperty<T> extends ReadOnlyProperty<T>
~~~

## Métodos
* [dispose()](/Java/ReadOnlyJavaBeanProperty/dispose)
* [fireValueChangedEvent()](/Java/ReadOnlyJavaBeanProperty/fireValueChangedEvent)

## Ejemplo
~~~java
{{ site.data.Java.R.ReadOnlyJavaBeanProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ReadOnlyJavaBeanProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
