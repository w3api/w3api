---
title: AclEntryType
permalink: Java/AclEntryType
date: 2021-01-04
key: JavaJava.A.AclEntryType
category: java
tags: ['java se', 'java.nio.file.attribute', 'java.base', 'enumerado java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AclEntryType.description }}

## Sintaxis
~~~java
public enum AclEntryType extends Enum<AclEntryType>
~~~

## Enumerados
* [ALARM](/Java/AclEntryType/ALARM)
* [ALLOW](/Java/AclEntryType/ALLOW)
* [AUDIT](/Java/AclEntryType/AUDIT)
* [DENY](/Java/AclEntryType/DENY)

## Métodos
* [valueOf()](/Java/AclEntryType/valueOf)
* [values()](/Java/AclEntryType/values)

## Ejemplo
~~~java
{{ site.data.Java.A.AclEntryType.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AclEntryType.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
