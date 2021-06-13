---
title: PropertyChangeSupport
permalink: /Java/PropertyChangeSupport/
date: 2021-01-11
key: Java.P.PropertyChangeSupport
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PropertyChangeSupport.description }}

## Sintaxis
~~~java
public class PropertyChangeSupport extends Object implements Serializable
~~~

## Constructores
* [PropertyChangeSupport()](/Java/PropertyChangeSupport/PropertyChangeSupport/)

## Métodos
* [addPropertyChangeListener()](/Java/PropertyChangeSupport/addPropertyChangeListener)
* [fireIndexedPropertyChange()](/Java/PropertyChangeSupport/fireIndexedPropertyChange)
* [firePropertyChange()](/Java/PropertyChangeSupport/firePropertyChange)
* [getPropertyChangeListeners()](/Java/PropertyChangeSupport/getPropertyChangeListeners)
* [hasListeners()](/Java/PropertyChangeSupport/hasListeners)
* [removePropertyChangeListener()](/Java/PropertyChangeSupport/removePropertyChangeListener)

## Ejemplo
~~~java
{{ site.data.Java.P.PropertyChangeSupport.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyChangeSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
