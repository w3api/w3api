---
title: IIOReadUpdateListener
permalink: /Java/IIOReadUpdateListener/
date: 2021-01-11
key: Java.I.IIOReadUpdateListener
category: Java
tags: ['java se', 'javax.imageio.event', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.IIOReadUpdateListener.description }}

## Sintaxis
~~~java
public interface IIOReadUpdateListener extends EventListener
~~~

## Métodos
* [imageUpdate()](/Java/IIOReadUpdateListener/imageUpdate)
* [passComplete()](/Java/IIOReadUpdateListener/passComplete)
* [passStarted()](/Java/IIOReadUpdateListener/passStarted)
* [thumbnailPassComplete()](/Java/IIOReadUpdateListener/thumbnailPassComplete)
* [thumbnailPassStarted()](/Java/IIOReadUpdateListener/thumbnailPassStarted)
* [thumbnailUpdate()](/Java/IIOReadUpdateListener/thumbnailUpdate)

## Ejemplo
~~~java
{{ site.data.Java.I.IIOReadUpdateListener.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.IIOReadUpdateListener.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
