---
title: DrbgParameters.Capability
permalink: /Java/DrbgParameters/Capability/
date: 2021-01-11
key: Java.D.DrbgParameters.Capability
category: Java
tags: ['java se', 'java.security', 'java.base', 'enumerado java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DrbgParameters.Capability.description }}

## Sintaxis
~~~java
public static enum DrbgParameters.Capability extends Enum<DrbgParameters.Capability>
~~~

## Enumerados
* [NONE](/Java/DrbgParameters/Capability/NONE)
* [PR_AND_RESEED](/Java/DrbgParameters/Capability/PR_AND_RESEED)
* [RESEED_ONLY](/Java/DrbgParameters/Capability/RESEED_ONLY)

## Métodos
* [supportsPredictionResistance()](/Java/DrbgParameters/Capability/supportsPredictionResistance)
* [supportsReseeding()](/Java/DrbgParameters/Capability/supportsReseeding)
* [valueOf()](/Java/DrbgParameters/Capability/valueOf)
* [values()](/Java/DrbgParameters/Capability/values)

## Ejemplo
~~~java
{{ site.data.Java.D.DrbgParameters.Capability.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DrbgParameters.Capability.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
