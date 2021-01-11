---
title: Transmitter
permalink: Java/Transmitter
date: 2021-01-11
key: JavaJava.T.Transmitter
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'interface java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.Transmitter.description }}

## Sintaxis
~~~java
public interface Transmitter extends AutoCloseable
~~~

## Métodos
* [close()](/Java/Transmitter/close)
* [getReceiver()](/Java/Transmitter/getReceiver)
* [setReceiver()](/Java/Transmitter/setReceiver)

## Ejemplo
~~~java
{{ site.data.Java.T.Transmitter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Transmitter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
