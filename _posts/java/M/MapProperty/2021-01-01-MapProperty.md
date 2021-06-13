---
title: MapProperty
permalink: /Java/MapProperty/
date: 2021-01-11
key: Java.M.MapProperty
category: Java
tags: ['java se', 'javafx.beans.property', 'javafx.base', 'clase java', 'JavaFX 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MapProperty.description }}

## Sintaxis
~~~java
public abstract class MapProperty<K,V> extends ReadOnlyMapProperty<K,V> implements Property<ObservableMap<K,V>>, WritableMapValue<K,V>
~~~

## Constructores
* [MapProperty()](/Java/MapProperty/MapProperty/)

## Métodos
* [toString()](/Java/MapProperty/toString)

## Ejemplo
~~~java
{{ site.data.Java.M.MapProperty.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MapProperty.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
