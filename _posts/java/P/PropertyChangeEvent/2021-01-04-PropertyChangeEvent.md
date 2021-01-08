---
title: PropertyChangeEvent
permalink: Java/PropertyChangeEvent
date: 2021-01-04
key: JavaJava.P.PropertyChangeEvent
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PropertyChangeEvent.description }}

## Sintaxis
~~~java
public class PropertyChangeEvent extends EventObject
~~~

## Constructores
* [PropertyChangeEvent()](/Java/PropertyChangeEvent/PropertyChangeEvent/)

## Métodos
* [getNewValue()](/Java/PropertyChangeEvent/getNewValue)
* [getOldValue()](/Java/PropertyChangeEvent/getOldValue)
* [getPropagationId()](/Java/PropertyChangeEvent/getPropagationId)
* [getPropertyName()](/Java/PropertyChangeEvent/getPropertyName)
* [setPropagationId()](/Java/PropertyChangeEvent/setPropagationId)
* [toString()](/Java/PropertyChangeEvent/toString)

## Ejemplo
~~~java
{{ site.data.Java.P.PropertyChangeEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyChangeEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
