---
title: NetworkChannel
permalink: Java/NetworkChannel
date: 2021-01-04
key: JavaJava.N.NetworkChannel
category: java
tags: ['java se', 'java.nio.channels', 'java.base', 'interface java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.N.NetworkChannel.description }}

## Sintaxis
~~~java
public interface NetworkChannel extends Channel
~~~

## Métodos
* [bind()](/Java/NetworkChannel/bind)
* [getLocalAddress()](/Java/NetworkChannel/getLocalAddress)
* [getOption()](/Java/NetworkChannel/getOption)
* [setOption()](/Java/NetworkChannel/setOption)
* [supportedOptions()](/Java/NetworkChannel/supportedOptions)

## Ejemplo
~~~java
{{ site.data.Java.N.NetworkChannel.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NetworkChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
