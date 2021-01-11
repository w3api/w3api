---
title: AbstractAction
permalink: Java/AbstractAction
date: 2021-01-10
key: JavaJava.A.AbstractAction
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AbstractAction.description }}

## Sintaxis
~~~java
public abstract class AbstractAction extends Object implements Action, Cloneable, Serializable
~~~

## Constructores
* [AbstractAction()](/Java/AbstractAction/AbstractAction/)

## Campos
* [changeSupport](/Java/AbstractAction/changeSupport)
* [enabled](/Java/AbstractAction/enabled)

## Métodos
* [addPropertyChangeListener()](/Java/AbstractAction/addPropertyChangeListener)
* [clone()](/Java/AbstractAction/clone)
* [firePropertyChange()](/Java/AbstractAction/firePropertyChange)
* [getKeys()](/Java/AbstractAction/getKeys)
* [getPropertyChangeListeners()](/Java/AbstractAction/getPropertyChangeListeners)
* [getValue()](/Java/AbstractAction/getValue)
* [isEnabled()](/Java/AbstractAction/isEnabled)
* [putValue()](/Java/AbstractAction/putValue)
* [removePropertyChangeListener()](/Java/AbstractAction/removePropertyChangeListener)
* [setEnabled()](/Java/AbstractAction/setEnabled)

## Ejemplo
~~~java
{{ site.data.Java.A.AbstractAction.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractAction.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
