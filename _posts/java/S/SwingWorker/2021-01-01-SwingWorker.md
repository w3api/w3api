---
title: SwingWorker
permalink: Java/SwingWorker
date: 2021-01-11
key: JavaJava.S.SwingWorker
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SwingWorker.description }}

## Sintaxis
~~~java
public abstract class SwingWorker<T,V> extends Object implements RunnableFuture<T>
~~~

## Constructores
* [SwingWorker()](/Java/SwingWorker/SwingWorker/)

## Métodos
* [addPropertyChangeListener()](/Java/SwingWorker/addPropertyChangeListener)
* [doInBackground()](/Java/SwingWorker/doInBackground)
* [done()](/Java/SwingWorker/done)
* [execute()](/Java/SwingWorker/execute)
* [firePropertyChange()](/Java/SwingWorker/firePropertyChange)
* [get()](/Java/SwingWorker/get)
* [getProgress()](/Java/SwingWorker/getProgress)
* [getPropertyChangeSupport()](/Java/SwingWorker/getPropertyChangeSupport)
* [getState()](/Java/SwingWorker/getState)
* [process()](/Java/SwingWorker/process)
* [publish()](/Java/SwingWorker/publish)
* [removePropertyChangeListener()](/Java/SwingWorker/removePropertyChangeListener)
* [run()](/Java/SwingWorker/run)
* [setProgress()](/Java/SwingWorker/setProgress)

## Ejemplo
~~~java
{{ site.data.Java.S.SwingWorker.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SwingWorker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
