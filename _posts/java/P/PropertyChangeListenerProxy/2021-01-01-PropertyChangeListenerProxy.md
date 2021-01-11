---
title: PropertyChangeListenerProxy
permalink: Java/PropertyChangeListenerProxy
date: 2021-01-11
key: JavaJava.P.PropertyChangeListenerProxy
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PropertyChangeListenerProxy.description }}

## Sintaxis
~~~java
public class PropertyChangeListenerProxy extends EventListenerProxy<PropertyChangeListener> implements PropertyChangeListener
~~~

## Constructores
* [PropertyChangeListenerProxy()](/Java/PropertyChangeListenerProxy/PropertyChangeListenerProxy/)

## Métodos
* [getPropertyName()](/Java/PropertyChangeListenerProxy/getPropertyName)
* [propertyChange()](/Java/PropertyChangeListenerProxy/propertyChange)

## Ejemplo
~~~java
{{ site.data.Java.P.PropertyChangeListenerProxy.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyChangeListenerProxy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
