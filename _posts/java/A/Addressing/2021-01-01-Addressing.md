---
title: Addressing
permalink: Java/Addressing
date: 2021-01-11
key: JavaJava.A.Addressing
category: java
tags: ['java se', 'javax.xml.ws.soap', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.Addressing.description }}

## Sintaxis
~~~java
@Target({TYPE,METHOD,FIELD}) @Retention(RUNTIME) @Documented @WebServiceFeatureAnnotation(id="http://www.w3.org/2005/08/addressing/module", bean=AddressingFeature.class) public @interface Addressing
~~~

## Elementos
* [enabled](/Java/Addressing/enabled)
* [required](/Java/Addressing/required)
* [responses](/Java/Addressing/responses)

## Ejemplo
~~~java
{{ site.data.Java.A.Addressing.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Addressing.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
