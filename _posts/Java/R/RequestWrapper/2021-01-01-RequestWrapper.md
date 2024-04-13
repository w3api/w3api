---
title: RequestWrapper
permalink: /Java/RequestWrapper/
date: 2021-01-11
key: Java.R.RequestWrapper
category: Java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'anotacion java', 'Java 1.6', 'JAX-WS 2.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RequestWrapper.description }}

## Sintaxis
~~~java
@Target(METHOD) @Retention(RUNTIME) @Documented public @interface RequestWrapper
~~~

## Elementos
* [className](/Java/RequestWrapper/className)
* [localName](/Java/RequestWrapper/localName)
* [partName](/Java/RequestWrapper/partName)
* [targetNamespace](/Java/RequestWrapper/targetNamespace)

## Ejemplo
~~~java
{{ site.data.Java.R.RequestWrapper.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RequestWrapper.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
