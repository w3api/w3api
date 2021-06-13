---
title: ResourceMeter
permalink: /Java/ResourceMeter/
date: 2021-01-11
key: Java.R.ResourceMeter
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'interface java', '8u40']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ResourceMeter.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public interface ResourceMeter
~~~

## Métodos
* [getAllocated()](/Java/ResourceMeter/getAllocated)
* [getType()](/Java/ResourceMeter/getType)
* [getValue()](/Java/ResourceMeter/getValue)

## Ejemplo
~~~java
{{ site.data.Java.R.ResourceMeter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceMeter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
