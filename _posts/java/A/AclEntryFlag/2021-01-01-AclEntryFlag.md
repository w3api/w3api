---
title: AclEntryFlag
permalink: Java/AclEntryFlag
date: 2021-01-11
key: JavaJava.A.AclEntryFlag
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AclEntryFlag.description }}

## Sintaxis
~~~java
public enum AclEntryFlag extends Enum<AclEntryFlag>
~~~

## Enumerados
* [DIRECTORY_INHERIT](/Java/AclEntryFlag/DIRECTORY_INHERIT)
* [FILE_INHERIT](/Java/AclEntryFlag/FILE_INHERIT)
* [INHERIT_ONLY](/Java/AclEntryFlag/INHERIT_ONLY)
* [NO_PROPAGATE_INHERIT](/Java/AclEntryFlag/NO_PROPAGATE_INHERIT)

## Métodos
* [valueOf()](/Java/AclEntryFlag/valueOf)
* [values()](/Java/AclEntryFlag/values)

## Ejemplo
~~~java
{{ site.data.Java.A.AclEntryFlag.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AclEntryFlag.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
