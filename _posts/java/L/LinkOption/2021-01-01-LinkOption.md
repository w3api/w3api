---
title: LinkOption
permalink: /Java/LinkOption/
date: 2021-01-11
key: Java.L.LinkOption
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.L.LinkOption.description }}

## Sintaxis
~~~java
public enum LinkOption extends Enum<LinkOption> implements OpenOption, CopyOption
~~~

## Enumerados
* [NOFOLLOW_LINKS](/Java/LinkOption/NOFOLLOW_LINKS)

## Métodos
* [valueOf()](/Java/LinkOption/valueOf)
* [values()](/Java/LinkOption/values)

## Ejemplo
~~~java
{{ site.data.Java.L.LinkOption.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LinkOption.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
