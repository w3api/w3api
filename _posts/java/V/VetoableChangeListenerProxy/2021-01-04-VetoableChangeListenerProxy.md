---
title: VetoableChangeListenerProxy
permalink: Java/VetoableChangeListenerProxy
date: 2021-01-04
key: JavaJava.V.VetoableChangeListenerProxy
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'clase java', 'Java 1.4']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.V.VetoableChangeListenerProxy.description }}

## Sintaxis
~~~java
public class VetoableChangeListenerProxy extends EventListenerProxy<VetoableChangeListener> implements VetoableChangeListener
~~~

## Constructores
* [VetoableChangeListenerProxy()](/Java/VetoableChangeListenerProxy/VetoableChangeListenerProxy/)

## Métodos
* [getPropertyName()](/Java/VetoableChangeListenerProxy/getPropertyName)
* [vetoableChange()](/Java/VetoableChangeListenerProxy/vetoableChange)

## Ejemplo
~~~java
{{ site.data.Java.V.VetoableChangeListenerProxy.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VetoableChangeListenerProxy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
