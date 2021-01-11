---
title: RemoteCall
permalink: Java/RemoteCall
date: 2021-01-11
key: JavaJava.R.RemoteCall
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'interface java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RemoteCall.description }}

## Sintaxis
~~~java
@Deprecated public interface RemoteCall
~~~

## Métodos
* [done()](/Java/RemoteCall/done)
* [executeCall()](/Java/RemoteCall/executeCall)
* [getInputStream()](/Java/RemoteCall/getInputStream)
* [getOutputStream()](/Java/RemoteCall/getOutputStream)
* [getResultStream()](/Java/RemoteCall/getResultStream)
* [releaseInputStream()](/Java/RemoteCall/releaseInputStream)
* [releaseOutputStream()](/Java/RemoteCall/releaseOutputStream)

## Ejemplo
~~~java
{{ site.data.Java.R.RemoteCall.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RemoteCall.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
