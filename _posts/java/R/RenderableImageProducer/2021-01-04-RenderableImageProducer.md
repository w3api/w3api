---
title: RenderableImageProducer
permalink: Java/RenderableImageProducer
date: 2021-01-04
key: JavaJava.R.RenderableImageProducer
category: java
tags: ['java se', 'java.awt.image.renderable', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RenderableImageProducer.description }}

## Sintaxis
~~~java
public class RenderableImageProducer extends Object implements ImageProducer, Runnable
~~~

## Constructores
* [RenderableImageProducer()](/Java/RenderableImageProducer/RenderableImageProducer/)

## Métodos
* [addConsumer()](/Java/RenderableImageProducer/addConsumer)
* [isConsumer()](/Java/RenderableImageProducer/isConsumer)
* [removeConsumer()](/Java/RenderableImageProducer/removeConsumer)
* [requestTopDownLeftRightResend()](/Java/RenderableImageProducer/requestTopDownLeftRightResend)
* [run()](/Java/RenderableImageProducer/run)
* [setRenderContext()](/Java/RenderableImageProducer/setRenderContext)
* [startProduction()](/Java/RenderableImageProducer/startProduction)

## Ejemplo
~~~java
{{ site.data.Java.R.RenderableImageProducer.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RenderableImageProducer.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
