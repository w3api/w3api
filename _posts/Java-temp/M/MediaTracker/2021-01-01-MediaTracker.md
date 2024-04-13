---
title: MediaTracker
permalink: /Java/MediaTracker/
date: 2021-01-11
key: Java.M.MediaTracker
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MediaTracker.description }}

## Sintaxis
~~~java
public class MediaTracker extends Object implements Serializable
~~~

## Constructores
* [MediaTracker()](/Java/MediaTracker/MediaTracker/)

## Campos
* [ABORTED](/Java/MediaTracker/ABORTED)
* [COMPLETE](/Java/MediaTracker/COMPLETE)
* [ERRORED](/Java/MediaTracker/ERRORED)
* [LOADING](/Java/MediaTracker/LOADING)

## Métodos
* [addImage()](/Java/MediaTracker/addImage)
* [checkAll()](/Java/MediaTracker/checkAll)
* [checkID()](/Java/MediaTracker/checkID)
* [getErrorsAny()](/Java/MediaTracker/getErrorsAny)
* [getErrorsID()](/Java/MediaTracker/getErrorsID)
* [isErrorAny()](/Java/MediaTracker/isErrorAny)
* [isErrorID()](/Java/MediaTracker/isErrorID)
* [removeImage()](/Java/MediaTracker/removeImage)
* [statusAll()](/Java/MediaTracker/statusAll)
* [statusID()](/Java/MediaTracker/statusID)
* [waitForAll()](/Java/MediaTracker/waitForAll)
* [waitForID()](/Java/MediaTracker/waitForID)

## Ejemplo
~~~java
{{ site.data.Java.M.MediaTracker.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MediaTracker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
