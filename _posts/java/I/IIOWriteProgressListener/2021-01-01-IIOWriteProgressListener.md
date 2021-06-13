---
title: IIOWriteProgressListener
permalink: /Java/IIOWriteProgressListener/
date: 2021-01-11
key: Java.I.IIOWriteProgressListener
category: Java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IIOWriteProgressListener.description }}

## Sintaxis
~~~java
public interface IIOWriteProgressListener extends EventListener
~~~

## Métodos
* [imageComplete()](/Java/IIOWriteProgressListener/imageComplete)
* [imageProgress()](/Java/IIOWriteProgressListener/imageProgress)
* [imageStarted()](/Java/IIOWriteProgressListener/imageStarted)
* [thumbnailComplete()](/Java/IIOWriteProgressListener/thumbnailComplete)
* [thumbnailProgress()](/Java/IIOWriteProgressListener/thumbnailProgress)
* [thumbnailStarted()](/Java/IIOWriteProgressListener/thumbnailStarted)
* [writeAborted()](/Java/IIOWriteProgressListener/writeAborted)

## Ejemplo
~~~java
{{ site.data.Java.I.IIOWriteProgressListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOWriteProgressListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
