---
title: ResourceContext
permalink: /Java/ResourceContext/
date: 2021-01-11
key: Java.R.ResourceContext
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'interface java', '8u40']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ResourceContext.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public interface ResourceContext extends AutoCloseable
~~~

## Métodos
* [addResourceMeter()](/Java/ResourceContext/addResourceMeter)
* [bindThreadContext()](/Java/ResourceContext/bindThreadContext)
* [boundThreads()](/Java/ResourceContext/boundThreads)
* [close()](/Java/ResourceContext/close)
* [getMeter()](/Java/ResourceContext/getMeter)
* [getName()](/Java/ResourceContext/getName)
* [getResourceRequest()](/Java/ResourceContext/getResourceRequest)
* [meters()](/Java/ResourceContext/meters)
* [removeResourceMeter()](/Java/ResourceContext/removeResourceMeter)
* [requestAccurateUpdate()](/Java/ResourceContext/requestAccurateUpdate)
* [unbindThreadContext()](/Java/ResourceContext/unbindThreadContext)

## Ejemplo
~~~java
{{ site.data.Java.R.ResourceContext.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
