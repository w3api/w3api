---
title: StandardCopyOption
permalink: Java/StandardCopyOption
date: 2021-01-04
key: JavaJava.S.StandardCopyOption
category: java
tags: ['java se', 'java.nio.file', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StandardCopyOption.description }}

## Sintaxis
~~~java
public enum StandardCopyOption extends Enum<StandardCopyOption> implements CopyOption
~~~

## Enumerados
* [ATOMIC_MOVE](/Java/StandardCopyOption/ATOMIC_MOVE)
* [COPY_ATTRIBUTES](/Java/StandardCopyOption/COPY_ATTRIBUTES)
* [REPLACE_EXISTING](/Java/StandardCopyOption/REPLACE_EXISTING)

## Métodos
* [valueOf()](/Java/StandardCopyOption/valueOf)
* [values()](/Java/StandardCopyOption/values)

## Ejemplo
~~~java
{{ site.data.Java.S.StandardCopyOption.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardCopyOption.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
